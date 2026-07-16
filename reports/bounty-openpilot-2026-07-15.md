# Bounty openpilot — investigación (2026-07-15)

**Veredicto: mala relación esfuerzo/recompensa. No es una buena apuesta ahora.**
Los 3 bounties sin hardware son "zombie bounties" contestados: 2+ años
abiertos, bombardeados por bots, con múltiples PRs compitiendo y **ninguno
mergeado**. Se gana solo si tu PR es el primero en mergear.

## Corrección importante sobre Algora

**comma ya NO usa Algora para openpilot.** El board `algora.io/commaai/bounties`
responde "0 open bounties". Los bounties vigentes viven en el **GitHub Project
#26** de comma (`comma.ai/bounties` redirige ahí). Implicación doble:
- El bloqueo de KYC de Algora/Perú **es irrelevante para openpilot**.
- Pero el mecanismo de pago de comma requiere login en su board; no verificable
  sin cuenta. Menos transparente que Algora.

## Protocolo de reclamo

- **No se asigna ni se reserva.** Decenas piden "assign me", los maintainers
  no asignan; conviven varios PRs por el mismo issue.
- **Gana el primer PR mergeable.** El bounty se "locka" al mergear. Flujo:
  build local → resolver → PR contra `master` cumpliendo el checklist estricto
  (<500 líneas, goal claro, pasa CI). Comentar intención es opcional y no da
  prioridad.
- comma recomienda empezar por bounties ≤ $100.

## Los 3 candidatos (todos open, sin asignar, sin PR mergeado)

| Issue | Monto (inferido) | Stack | Problema |
|---|---|---|---|
| #32425 fuzz tx messages | ~$500 (de PR #32577) | Python puro | 2+ años abierto; la parte difícil (clasificar actuación vs genérico por marca) sigue **sin resolver** — por eso nadie lo cierra. Muy disputado. |
| #33207 MetaDrive en macOS | no visible | Python | **Verificable en tu propia Mac** (bug fix). Pero el MÁS disputado: 10+ PRs en 2026, varios dicen "pasa local", ninguno mergeado. |
| #30693 MetaDrive test en CI | ~$100 (de PR #31125) | Python/CI | CPU-bound en runners gratis; openpilot nunca llega a `engageable`. El más difícil de validar, peor pago. |

Los otros 4 bounties abiertos exigen hardware (comma three/3X, harness+auto).

## Recomendación

Si se intenta, **#33207 (macOS)** es el único que puedes validar de punta a
punta en tu máquina sin hardware ni CI — pero trátalo como ejercicio de
aprendizaje/reputación, no como ingreso probable: es un long shot muy
contestado. Para ingreso real, **Algora con otros repos** (onyx, cal.com) es
mejor vía que los zombie bounties de comma.

Draft de test para #32425 (por si se retoma):
`scratchpad/draft_test_panda_safety_tx_fuzzy.py`.
