# AEGIS BEFORE v2 — Build Contract

## Build this, nothing else
A mobile-first reflective PWA implementing `product/mirror-test-v2.md`.

## State machine
`ENTRY -> SELF -> READINESS -> RESILIENCE -> OPENNESS -> MIRROR -> REFLECTION -> END`

Global actions in every reflective state: `PAUSE`, `SKIP`, `EXIT`. Answer screens also allow `BACK` and `REVISE`.

## KISS UI
- One question per viewport.
- One primary action.
- 44px+ touch targets.
- No horizontal overflow at 320px width.
- Body copy remains readable without zoom.
- Progress is quiet and non-competitive; never show a score or gamified streak.
- Optional free text is secondary to guided choices.

## Cinematic progression
ENTRY: near-darkness, small torch glow.
SELF: low fog, warm local illumination.
READINESS: path/threshold becomes faintly visible.
RESILIENCE: light flickers/responds subtly; never punishing.
OPENNESS: field of view widens.
MIRROR: fog falls away and reflection plane resolves.
END: calm horizon / open path.

Visuals must never block comprehension. Respect `prefers-reduced-motion`; provide DOM/CSS fallback.

## Privacy architecture
Prototype default = local-first. Keep reflection data in device storage only unless a separate, explicit consented sync capability is later designed. Analytics events must not contain answer text or choice values. Provide clear delete-all control.

Suggested local schema:
```ts
type ReflectionSession = {
  version: 'before-v2';
  startedAt: string;
  updatedAt: string;
  responses: Record<string, { choice?: string; note?: string }>;
  mirrorFeedback: Record<string, 'yes' | 'partly' | 'no'>;
  finalReflection?: string;
};
```

## Mirror engine contract
Input: current session responses only.
Output: at most 3 reflection cards.
Each card contains `observation`, `evidenceQuestionIds`, `confidence: low|medium|high`, and optional `question`.

Rules:
1. Never diagnose.
2. Never produce a readiness percentage.
3. Never invent evidence.
4. Contradiction is framed as tension/possibility, not deception.
5. If insufficient evidence, say so.
6. User can reject/revise every observation.
7. User's correction supersedes model interpretation in the displayed personal record.

## Analytics allowlist
Allowed: anonymous session id, experience version, scene id, elapsed ms, pause, skip, revise, complete, JS error class, reduced-motion/captions/accessibility mode.
Forbidden: response text, selected answer, inferred trait, mirror content, sensitive personal detail.

## Acceptance gates
- Works on ordinary mobile without account.
- Works without WebGL/audio/camera/haptics.
- Keyboard + screen-reader path usable.
- Reduced motion respected.
- Captions/transcript available for any future audio.
- Delete removes local reflection state.
- Analytics payload inspection proves no intimate content leaves device.
- No matching/profile/swipe/compatibility marketplace code in v2 surface.
- Mirror output can always be challenged or revised.

## Freeze rule
After these gates pass, freeze features and run Working Proof #001 with 10–20 consenting Founding Witnesses. Build -> test -> fail/correct -> prove before expansion.