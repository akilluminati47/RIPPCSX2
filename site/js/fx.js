// The explosions: flames, sparks and smoke as particles the GPU moves on its own (a burst writes only its birth), wreckage, a floor shockwave, and
// the sound, synthesised on the spot so there is no audio file to ship.
import * as THREE from 'three';

const VERT = /* glsl */ `
  attribute vec3 aV;
  attribute vec4 aT;   // birth, life, size, kind (0 flame, 1 spark, 2 smoke)
  attribute float aSeed;
  uniform float uTime, uScale;
  varying float vAge, vKind, vSeed;
  void main() {
    float a = uTime - aT.x, life = max(aT.y, 0.001);
    vAge = a / life; vKind = aT.w; vSeed = aSeed;
    if (a < 0.0 || vAge >= 1.0) { gl_Position = vec4(0.0, 0.0, 2.0, 1.0); gl_PointSize = 0.0; return; }
    vec3 p = position;
    float size = aT.z;
    if (aT.w < 0.5) {            // flame: thrown out, dragged to a stop, then it climbs
      p += aV * (1.0 - exp(-3.2 * a)) / 3.2;
      p.y += 0.34 * a * a + 0.12 * a;
      p.x += sin(a * 7.0 + aSeed * 40.0) * 0.012;
      size *= 0.55 + 1.3 * smoothstep(0.0, 0.35, vAge) - 0.7 * smoothstep(0.5, 1.0, vAge);
    } else if (aT.w < 1.5) {     // spark: a straight ballistic line
      p += aV * a;
      p.y -= 2.4 * a * a;
      if (p.y < 0.004) p.y = 0.004;
      size *= 1.0 - vAge;
    } else {                     // smoke: slow, wide, rising
      p += aV * (1.0 - exp(-1.5 * a)) / 1.5;
      p.y += 0.22 * a;
      size *= 0.5 + 1.5 * vAge;
    }
    vec4 mv = modelViewMatrix * vec4(p, 1.0);
    gl_Position = projectionMatrix * mv;
    gl_PointSize = max(0.0, size) * uScale / max(0.05, -mv.z);
  }
`;
const FRAG_ADD = /* glsl */ `
  varying float vAge, vKind, vSeed;
  void main() {
    vec2 c = gl_PointCoord - 0.5;
    float r = length(c) * 2.0;
    if (r > 1.0) discard;
    if (vKind > 0.5) {                // a spark
      float a = pow(1.0 - r, 2.0) * (1.0 - vAge);
      gl_FragColor = vec4(vec3(3.2, 1.9, 0.7) * a, 1.0);
      return;
    }
    float a = pow(1.0 - r, 1.6);
    vec3 hot = mix(vec3(1.5, 1.05, 0.5), vec3(1.25, 0.42, 0.07), smoothstep(0.0, 0.3, vAge));
    vec3 col = mix(hot, vec3(0.55, 0.07, 0.015), smoothstep(0.3, 0.8, vAge));
    a *= 1.0 - smoothstep(0.5, 1.0, vAge);
    gl_FragColor = vec4(col * a * 0.62, 1.0);
  }
`;
const FRAG_SMOKE = /* glsl */ `
  varying float vAge, vSeed;
  void main() {
    vec2 c = gl_PointCoord - 0.5;
    float r = length(c) * 2.0;
    if (r > 1.0) discard;
    float a = (1.0 - smoothstep(0.2, 1.0, r)) * smoothstep(0.0, 0.12, vAge) * (1.0 - vAge) * 0.4;
    gl_FragColor = vec4(vec3(0.035 + vSeed * 0.03), a);
  }
`;

class Pool {
  constructor(size, material) {
    this.size = size;
    this.head = 0;
    const g = (this.geo = new THREE.BufferGeometry());
    const add = (n, k) => { const a = new THREE.BufferAttribute(new Float32Array(size * k), k); a.setUsage(THREE.DynamicDrawUsage); g.setAttribute(n, a); return a; };
    this.pos = add('position', 3);
    this.vel = add('aV', 3);
    this.tim = add('aT', 4);
    this.see = add('aSeed', 1);
    for (let i = 0; i < size; i++) this.tim.setXYZW(i, -1000, 1, 0, 0);
    this.points = new THREE.Points(g, material);
    this.points.frustumCulled = false;
  }

