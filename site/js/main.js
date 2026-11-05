// The page: a room, a PS2 you can take apart or blow up, and everything about RIPPCSX2 in a glass panel. A cousin of BIBLE's site:
// the same sky, floor, towers and fire (fx.js and towers.js are its files), with real models from tools/site/blender in place of the TVs.
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { createField } from './towers.js';
import { FX, Boom } from './fx.js';

const $ = (id) => document.getElementById(id);
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const coarse = matchMedia('(pointer: coarse)').matches;
const lowGuess = coarse && Math.min(screen.width, screen.height) < 700;

const st = { sound: '1', flash: 'full', ...(() => { try { return JSON.parse(localStorage.getItem('rippcsx2-site')) || {}; } catch { return {}; } })() };
const save = () => { try { localStorage.setItem('rippcsx2-site', JSON.stringify(st)); } catch { /* not kept */ } };

// ---- the renderer ----
const canvas = $('stage');
let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: false, powerPreference: 'high-performance' });
  if (!renderer.capabilities.isWebGL2) throw new Error('WebGL 2');
} catch {
  $('nogl').hidden = false;
  throw new Error('no WebGL');
}
renderer.toneMapping = THREE.NoToneMapping;
renderer.setClearColor(0x000000, 1);

const q = { level: lowGuess ? 0 : 1, dpr: 1 };
const budget = q.level ? 1 : 0.45;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(24, 1, 0.05, 80);
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.03).texture;
scene.environmentIntensity = 0.42;

const composer = new EffectComposer(renderer, new THREE.WebGLRenderTarget(4, 4, { type: THREE.HalfFloatType, samples: q.level ? 4 : 2 }));
composer.addPass(new RenderPass(scene, camera));
composer.addPass(new ShaderPass({ // nothing bad reaches the bloom (BIBLE's site found NaNs smeared across the frame without this)
  uniforms: { tDiffuse: { value: null } },
  vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
  fragmentShader: `uniform sampler2D tDiffuse; varying vec2 vUv;
    void main(){ vec3 c = texture2D(tDiffuse, vUv).rgb;
      if (!(c.r >= 0.0)) c.r = 0.0; if (!(c.g >= 0.0)) c.g = 0.0; if (!(c.b >= 0.0)) c.b = 0.0;
      gl_FragColor = vec4(min(c, vec3(24.0)), 1.0); }`,
}));
const bloom = new UnrealBloomPass(new THREE.Vector2(1, 1), 0.28, 0.5, 0.84);
composer.addPass(bloom);
composer.addPass(new OutputPass());

// ---- the room: RIPPS2's sky round it, the floor's grid under it, its towers far behind ----
const srgb = (hex, k = 1) => new THREE.Color(hex).multiplyScalar(k);
const roomU = { uTop: { value: srgb(0x02061c, 0.9) }, uMid: { value: srgb(0x0a1646, 0.42) }, uLow: { value: srgb(0x01030d, 0.8) } };
const room = new THREE.Mesh(new THREE.SphereGeometry(40, 32, 16), new THREE.ShaderMaterial({
  side: THREE.BackSide, depthWrite: false, uniforms: roomU,
  vertexShader: 'varying vec3 vP; void main(){ vP = position; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
  fragmentShader: `uniform vec3 uTop, uMid, uLow; varying vec3 vP;
    void main(){ float y = normalize(vP).y; vec3 c = y > 0.04 ? mix(uMid, uTop, smoothstep(0.04, 0.42, y)) : mix(uMid, uLow, smoothstep(0.04, -0.2, y)); gl_FragColor = vec4(c, 1.0); }`,
}));
room.renderOrder = -2;
scene.add(room);

