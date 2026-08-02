/**
 * Learning-progress tracking backed by localStorage.
 *
 * The Academy journey is a set of "steps". Each step is identified by a
 * stable key (e.g. `path:senior-pm-path:week:1:step:2` or `read:PRN-0001`).
 * We record which steps the learner has completed and which item they are
 * currently working on, so the UI can always say "Continue where you left off".
 */

const KEY = "pa-progress-v1";

function load() {
  try {
    return JSON.parse(localStorage.getItem(KEY) || "{}");
  } catch {
    return {};
  }
}

function save(state) {
  try {
    localStorage.setItem(KEY, JSON.stringify(state));
  } catch {
    /* storage unavailable */
  }
}

/** Mark a step key complete. */
export function markDone(key) {
  const s = load();
  s.done = s.done || {};
  s.done[key] = true;
  save(s);
}

/** Unmark a step. */
export function markUndone(key) {
  const s = load();
  if (s.done) delete s.done[key];
  save(s);
}

/** Is a step complete? */
export function isDone(key) {
  return !!(load().done && load().done[key]);
}

/** Set the current step the learner is working on. */
export function setCurrent(key, meta = {}) {
  const s = load();
  s.current = { key, at: Date.now(), ...meta };
  save(s);
}

/** Current step + its metadata (or null). */
export function getCurrent() {
  const s = load();
  return s.current || null;
}

/** Count done steps within a key prefix (e.g. all steps of a path). */
export function countDone(prefix) {
  const s = load();
  const done = s.done || {};
  return Object.keys(done).filter((k) => k.startsWith(prefix)).length;
}

/** Reset all progress. */
export function resetAll() {
  try {
    localStorage.removeItem(KEY);
  } catch {
    /* noop */
  }
}