  spawn(x, y, z, vx, vy, vz, birth, life, size, kind) {
    const i = this.head;
    this.head = (i + 1) % this.size;
    this.pos.setXYZ(i, x, y, z);
    this.vel.setXYZ(i, vx, vy, vz);
    this.tim.setXYZW(i, birth, life, size, kind);
    this.see.setX(i, Math.random());
  }

  commit() {
    for (const a of [this.pos, this.vel, this.tim, this.see]) a.needsUpdate = true;
  }
}

export class FX {
  constructor(scene, budget = 1) {
    this.scene = scene;
    this.budget = budget;
    this.time = 0;
    this.uTime = { value: 0 };
    this.uScale = { value: 300 };
    const shared = { uTime: this.uTime, uScale: this.uScale };
    const add = new THREE.ShaderMaterial({ uniforms: shared, vertexShader: VERT, fragmentShader: FRAG_ADD, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending });
    const smoke = new THREE.ShaderMaterial({ uniforms: shared, vertexShader: VERT, fragmentShader: FRAG_SMOKE, transparent: true, depthWrite: false });
    this.flames = new Pool(Math.round(5000 * budget), add);
    this.smoke = new Pool(Math.round(900 * budget), smoke);
    this.smoke.points.renderOrder = 4;
    this.flames.points.renderOrder = 5;
    scene.add(this.smoke.points, this.flames.points);

    // the shockwave along the floor
    this.rings = [];
    this.ringGeo = new THREE.RingGeometry(0.97, 1, 96);
    this.ringGeo.rotateX(-Math.PI / 2);

    // wreckage: shards of cabinet and glass, thrown with their own physics
    const n = Math.round(120 * Math.max(0.5, budget));
    const shard = new THREE.TetrahedronGeometry(1);
    this.shards = new THREE.InstancedMesh(shard, new THREE.MeshStandardMaterial({ roughness: 0.5, metalness: 0.15 }), n);
    this.shards.frustumCulled = false;
    this.shards.visible = false;
    this.shardState = Array.from({ length: n }, () => ({ p: new THREE.Vector3(), v: new THREE.Vector3(), r: new THREE.Euler(), w: new THREE.Vector3(), s: 0.01 }));
    scene.add(this.shards);
    this._m = new THREE.Matrix4();
    this._q = new THREE.Quaternion();
    this._v = new THREE.Vector3();
    this._c = new THREE.Color();

    this.light = new THREE.PointLight(0xff8a3c, 0, 8, 1.6);
    scene.add(this.light);
    this.lightPower = 0;
    this.embers = []; // places that go on burning for a moment
  }

  setScale(px) { this.uScale.value = px; }