const floorU = {
  uGrid: { value: srgb(0x2f6bff, 0.5) }, uFar: { value: srgb(0x0a1646, 0.14) }, uBurn: { value: 0 }, uFire: { value: 0 }, uHalf: { value: new THREE.Vector2(0.3, 0.2) },
};
const floor = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), new THREE.ShaderMaterial({
  uniforms: floorU,
  vertexShader: 'varying vec3 vW; void main(){ vec4 w = modelMatrix * vec4(position, 1.0); vW = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }',
  fragmentShader: `uniform vec3 uGrid, uFar; uniform float uBurn, uFire; uniform vec2 uHalf; varying vec3 vW;
    float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    float noise(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y); }
    void main(){
      vec2 p = vW.xz; float d = length(p);
      vec2 c = p / 0.4 + 0.5; vec2 g = abs(fract(c - 0.5) - 0.5) / fwidth(c); float line = 1.0 - min(min(g.x, g.y), 1.0);
      vec3 col = uFar + uGrid * line * 0.5 * exp(-d * 0.22);
      col += uGrid * 0.05 * exp(-d * d * 0.9);
      vec2 s = abs(p) - uHalf;
      float contact = 1.0 - smoothstep(0.0, 0.18, max(s.x, s.y));
      col *= 1.0 - contact * 0.85;
      float burn = smoothstep(0.42, 0.75, noise(p * 7.0) * 0.5 + 0.5 - length(p) * 0.62) * uBurn;
      col = mix(col, vec3(0.002), burn * 0.9);
      col += vec3(1.5, 0.55, 0.12) * uFire * exp(-d * d * 1.9) * 0.55;
      col = mix(col, uFar * 1.2, smoothstep(2.6, 11.0, d));
      gl_FragColor = vec4(col, 1.0);
    }`,
}));
floor.rotation.x = -Math.PI / 2;
scene.add(floor);

const backdrop = createField({ grid: 11, spacing: 2.4, motes: q.level ? 90 : 0, mirror: false, floor: false, sky: false, fogDensity: 0.03 });
backdrop.group.scale.setScalar(0.34);
backdrop.group.position.set(0, -0.02, -7.4);
backdrop.setMoteScale(0.8);
backdrop.colors.base.copy(srgb(0x0a1a52, 0.6));
backdrop.colors.glow.copy(srgb(0x2f6bff, 0.32));
backdrop.colors.rim.copy(srgb(0x7ec2ff, 0.3));
backdrop.colors.horizon.copy(srgb(0x0a1646, 0.42));
backdrop.fogColor.copy(srgb(0x0a1646, 0.42));
scene.add(backdrop.group);
backdrop.pose(14);

const key = new THREE.DirectionalLight(0xf4f4ff, 1.15);
key.position.set(-0.9, 2.6, 1.8);
const fill = new THREE.DirectionalLight(0xb0bcff, 0.22);
fill.position.set(2.4, 0.8, 1.2);
const rimL = new THREE.DirectionalLight(0x5a8cff, 0.7);
rimL.position.set(0.4, 0.8, -2.6);
scene.add(key, fill, rimL);

// ---- the consoles ----
const SCALE = 2.0; // real millimetres are small next to the fire and the grid; the room is built for something this size
const SPEC = {
  fat: { file: 'models/ps2-fat.glb', w: 0.301, d: 0.182, h: 0.078, label: 'PS2, SCPH-30001 era', other: 'Slim' },
  slim: { file: 'models/ps2-slim.glb', w: 0.23, d: 0.152, h: 0.028, label: 'PS2 slim, SCPH-70001', other: 'Fat' },
};
const NAMES = {
  lid: 'The lid', tray: 'The disc tray', disc: 'A DVD', controller_board: 'Controller ports and memory cards', buttons: 'Reset and eject', base: 'The lower shell', usb_board: 'USB and i.LINK',
  dvd_drive: 'The DVD drive', top_shield: 'The top shield', bottom_shield: 'The bottom shield', main_board: 'The main board', power_board: 'The power board', power_inlet: 'The mains inlet', fan: 'The fan',
  expansion_bay: 'The expansion bay', isolation_sheet: 'The insulating sheet', band: 'The band', shell: 'The top plates', card_doors: 'The memory card slots', badge: 'The PlayStation badge', rear_ports: 'The rear ports',
  top_plate: 'The top plate', bottom_plate: 'The bottom plate', battery: 'The clock battery',
};
const consoles = {};
const rig = new THREE.Group();
rig.scale.setScalar(SCALE);
scene.add(rig);

