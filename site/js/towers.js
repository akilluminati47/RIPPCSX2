// RIPPS2's towers: the RIPPS2 site's pillars.js scene (the ELF's boot swoop is "the web theme's"), rebuilt to draw into a render target for the TV's
// screen, and as the room's far backdrop. Heights and the swoop's camera are pillars.js's own; the pointer's hover and ripples are not here.
import * as THREE from 'three';
import { PILLAR_VERT, PILLAR_FRAG, FLOOR_VERT, FLOOR_FRAG, MOTE_VERT, MOTE_FRAG, SKY_VERT, SKY_FRAG } from './pillars_glsl.js';

const COBALT = { base: '#0a1a52', glow: '#2f6bff', rim: '#7ec2ff', zenith: '#010209', horizon: '#0a1646', mote: '#8fc4ff' };
const easeOutCubic = (x) => 1 - Math.pow(1 - x, 3);
const easeInOutCubic = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
const clamp01 = (x) => Math.min(1, Math.max(0, x));
const lerp = (a, b, t) => a + (b - a) * t;

function seeded(seed) {
  let s = seed >>> 0;
  return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296);
}

export function createField({ grid = 15, spacing = 2.4, maxHeight = 13, motes = 700, mirror = true, floor = true, sky = true, fogDensity = 0.02 } = {}) {
  const colors = {};
  for (const k in COBALT) colors[k] = new THREE.Color(COBALT[k]);
  const fogColor = colors.horizon.clone().lerp(colors.glow, 0.12);
  const fog = { uFogColor: { value: fogColor }, uFogDensity: { value: fogDensity } };
  const time = { value: 0 };
  const group = new THREE.Group();

  const rand = seeded(47), half = (grid - 1) / 2, towers = [];
  for (let gx = 0; gx < grid; gx++)
    for (let gz = 0; gz < grid; gz++) {
      const x = gx - half, z = gz - half, d = Math.hypot(x, z) / half;
      if (d > 1.02) continue;
      const falloff = 0.22 + 0.78 * Math.exp(-(d * d) / (2 * 0.38 * 0.38));
      let base = falloff * (0.45 + rand() * 0.55);
      if (rand() < 0.06) base = Math.min(1.15, base * 1.6);
      towers.push({ x: x * spacing, z: z * spacing, d, base, width: spacing * (0.42 + rand() * 0.2), seed: rand(), phase: rand() * Math.PI * 2 });
    }
  const count = towers.length;
  const box = new THREE.BoxGeometry(1, 1, 1);
  box.translate(0, 0.5, 0);
  const aData = new THREE.InstancedBufferAttribute(new Float32Array(count * 4), 4);
  aData.setUsage(THREE.DynamicDrawUsage);
  box.setAttribute('aData', aData);
  const uni = (m) => ({ ...fog, uTime: time, uMirror: { value: m }, uBase: { value: colors.base }, uGlow: { value: colors.glow }, uRim: { value: colors.rim } });
  const pillars = new THREE.InstancedMesh(box, new THREE.ShaderMaterial({ uniforms: uni(0), vertexShader: PILLAR_VERT, fragmentShader: PILLAR_FRAG }), count);
  pillars.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  pillars.frustumCulled = false;
  group.add(pillars);
  if (mirror) {
    const under = new THREE.InstancedMesh(box, new THREE.ShaderMaterial({ uniforms: uni(1), vertexShader: PILLAR_VERT, fragmentShader: PILLAR_FRAG, side: THREE.BackSide }), count);
    under.instanceMatrix = pillars.instanceMatrix;
    under.scale.y = -1;
    under.frustumCulled = false;
    group.add(under);
  }
  if (floor) {
    const waves = Array.from({ length: 8 }, () => new THREE.Vector4());
    const f = new THREE.Mesh(new THREE.PlaneGeometry(600, 600), new THREE.ShaderMaterial({
      uniforms: { ...fog, uTime: time, uSpacing: { value: spacing }, uGlow: { value: colors.glow }, uRim: { value: colors.rim }, uWaves: { value: waves }, uWaveW: { value: new Array(8).fill(1) } },
      vertexShader: FLOOR_VERT, fragmentShader: FLOOR_FRAG, transparent: true, depthWrite: false,
    }));
    f.rotation.x = -Math.PI / 2;
    group.add(f);
  }
  let moteU = null;
  if (motes > 0) {
    const span = grid * spacing, pos = new Float32Array(motes * 3), seed = new Float32Array(motes);
    for (let i = 0; i < motes; i++) {
      const a = rand() * Math.PI * 2, r = Math.sqrt(rand()) * span * 0.9;
      pos.set([Math.cos(a) * r, rand() * maxHeight * 1.8, Math.sin(a) * r], i * 3);
      seed[i] = rand();
    }
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    g.setAttribute('aSeed', new THREE.BufferAttribute(seed, 1));
    moteU = { uTime: time, uHeight: { value: maxHeight * 1.8 }, uScale: { value: 1 }, uMote: { value: colors.mote } };
    const p = new THREE.Points(g, new THREE.ShaderMaterial({ uniforms: moteU, vertexShader: MOTE_VERT, fragmentShader: MOTE_FRAG, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending }));
    p.frustumCulled = false;
    group.add(p);
  }
  if (sky) {
    const s = new THREE.Mesh(new THREE.SphereGeometry(300, 32, 16), new THREE.ShaderMaterial({
      uniforms: { uTime: time, uZenith: { value: colors.zenith }, uFogColor: fog.uFogColor }, vertexShader: SKY_VERT, fragmentShader: SKY_FRAG, side: THREE.BackSide, depthWrite: false,
    }));
    s.renderOrder = -1;
    group.add(s);
  }

  const m = new THREE.Matrix4();
  function pose(t) {
    time.value = t;
    for (let i = 0; i < count; i++) {
      const tw = towers[i];
      const rise = easeOutCubic(clamp01((t - 0.3 - tw.d * 1.6) / 1.8));
      const breathe = 0.9 + 0.1 * Math.sin(t * 0.5 + tw.phase), swell = 0.5 + 0.5 * Math.sin(tw.x * 0.18 + tw.z * 0.11 - t * 0.6);
      const height = Math.max(0.05, (tw.base * breathe * maxHeight + swell * 1.4) * rise);
      m.makeScale(tw.width, height, tw.width).setPosition(tw.x, 0, tw.z);
      pillars.setMatrixAt(i, m);
      aData.setXYZW(i, tw.seed, 0, height, tw.width);
    }
    pillars.instanceMatrix.needsUpdate = true;
    aData.needsUpdate = true;
  }
  return { group, pose, colors, fogColor, setMoteScale: (v) => { if (moteU) moteU.uScale.value = v; } };
}

// The boot swoop into a render target
export function createSwoop(renderer, motes) {
  const field = createField({ motes });
  const scene = new THREE.Scene();
  scene.add(field.group);
  const camera = new THREE.PerspectiveCamera(40, 4 / 3, 0.1, 400);
  const rt = new THREE.WebGLRenderTarget(4, 4, { type: THREE.HalfFloatType, minFilter: THREE.LinearFilter, magFilter: THREE.LinearFilter, depthBuffer: true });
  function size(w, h) {
    if (rt.width === w && rt.height === h) return;
    rt.setSize(w, h);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    field.setMoteScale(h / 900);
  }
  function render(t) {
    field.pose(t);
    const intro = easeInOutCubic(clamp01(t / 5)), ang = t * 0.03 + 0.7, radius = lerp(12, 40, intro);
    camera.position.set(Math.cos(ang) * radius, lerp(1.6, 7.5, intro), Math.sin(ang) * radius);
    camera.lookAt(0, lerp(9, 10.5, intro), 0);
    renderer.setRenderTarget(rt);
    renderer.clear();
    renderer.render(scene, camera);
    renderer.setRenderTarget(null);
  }
  return { rt, size, render };
}