  // a fireball at p; power 1 is one click, 2 the whole set going up
  burst(p, power = 1, spread = { x: 0.2, y: 0.18 }) {
    const t = this.time, F = this.flames, S = this.smoke, b = this.budget;
    const nf = Math.round(320 * power * b), ns = Math.round(110 * power * b), nm = Math.round(30 * power * b);
    for (let i = 0; i < nf; i++) {
      const a = Math.random() * 6.283, u = Math.random() * 2 - 1, q = Math.sqrt(1 - u * u), sp = (0.25 + Math.random() * 1.15) * Math.sqrt(power);
      F.spawn(p.x + (Math.random() - 0.5) * spread.x, p.y + (Math.random() - 0.5) * spread.y, p.z + Math.random() * 0.06,
        Math.cos(a) * q * sp, u * sp * 0.8 + 0.2, Math.sin(a) * q * sp * 0.6 + 0.2, t + Math.random() * 0.09, 0.32 + Math.random() * 0.52, 0.045 + Math.random() * 0.085, 0);
    }
    for (let i = 0; i < ns; i++) {
      const a = Math.random() * 6.283, u = Math.random() * 1.8 - 0.5, sp = 1.0 + Math.random() * 2.3;
      F.spawn(p.x, p.y, p.z + 0.03, Math.cos(a) * sp, u * sp, Math.sin(a) * sp * 0.45 + 0.35, t, 0.4 + Math.random() * 0.8, 0.008 + Math.random() * 0.01, 1);
    }
    for (let i = 0; i < nm; i++) {
      const a = Math.random() * 6.283, sp = 0.25 + Math.random() * 0.6;
      S.spawn(p.x + (Math.random() - 0.5) * spread.x, p.y, p.z, Math.cos(a) * sp, 0.3 + Math.random() * 0.6, Math.sin(a) * sp, t + 0.12 + Math.random() * 0.2, 0.9 + Math.random() * 1.1, 0.14 + Math.random() * 0.2, 2);
    }
    F.commit();
    S.commit();
    this.light.position.set(p.x, p.y + 0.1, p.z + 0.4);
    this.lightPower = Math.min(5, this.lightPower + 2.2 * power);
    if (power > 0.9) this.ring(p.x, p.z, power);
  }

  ring(x, z, power) {
    const mat = new THREE.MeshBasicMaterial({ color: new THREE.Color(2.2, 1.0, 0.32), transparent: true, opacity: 0.7, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide });
    const m = new THREE.Mesh(this.ringGeo, mat);
    m.position.set(x, 0.006, z);
    this.scene.add(m);
    this.rings.push({ m, age: 0, life: 0.6, r: 0.5 + power * 0.9 });
    while (this.rings.length > 8) { const o = this.rings.shift(); this.scene.remove(o.m); o.m.material.dispose(); }
  }

  // the set comes apart: shards from its body in its own colours, and fires left burning where it stood
  wreck(center, size, colors) {
    const st = this.shardState;
    st.forEach((s, i) => {
      s.p.set(center.x + (Math.random() - 0.5) * size.x, center.y + (Math.random() - 0.5) * size.y, center.z + (Math.random() - 0.3) * size.z);
      const d = this._v.subVectors(s.p, center).normalize(), sp = 0.7 + Math.random() * 1.7;
      s.v.set(d.x * sp, d.y * sp + 0.9 + Math.random() * 1.1, d.z * sp * 0.5 + 0.25);
      s.r.set(Math.random() * 6, Math.random() * 6, Math.random() * 6);
      s.w.set(Math.random() * 12 - 6, Math.random() * 12 - 6, Math.random() * 12 - 6);
      s.s = 0.005 + Math.random() * Math.random() * 0.028;
      this.shards.setColorAt(i, this._c.set(colors[i % colors.length]));
    });
    if (this.shards.instanceColor) this.shards.instanceColor.needsUpdate = true;
    this.shards.visible = true;
    this.shardsAge = 0;
    for (let i = 0; i < 5; i++) this.embers.push({ x: center.x + (Math.random() - 0.5) * size.x, z: center.z + (Math.random() - 0.3) * size.z, age: 0, life: 1.1 + Math.random() * 0.9, acc: 0 });
  }

  clearShards() { this.shards.visible = false; this.embers.length = 0; }