function prepare(kind, gltf) {
  const spec = SPEC[kind], root = gltf.scene;
  root.position.set(-spec.w / 2, 0, spec.d / 2);
  const parts = [];
  for (const node of [...root.children]) {
    const u = node.userData || {};
    const e = u.explode || [0, 0, 0];
    const part = {
      name: node.name, node, caption: u.caption || '', spin: u.spin || 1,
      home: node.position.clone(), homeQ: node.quaternion.clone(), apart: new THREE.Vector3(e[0], e[2], -e[1]),
      v: new THREE.Vector3(), w: new THREE.Vector3(), mats: [], k: 0, delay: 0, landed: false, thin: 0.01, flatQ: new THREE.Quaternion(),
    };
    node.traverse((o) => {
      if (!o.isMesh) return;
      o.userData.part = part;
      // each part its own materials, so the one under the pointer can light up alone
      let m = o.material;
      if (m.name === 'disc_silver') {
        const p = new THREE.MeshPhysicalMaterial({ map: m.map, metalness: 1, roughness: 0.16, iridescence: 1, iridescenceIOR: 1.6, iridescenceThicknessRange: [180, 620], name: m.name });
        m = p;
      } else m = m.clone();
      if (m.map) m.map.anisotropy = 8;
      o.material = m;
      part.mats.push({ m, em: m.emissive ? m.emissive.clone() : null, ei: m.emissiveIntensity });
    });
    // how big it is, and how it lies when it lands: on its thinnest side
    const box = new THREE.Box3().setFromObject(node), size = box.getSize(new THREE.Vector3());
    part.radius = Math.max(size.x, size.y, size.z) / 2;
    part.size = size;
    part.mass = 0.35 + Math.cbrt(size.x * size.y * size.z) * 9;
    const thinAxis = size.x < size.y && size.x < size.z ? 'x' : size.z < size.y ? 'z' : 'y';
    part.thin = size[thinAxis];
    if (thinAxis === 'x') part.flatQ.setFromAxisAngle(new THREE.Vector3(0, 0, 1), Math.PI / 2);
    else if (thinAxis === 'z') part.flatQ.setFromAxisAngle(new THREE.Vector3(1, 0, 0), Math.PI / 2);
    parts.push(part);
  }
  root.visible = false;
  rig.add(root);
  // the spread-out view's extent, for the camera
  const b = new THREE.Box3();
  for (const p of parts) b.expandByPoint(p.home.clone().add(p.apart).add(root.position));
  // each part's own size, so the spread-out view is framed round what is really there
  for (const p of parts) {
    const c = p.home.clone().add(p.apart).add(root.position);
    b.expandByPoint(c.clone().addScaledVector(p.size, 0.5));
    b.expandByPoint(c.clone().addScaledVector(p.size, -0.5));
  }
  const lift = Math.max(0, -b.min.y) + 0.01;
  b.min.y += lift;
  b.max.y += lift;
  consoles[kind] = { kind, root, parts, spec, apartBox: b, lift };
}

// ---- the state ----
const fx = new FX(scene, budget);
const boom = new Boom();
boom.on = st.sound === '1';
const state = { kind: 'fat', mode: 'whole', apartK: 0, next: null, respawnAt: 0, deadSince: 0, blinkUntil: 0, bounce: 0, hover: null, pinned: null };
const cur = () => consoles[state.kind];
let sceneT = 0, bloomKick = 0, readyTimer = 0;

const pick = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshBasicMaterial());
pick.visible = false;
rig.add(pick);

function showConsole(kind) {
  for (const c of Object.values(consoles)) c.root.visible = false;
  state.kind = kind;
  const c = consoles[kind];
  c.root.visible = true;
  for (const p of c.parts) {
    p.node.position.copy(p.home);
    p.node.quaternion.copy(p.homeQ);
    p.v.set(0, 0, 0);
    p.w.set(0, 0, 0);
    p.landed = false;
  }
  floorU.uHalf.value.set((c.spec.w * SCALE) / 2, (c.spec.d * SCALE) / 2);
  pick.scale.set(c.spec.w, c.spec.h, c.spec.d);
  pick.position.set(0, c.spec.h / 2, 0);
  $('caption').textContent = c.spec.label;
  $('swap').textContent = c.spec.other;
}

// ---- the camera ----
const view = { panel: 0, first: true, yaw: -0.55, pitch: 0.36, ty: -0.55, tp: 0.36, dist: 3, dragging: false, H: 1, W: 1, top: 0, bot: 0, shake: 0, cy: 0.1, lastDrag: -10 };

function layout() {
  const W = innerWidth, H = innerHeight;
  q.dpr = Math.min(devicePixelRatio || 1, q.level ? 2 : 1.5);
  renderer.setPixelRatio(q.dpr);
  renderer.setSize(W, H, false);
  composer.setPixelRatio(q.dpr);
  composer.setSize(W, H);
  bloom.enabled = !!q.level;
  view.W = W;
  view.H = H;
  view.top = $('top').getBoundingClientRect().bottom;
  view.bot = H - $('hud').getBoundingClientRect().top;
  camera.aspect = W / H;
  camera.updateProjectionMatrix();
  fx.setScale((H * q.dpr) / (2 * Math.tan((camera.fov * Math.PI) / 360)));
  view.first = true;
}
new ResizeObserver(layout).observe(document.documentElement);
addEventListener('orientationchange', layout);

