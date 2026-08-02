/**
 * Resolve "what's next" across the curriculum.
 *
 * Given the current page URL and the parsed learning paths, find the next
 * step the learner should take: the first step after the current page in
 * any of the journeys that reference it, or simply the next doc in a track.
 */

import { paths } from "../data/paths.json";

// Flatten all journeys into ordered step lists.
const JOURNEYS = paths.map((p) => ({
  id: p.id,
  title: p.title,
  steps: [],
}));

paths.forEach((p, pi) => {
  p.phases.forEach((ph) =>
    ph.weeks.forEach((w) =>
      w.steps.forEach((s) => {
        JOURNEYS[pi].steps.push(s);
      }),
    ),
  );
});

/** Given a URL, return { journey, stepIndex } or null. */
export function findStepByUrl(url) {
  const normalized = url.split("?")[0].replace(/\/$/, "");
  for (const j of JOURNEYS) {
    const i = j.steps.findIndex((s) => s.route && s.route.replace(/\/$/, "") === normalized);
    if (i >= 0) return { journey: j, stepIndex: i };
  }
  return null;
}

/** Next step after the given URL (across any journey). */
export function nextStepFor(url) {
  const found = findStepByUrl(url);
  if (!found) return null;
  const { journey, stepIndex } = found;
  // advance to the next step with a route in the same journey
  for (let i = stepIndex + 1; i < journey.steps.length; i++) {
    if (journey.steps[i].route) {
      return { url: journey.steps[i].route, label: journey.steps[i].title, journey: journey.title };
    }
  }
  // journey finished → suggest the next journey or the simulator
  return { url: "/tracks/10_simulator/", label: "Try the simulator", journey: null, done: true };
}

/** Build a prev/next pair for a reading page given its URL. */
export function prevNextFor(url) {
  const found = findStepByUrl(url);
  if (!found) return { prev: null, next: null };
  const { journey, stepIndex } = found;
  let prev = null;
  for (let i = stepIndex - 1; i >= 0; i--) {
    if (journey.steps[i].route) {
      prev = { url: journey.steps[i].route, label: journey.steps[i].title };
      break;
    }
  }
  const next = nextStepFor(url);
  return { prev, next };
}
