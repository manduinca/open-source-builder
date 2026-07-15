# Deep dive: freeCodeCamp/freeCodeCamp — 2026-07-14

**Veredicto: SÍ, con un candidato claro: #68738 (API/backend).** Flujo de
merges externos muy sano (PRs de contribuidores mergeados en 2h–2 días),
protocolo sin fricción (PR directo, sin CLA/DCO). Contrapartida: no asignan
issues ("gana el primer PR válido"), competencia feroz y moderación
anti-AI-slop real y silenciosa (~47% de PRs cerrados sin merge, sin feedback).

## Validación de los 5 issues candidatos

| Issue | Estado real | Veredicto |
|---|---|---|
| **#68738** — rate-limit sobrescribe `newEmail` pendiente | Sin PRs enlazados; maintainer Sembauke confirmó y dictó la solución (2026-07-13) | ⭐ **Mejor candidato** |
| #68733 — lab RegEx requiere `RegExp` no enseñado | 2 PRs abiertos compitiendo | Saturado |
| #67770 — progreso no llega a screen readers | 7 PRs (5 rechazados) | Cementerio, evitar |
| #67605 — hint inválido workshop RDB | El fix vive en otro repo y ya hay PR allí | Evitar |
| #62452 — metadata en create-new-project | PR #66782 activo desde abril | Ocupado |

## ⭐ #68738 — detalle

- **Bug**: `PUT /update-my-email` muta `user.newEmail` *antes* del check de
  rate-limit (`emailAuthLinkTTL`); la 2.ª petición en la ventana de 5 min
  devuelve 429 pero pisa el email pendiente, invalidando el link anterior.
- **Fix esperado (dictado por Sembauke)**: mover el check del TTL antes del
  update. Regression test esperado: request A, request B inmediata → B da 429
  y `newEmail` sigue siendo el de A.
- **Tocar**: `api/src/routes/protected/settings.ts` (~línea 206) y
  `api/src/routes/protected/settings.test.ts` (describe `/update-my-email`,
  ~línea 501). Stack: Fastify + TypeScript + Prisma/MongoDB.
- **Riesgo**: dos personas comentaron interés el 2026-07-14; fCC no asigna —
  gana el primer PR correcto. Ventana: 24–48 h.

## Protocolo

- PR directo con `Closes #N` para issues `help wanted` (sin permiso previo).
- No asignan: mergean el primer PR que resuelve; ante empate priorizan el que
  tiene tests y sigue las guías. Checklist del template obligatorio en serio
  ("not just tick things off; otherwise, we won't take you seriously").
- Títulos conventional commits (`fix(api): ...`); rama propia.
- **Política de IA formal (FAQ de contribute.freecodecamp.org)**:
  - ✅ IA para código: permitido ("We use tools like GitHub Copilot and
    Claude every day").
  - ❌ Respuestas/descripciones generadas por IA en issues/PRs/discussions:
    vetadas ("We will not engage with contributors who reply through
    AI-generated content"). → La prosa del PR la escribe el usuario.
- Sin CLA/DCO. Licencia BSD-3.

## Salud (últimos 30 días)

316 PRs mergeados vs 280 cerrados sin merge (~53% de tasa). Los rechazos son
silenciosos: cero reviews, solo el mensaje boilerplate del bot camper-chan.
No pinguear a maintainers pidiendo review (lo penalizan socialmente).

## Setup

Node LTS + pnpm 10.x + MongoDB 8 replica set (`docker compose -f
docker/docker-compose.yml up -d`), `cp sample.env .env`, `pnpm install`,
`pnpm run seed`. **Para #68738 no hace falta el stack completo**: los tests
de API (vitest) solo necesitan Mongo en Docker, no el client ni el seed.

## Plan

Clone shallow → Mongo docker → reproducir con tests existentes → fix de 2–4
líneas + regression test → PR con `Closes #68738` en 24 h, descripción
escrita por el usuario.