function placeCamera(dt) {
  const c = cur(), tan = Math.tan((camera.fov * Math.PI) / 360), k = state.apartK;
  // the console fits between the bars, whichever way the screen is held, with a margin
  // with the panel open beside it, the console moves over into the space that is left
  const panelW = isOpen && view.W > 720 ? Math.min(560, view.W) : 0;
  view.panel += (panelW - view.panel) * Math.min(1, dt * 6);
  const availH = Math.max(120, view.H - view.top - view.bot - 16), availW = view.W - view.panel - 16;
  const a = c.apartBox;
  const cy = Math.cos(view.yaw), sy = Math.sin(view.yaw), cp = Math.cos(view.pitch), sp = Math.sin(view.pitch);
  const wholeW = (c.spec.w * Math.abs(cy) + c.spec.d * Math.abs(sy)) * SCALE;
  const wholeH = (c.spec.h * cp + (c.spec.d * Math.abs(cy) + c.spec.w * Math.abs(sy)) * sp) * SCALE;
  const as = a.getSize(new THREE.Vector3()).multiplyScalar(SCALE);
  const spreadW = as.x * Math.abs(cy) + as.z * Math.abs(sy);
  const spreadH = as.y * cp + (as.z * Math.abs(cy) + as.x * Math.abs(sy)) * sp;
  const w = THREE.MathUtils.lerp(wholeW, spreadW, k), h = THREE.MathUtils.lerp(wholeH, spreadH, k);
  const blast = state.mode === 'blown' ? 1.55 : 1;
  const want = (Math.max((h / (2 * tan)) * (view.H / availH), (w / (2 * tan * camera.aspect)) * (view.W / availW)) * (1.1 - 0.12 * k) + 0.2 * (1 - k)) * blast;
  view.dist = view.first ? want : view.dist + (want - view.dist) * Math.min(1, dt * 3.5);
  view.first = false;
  if (!view.dragging && sceneT - view.lastDrag > 4) {
    view.pitch += (view.tp - view.pitch) * Math.min(1, dt * 0.7);
    if (Math.abs(view.yaw) < 3.3) view.yaw += (view.ty - view.yaw) * Math.min(1, dt * 0.5);
  }
  const sway = reduced || view.dragging ? 0 : Math.sin(sceneT * 0.22) * 0.12;
  const yaw = view.yaw + sway;
  const midY = THREE.MathUtils.lerp((c.spec.h * SCALE) / 2, ((a.min.y + a.max.y) / 2) * SCALE, k);
  view.cy += (midY - view.cy) * Math.min(1, dt * 3);
  camera.position.set(Math.sin(yaw) * Math.cos(view.pitch) * view.dist, view.cy + Math.sin(view.pitch) * view.dist, Math.cos(yaw) * Math.cos(view.pitch) * view.dist);
  camera.lookAt(0, view.cy, 0);
  if (view.shake > 0.001 && !reduced) {
    camera.position.x += Math.sin(sceneT * 61) * view.shake * 0.05;
    camera.position.y += Math.sin(sceneT * 47 + 1.3) * view.shake * 0.04;
  }
  view.shake *= Math.exp(-dt * 6);
  camera.setViewOffset(view.W, view.H, view.panel / 2, (view.bot - view.top) / 2, view.W, view.H);
}

// ---- boom ----
let count = 0;
try { count = +localStorage.getItem('rippcsx2-site-blown') || 0; } catch { /* not kept */ }
$('count').textContent = count;
let lastFlash = 0, flashAnim = null;

// Never more than three full-screen flashes a second, however fast the clicks come
function flash(strength) {
  const now = performance.now();
  if (now - lastFlash < 340) return;
  lastFlash = now;
  const soft = st.flash === 'soft' || reduced;
  flashAnim?.cancel();
  flashAnim = $('flash').animate(soft ? [{ opacity: 0.1 }, { opacity: 0 }] : [{ opacity: 0.72 * strength }, { opacity: 0 }], { duration: soft ? 260 : 170, easing: 'ease-out' });
}

const WRECK_COLORS = ['#232428', '#141518', '#3a3b40', '#16705f', '#c4c8ca', '#b5721e'];