  update(dt) {
    this.time += dt;
    this.uTime.value = this.time;
    this.lightPower *= Math.exp(-dt * 6);
    this.light.intensity = this.lightPower;
    for (let i = this.rings.length - 1; i >= 0; i--) {
      const r = this.rings[i];
      r.age += dt;
      const k = r.age / r.life;
      if (k >= 1) { this.scene.remove(r.m); r.m.material.dispose(); this.rings.splice(i, 1); continue; }
      r.m.scale.setScalar(0.1 + r.r * (1 - Math.pow(1 - k, 3)));
      r.m.material.opacity = 0.7 * (1 - k);
    }
    if (this.shards.visible) {
      this.shardsAge += dt;
      this.shardState.forEach((s, i) => {
        s.v.y -= 5.2 * dt;
        s.p.addScaledVector(s.v, dt);
        if (s.p.y < s.s) { s.p.y = s.s; s.v.y *= -0.32; s.v.x *= 0.6; s.v.z *= 0.6; s.w.multiplyScalar(0.5); }
        s.r.x += s.w.x * dt; s.r.y += s.w.y * dt; s.r.z += s.w.z * dt;
        this._q.setFromEuler(s.r);
        this._m.compose(s.p, this._q, this._v.setScalar(s.s));
        this.shards.setMatrixAt(i, this._m);
      });
      this.shards.instanceMatrix.needsUpdate = true;
    }
    let wrote = false;
    for (let i = this.embers.length - 1; i >= 0; i--) { // the fires on the floor
      const e = this.embers[i];
      e.age += dt;
      e.acc += dt * 70 * this.budget * (1 - e.age / e.life);
      while (e.acc >= 1) {
        e.acc -= 1;
        this.flames.spawn(e.x + (Math.random() - 0.5) * 0.14, 0.02, e.z + (Math.random() - 0.5) * 0.14, (Math.random() - 0.5) * 0.25, 0.5 + Math.random() * 0.7, (Math.random() - 0.5) * 0.25, this.time, 0.3 + Math.random() * 0.4, 0.035 + Math.random() * 0.055, 0);
        wrote = true;
      }
      if (e.age >= e.life) this.embers.splice(i, 1);
    }
    if (wrote) this.flames.commit();
  }
}

// ---- sound ----
export class Boom {
  constructor() { this.ctx = null; this.on = true; this.last = 0; }

  unlock() {
    if (this.ctx || !window.AudioContext) return;
    this.ctx = new AudioContext();
    this.out = this.ctx.createDynamicsCompressor();
    this.gain = this.ctx.createGain();
    this.gain.gain.value = 0.7;
    this.out.connect(this.gain).connect(this.ctx.destination);
    const n = this.ctx.sampleRate * 2, b = this.ctx.createBuffer(1, n, this.ctx.sampleRate), d = b.getChannelData(0);
    for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
    this.noise = b;
  }

  play(power = 1) {
    if (!this.on || !this.ctx) return;
    const c = this.ctx, t = c.currentTime;
    if (t - this.last < 0.045) return;
    this.last = t;
    if (c.state === 'suspended') c.resume();
    const dur = 0.55 + 0.75 * power, s = c.createBufferSource(), f = c.createBiquadFilter(), g = c.createGain();
    s.buffer = this.noise;
    s.playbackRate.value = 0.75 + Math.random() * 0.3;
    f.type = 'lowpass';
    f.frequency.setValueAtTime(2600, t);
    f.frequency.exponentialRampToValueAtTime(90, t + dur);
    g.gain.setValueAtTime(0.9, t);
    g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    s.connect(f).connect(g).connect(this.out);
    s.start(t, Math.random());
    s.stop(t + dur);
    const o = c.createOscillator(), og = c.createGain(); // the thump
    o.type = 'sine';
    o.frequency.setValueAtTime(130, t);
    o.frequency.exponentialRampToValueAtTime(30, t + 0.35);
    og.gain.setValueAtTime(0.85, t);
    og.gain.exponentialRampToValueAtTime(0.001, t + 0.45);
    o.connect(og).connect(this.out);
    o.start(t);
    o.stop(t + 0.5);
  }

  // the arcade's respawn: two quick square blips going up
  blip() {
    if (!this.on || !this.ctx) return;
    const c = this.ctx, t = c.currentTime;
    [0, 0.07].forEach((at, i) => {
      const o = c.createOscillator(), g = c.createGain();
      o.type = 'square';
      o.frequency.value = i ? 1320 : 880;
      g.gain.setValueAtTime(0.09, t + at);
      g.gain.exponentialRampToValueAtTime(0.001, t + at + 0.08);
      o.connect(g).connect(this.out);
      o.start(t + at);
      o.stop(t + at + 0.09);
    });
  }
}