function blow(point, { power = 1 } = {}) {
  boom.unlock();
  const c = cur(), s = c.spec;
  const center = new THREE.Vector3(0, (s.h * SCALE) / 2 + 0.03, 0);
  const p = point || center;
  fx.burst(p, power);
  boom.play(power);
  view.shake = Math.min(1.4, view.shake + 0.55 * power);
  floorU.uFire.value = Math.min(1.6, floorU.uFire.value + 0.6 * power);
  floorU.uBurn.value = Math.min(1, floorU.uBurn.value + 0.16);
  bloomKick = Math.min(0.45, bloomKick + 0.16);
  count++;
  $('count').textContent = count;
  try { localStorage.setItem('rippcsx2-site-blown', count); } catch { /* not kept */ }
  $('hint').classList.add('gone');
  const now = performance.now();
  setPinned(null);
  if (state.mode !== 'blown') {
    state.mode = 'blown';
    state.deadSince = now;
    state.respawnAt = now + 3600;
    state.next = state.kind === 'fat' ? 'slim' : 'fat';
    $('apart').setAttribute('aria-pressed', 'false');
    $('apart').textContent = 'Take apart';
    state.apartK = 0;
    fx.burst(center, 1.5, { x: s.w * SCALE * 0.75, y: s.h * SCALE * 0.75 });
    fx.wreck(center, new THREE.Vector3(s.w * SCALE, Math.max(0.1, s.h * SCALE), s.d * SCALE), WRECK_COLORS);
    flash(1);
    const mid = new THREE.Vector3(0, s.h / 2, 0).sub(c.root.position);
    for (const part of c.parts) {
      const dir = part.node.position.clone().sub(mid);
      if (dir.lengthSq() < 1e-6) dir.set(0, 1, 0);
      dir.normalize();
      const sp = (0.7 + Math.random() * 0.9) / Math.sqrt(part.mass);
      part.v.set(dir.x * sp + (Math.random() - 0.5) * 0.5, Math.abs(dir.y) * sp + 0.8 + Math.random() * 0.8, dir.z * sp + (Math.random() - 0.5) * 0.5);
      const spin = part.spin * (2 + Math.random() * 6) / Math.sqrt(part.mass);
      part.w.set((Math.random() - 0.5) * spin, (Math.random() - 0.5) * spin, (Math.random() - 0.5) * spin);
      part.landed = false;
    }
  } else {
    // more on the wreck: it stays down a little longer, within reason
    state.respawnAt = Math.min(state.deadSince + 7000, Math.max(state.respawnAt, now + 1400));
    flash(0.55);
    for (const part of c.parts) { // the blast lifts what is lying near it
      const worldP = part.node.getWorldPosition(new THREE.Vector3());
      const d = worldP.distanceTo(p);
      if (d < 0.7) {
        const dir = worldP.clone().sub(p).setY(0.25).normalize(), sp = (1.3 * (1 - d / 0.7)) / Math.sqrt(part.mass);
        part.v.addScaledVector(dir, sp);
        part.v.y += sp * 0.9;
        part.w.x += (Math.random() - 0.5) * 8 * part.spin;
        part.w.z += (Math.random() - 0.5) * 8 * part.spin;
        part.landed = false;
      }
    }
  }
}

function respawn() {
  showConsole(state.next || state.kind);
  state.next = null;
  state.mode = 'whole';
  fx.clearShards();
  state.blinkUntil = performance.now() + 1150;
  state.bounce = 1;
  flash(1);
  boom.blip();
  const r = $('ready');
  r.textContent = state.kind === 'fat' ? 'FAT READY' : 'SLIM READY';
  r.classList.remove('on');
  void r.offsetWidth;
  r.classList.add('on');
  clearTimeout(readyTimer);
  readyTimer = setTimeout(() => r.classList.remove('on'), 1400);
  fx.burst(new THREE.Vector3(0, 0.02, 0.02), 0.28, { x: cur().spec.w * SCALE, y: 0.02 });
}

const upQ = new THREE.Quaternion(), tmpQ = new THREE.Quaternion(), tmpE = new THREE.Euler(), tmpV = new THREE.Vector3();
const easeOutBack = (x) => 1 + 2.2 * Math.pow(x - 1, 3) + 1.2 * Math.pow(x - 1, 2);

function updateConsole(dt) {
  const now = performance.now(), c = cur();
  const baseY = -c.root.position.y;
  if (state.mode === 'blown') {
    for (const p of c.parts) {
      const n = p.node;
      if (!p.landed) {
        p.v.y -= 2.6 * dt;
        n.position.addScaledVector(p.v, dt);
        tmpE.set(p.w.x * dt, p.w.y * dt, p.w.z * dt);
        n.quaternion.premultiply(tmpQ.setFromEuler(tmpE));
        const rest = baseY + p.radius * 0.42;
        if (n.position.y < rest) {
          n.position.y = rest;
          if (Math.abs(p.v.y) < 0.28) p.landed = true;
          p.v.y *= -0.34;
          p.v.x *= 0.62;
          p.v.z *= 0.62;
          p.w.multiplyScalar(0.55);
        }
      } else {
        // settle flat on the floor, on its thinnest side, wherever it was left facing
        const yaw = new THREE.Euler().setFromQuaternion(n.quaternion, 'YXZ').y;
        tmpQ.setFromAxisAngle(tmpV.set(0, 1, 0), yaw).multiply(p.flatQ);
        n.quaternion.slerp(tmpQ, Math.min(1, dt * 7));
        n.position.y += (baseY + p.thin / 2 + 0.001 - n.position.y) * Math.min(1, dt * 8);
        p.v.multiplyScalar(Math.exp(-dt * 6));
        n.position.x += p.v.x * dt;
        n.position.z += p.v.z * dt;
      }
    }
    if (now >= state.respawnAt) respawn();
  } else {
    const want = state.mode === 'apart' ? 1 : 0;
    state.apartK += (want - state.apartK) * Math.min(1, dt * 2.6);
    const k = state.apartK;
    for (const p of c.parts) {
      const hoverLift = p === (state.pinned || state.hover) && state.mode === 'apart' ? 0.012 : 0;
      p.k += (k - p.k) * Math.min(1, dt * (3 + (p.apart.length() * 3)));
      p.node.position.copy(p.home).addScaledVector(p.apart, p.k);
      p.node.position.y += hoverLift;
      p.node.quaternion.copy(p.homeQ);
    }
    c.root.visible = now >= state.blinkUntil || reduced || Math.floor(now / 70) % 2 === 0;
  }
  state.bounce *= Math.exp(-dt * 7);
  const b = state.bounce;
  rig.position.y = state.mode === 'blown' ? 0 : Math.abs(Math.sin(b * 7)) * 0.05 * b + state.apartK * c.lift * SCALE;
  rig.scale.setScalar(SCALE * (1 - 0.07 * b));
  floorU.uFire.value *= Math.exp(-dt * 2.2);
  floorU.uBurn.value *= Math.exp(-dt * 0.06);
  bloomKick *= Math.exp(-dt * 5);
  bloom.strength = 0.28 + bloomKick;
}

// ---- what the pointer is on ----
const LINES = [
  'It runs ELFs, OPL and homebrew the way a PS2 does.',
  'True 720p and 1080i, shown, captured and saved as an HDTV shows them.',
  'The EE\'s hardware breakpoint is there, so in-game menus work.',
  'Made to be driven by you or by an AI agent.',
  'The end goal: the whole PS2 library, tested through OPL and written down.',
];
let lineAt = 0, lineI = 0;
function setReadout(html) {
  const r = $('readout');
  if (r.dataset.html !== html) {
    r.dataset.html = html;
    r.innerHTML = html;
  }
}
function updateReadout() {
  const p = state.pinned || (state.mode !== 'blown' ? state.hover : null);
  if (p) {
    const title = NAMES[p.name] || p.name;
    const said = p.caption.toLowerCase().startsWith(title.toLowerCase());
    if (said) {
      // the caption opens by naming the part: bold that sentence, do not say it twice
      const head = p.caption.split(/\.\s/)[0].replace(/\.$/, '');
      setReadout(`<b>${head}.</b> ${p.caption.slice(head.length + 1).trim()}`);
    } else {
      setReadout(`<b>${title}.</b> ${p.caption}`);
    }
    return;
  }
  if (state.mode === 'apart') { setReadout(`<b>${coarse ? 'Tap' : 'Point at'} a part</b> to see what it has to do with RIPPCSX2.`); return; }
  if (state.mode === 'blown') { setReadout('<b>Boom.</b> The other console is on its way.'); return; }
  if (sceneT - lineAt > 6.5) { lineAt = sceneT; lineI = (lineI + 1) % LINES.length; }
  setReadout(LINES[lineI]);
}

function light(part, on) {
  if (!part) return;
  for (const { m, em, ei } of part.mats) {
    if (!em) continue;
    if (on && em.getHex() === 0) { m.emissive.setRGB(0.06, 0.12, 0.32); m.emissiveIntensity = 1; } else { m.emissive.copy(em); m.emissiveIntensity = ei; }
  }
}
function setHover(p) {
  if (state.hover === p) return;
  if (state.hover !== state.pinned) light(state.hover, false);
  state.hover = p;
  if (p && state.mode === 'apart') light(p, true);
}
function setPinned(p) {
  if (state.pinned && state.pinned !== p) light(state.pinned, false);
  state.pinned = p;
  if (p) light(p, true);
}

// ---- the pointer: a press that does not move is a shot, a drag turns the console ----
const ray = new THREE.Raycaster();
const ndc = new THREE.Vector2();
function under(e) {
  const r = canvas.getBoundingClientRect();
  ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  ray.setFromCamera(ndc, camera);
  const c = cur();
  if (!c.root.visible) return null;
  return ray.intersectObject(c.root, true).find((h) => h.object.userData.part) || null;
}
let down = null;
canvas.addEventListener('pointerdown', (e) => {
  boom.unlock();
  down = { x: e.clientX, y: e.clientY, sx: e.clientX, sy: e.clientY, moved: false };
  canvas.setPointerCapture(e.pointerId);
});
canvas.addEventListener('pointermove', (e) => {
  if (down) {
    const dx = e.clientX - down.x, dy = e.clientY - down.y;
    if (Math.hypot(e.clientX - down.sx, e.clientY - down.sy) > 9) { down.moved = true; view.dragging = true; }
    if (down.moved) {
      view.yaw -= dx * 0.0062;
      view.pitch = Math.max(0.02, Math.min(1.3, view.pitch + dy * 0.0036));
      view.lastDrag = sceneT;
    }
    down.x = e.clientX;
    down.y = e.clientY;
  } else if (!coarse) {
    const h = under(e);
    canvas.classList.toggle('aim', !!h && state.mode !== 'apart');
    setHover(h ? h.object.userData.part : null);
  }
});
canvas.addEventListener('pointerup', (e) => {
  if (down && !down.moved) {
    const h = under(e);
    if (state.mode === 'apart') {
      const p = h ? h.object.userData.part : null;
      setPinned(p === state.pinned ? null : p);
    } else if (h) blow(h.point.clone());
  }
  down = null;
  if (view.dragging) {
    view.dragging = false;
    // the turn it was given is the one it keeps: wrap to the nearest way round
    view.yaw = Math.atan2(Math.sin(view.yaw), Math.cos(view.yaw));
    view.ty = view.yaw;
  }
});
canvas.addEventListener('pointercancel', () => { down = null; view.dragging = false; });
canvas.addEventListener('pointerleave', () => setHover(null));

$('boom').onclick = () => {
  const s = cur().spec;
  blow(new THREE.Vector3((Math.random() - 0.5) * s.w, (s.h * SCALE) * (0.4 + Math.random() * 0.5) + 0.02, (Math.random() - 0.5) * s.d));
};
$('apart').onclick = () => {
  if (state.mode === 'blown') return;
  const on = state.mode !== 'apart';
  state.mode = on ? 'apart' : 'whole';
  $('apart').setAttribute('aria-pressed', on);
  $('apart').textContent = on ? 'Put back' : 'Take apart';
  $('hint').classList.add('gone');
  view.tp = on ? 0.62 : 0.36;
  if (!on) setPinned(null);
};
$('swap').onclick = () => {
  if (state.mode === 'blown') { state.next = state.next === 'fat' ? 'slim' : 'fat'; $('swap').textContent = state.next === 'fat' ? 'Slim' : 'Fat'; return; }
  blow(null, { power: 1.4 });
};
addEventListener('keydown', (e) => {
  if (document.body.classList.contains('open')) return;
  if (e.key === 'b' || e.key === 'B') $('boom').click();
  if (e.key === 'a' || e.key === 'A') $('apart').click();
});
const setMute = () => {
  const on = st.sound === '1';
  $('mute').setAttribute('aria-pressed', on);
  $('waves').toggleAttribute('hidden', !on);
  $('cross').toggleAttribute('hidden', on);
  boom.on = on;
  markRadios();
};
$('mute').onclick = () => { st.sound = st.sound === '1' ? '0' : '1'; boom.unlock(); setMute(); save(); };

// ---- the panel ----
const panel = $('panel'), hudBits = [$('hud'), $('top')];
let last = null, isOpen = false;
function openPanel() {
  if (isOpen) return;
  isOpen = true;
  last = document.activeElement;
  document.body.classList.add('show');
  void panel.offsetWidth; // shown at its start, so the slide runs
  document.body.classList.add('open');
  panel.inert = false;
  hudBits.forEach((h) => { h.inert = true; });
  $('close').focus();
}
function closePanel() {
  if (!isOpen) return;
  isOpen = false;
  document.body.classList.remove('open');
  setTimeout(() => { if (!isOpen) document.body.classList.remove('show'); }, 400);
  panel.inert = true;
  hudBits.forEach((h) => { h.inert = false; });
  last?.focus?.();
}
$('open').onclick = openPanel;
$('close').onclick = closePanel;
$('scrim').onclick = closePanel;
addEventListener('keydown', (e) => { if (e.key === 'Escape') closePanel(); });
panel.addEventListener('keydown', (e) => { // the focus stays in the panel
  if (e.key !== 'Tab') return;
  const f = [...panel.querySelectorAll('button:not([tabindex="-1"]), a, input, summary, pre')].filter((x) => x.offsetParent !== null);
  const a = f[0], z = f[f.length - 1];
  if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
  else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
});
panel.querySelectorAll('.chips a').forEach((a) => {
  a.onclick = (e) => {
    e.preventDefault();
    $(a.getAttribute('href').slice(1)).scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
  };
});
function markRadios() {
  for (const box of panel.querySelectorAll('[data-group]')) {
    const id = box.dataset.group;
    box.querySelectorAll('[role=radio]').forEach((o) => {
      const on = o.dataset.v === st[id];
      o.setAttribute('aria-checked', on);
      o.tabIndex = on ? 0 : -1;
    });
  }
}
panel.querySelectorAll('[data-group] [role=radio]').forEach((o) => {
  o.onclick = () => {
    const id = o.parentElement.dataset.group;
    st[id] = o.dataset.v;
    save();
    if (id === 'sound') { boom.unlock(); setMute(); } else markRadios();
  };
  o.onkeydown = (e) => {
    const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
    if (!d) return;
    e.preventDefault();
    const all = [...o.parentElement.children], next = all[(all.indexOf(o) + d + all.length) % all.length];
    next.focus();
    next.click();
  };
});
$('copy').onclick = async () => {
  const b = $('copy');
  try { await navigator.clipboard.writeText($('agentlink').textContent); b.textContent = 'Copied'; } catch { b.textContent = 'Select it above to copy'; }
  setTimeout(() => { b.textContent = 'Copy the link'; }, 1600);
};

// ---- go ----
setMute();
layout();
$('hint').textContent = coarse ? 'Tap the console. Drag to turn it.' : 'Click the console. Drag to turn it.';
setReadout(LINES[0]);

const loader = new GLTFLoader();
Promise.all(Object.entries(SPEC).map(async ([kind, s]) => prepare(kind, await loader.loadAsync(s.file)))).then(() => {
  showConsole('fat');
  // everything hidden is compiled up front, so the first boom does not hitch
  consoles.slim.root.visible = true;
  fx.shards.visible = true;
  placeCamera(0.016);
  renderer.compile(scene, camera);
  consoles.slim.root.visible = false;
  fx.shards.visible = false;
  requestAnimationFrame(frame);
});

let lastT = performance.now(), slow = 0, slowN = 0, frames = 0;
function frame(now) {
  requestAnimationFrame(frame);
  if (++frames === 4) { $('veil').classList.add('gone'); setTimeout(() => $('veil').remove(), 700); slow = 0; slowN = 0; }
  const dt = Math.min(0.05, (now - lastT) / 1000);
  lastT = now;
  sceneT += dt;
  updateConsole(dt);
  updateReadout();
  fx.update(dt);
  placeCamera(dt);
  if (q.level && !reduced && Math.floor(sceneT * 12) !== Math.floor((sceneT - dt) * 12)) backdrop.pose(14 + sceneT * 0.5);
  composer.render(dt);

  // a device that cannot keep up gives up the extras
  slow += dt; slowN++;
  if (slowN >= 80) {
    if (q.level && slow / slowN > 1 / 38) {
      q.level = 0;
      layout();
    }
    slow = 0; slowN = 0;
  }
}
window.__rippcsx2 = { st, blow, consoles, state, view, showConsole, camera, scene };
