# Deep dive: PostHog/posthog — 2026-07-14

**Veredicto: sí con reservas.** El proyecto es genuinamente contribuible (PR directo sin asignación, sin CLA, merch por PR, historial real de contratar contribuidores, y un PR externo de `good first issue` mergeado en 5 días este mes). Pero **los 6 issues candidatos NO pasan validación**: todos están abiertos y sin asignar en apariencia, y en la práctica están ocupados por PRs abiertos, ya resueltos, o stale. La cola de `good first issue` está saturada de cazadores de contribuciones, y los PRs externos que no enganchan a un maintainer esperan 6–10 semanas bajo presión del stale-bot.

## Validación de los 6 issues

| Issue | Estado real | Área | Apto |
|---|---|---|---|
| [#31267](https://github.com/PostHog/posthog/issues/31267) Surveys: posición del widget embebido | Abierto/sin asignar, pero **2 PRs abiertos de `okxint`** (#58401 desde mayo, #68495 del 6-jul). Un comentario advierte que podría ser **paid feature** (vetado a externos). | Frontend (TS, surveys) | No — ocupado |
| [#29916](https://github.com/PostHog/posthog/issues/29916) Cohorts: `is_set` incluye `null` | Abierto, pero **5 PRs cerrados** (#36729, #53250, #58501, #59962, #65069) y **1 abierto** (#66573, 28-jun). Maintainer `haacked` pidió clarificación semántica en 2025 que nunca se cerró. | Backend (Django/ClickHouse SQL) | Condicional — mejor fit técnico, pero contested |
| [#26621](https://github.com/PostHog/posthog/issues/26621) Filtrar insights sin dashboard | Abierto, pero **PR #57345 completo (rebased, feedback atendido) espera review desde el 2-may** (10 semanas); además #58365 de `okxint`. | Full-stack | No — ocupado; además evidencia de latencia de review |
| [#19367](https://github.com/PostHog/posthog/issues/19367) BigInt crash en feature flags | **Ya resuelto**: PR #66505 (`apoorva-01`, externo) mergeado el 2026-07-02 por `haacked` con "Closes #19367"; el issue sigue abierto por descuido. | Frontend (TS) | No — resuelto (queda micro follow-up) |
| [#14579](https://github.com/PostHog/posthog/issues/14579) Ordenar barras Lifecycle | Abierto, pero **PR #62620 abierto de `okxint`** (10-jun) y dos aspirantes más comentando sin respuesta. | Frontend | No — ocupado |
| [#1289](https://github.com/PostHog/posthog/issues/1289) Filtro por usuario individual | De **2020**; en 2021 un maintainer dijo "esperen al rework de filtros"; UI cambió por completo. | Frontend | No — stale |

Patrón notable: `okxint` (externo) tiene PRs abiertos simultáneos en 3 de los 6 issues, todos sin review de maintainer, sobreviviendo a base de pings al stale-bot.

## Los 2–3 mejores objetivos (con qué tocar)

1. **#29916 (`is_set` + null en cohorts)** — el único que encaja con perfil Django/Python. Qué tocar: `posthog/models/property/util.py` (generación SQL del operador `is_set` sobre person properties: excluir `JSONExtractRaw(...) = 'null'`), tests en `ee/clickhouse/models/test/test_property.py`; verificar consistencia con el camino HogQL (`posthog/hogql/property.py`) que ya filtra null en insights. **Condición**: entrar solo si #66573 muere. El valor diferencial no es el código (trivial) sino resolver la ambigüedad semántica que `haacked` planteó y que hizo rebotar 5 PRs — responder eso primero en el issue.
2. **#19367 follow-up (bajo esfuerzo, alta probabilidad de feedback)** — `haacked` señaló en la review de #66505 que quedaban rutas con `JSON.stringify` crudo. Hacer `grep` de `JSON.stringify` en `frontend/src/scenes/feature-flags/` vs. el nuevo `safeStringify` de `frontend/src/lib/utils/json.ts`; si quedan sobras, PR pequeño; si no, comentar en el issue para que lo cierren. `haacked` responde rápido y merch-ea.
3. **#31267 / #14579 solo como plan C** si los PRs de `okxint` se cierran; en #31267 verificar antes en build local que el widget de surveys no sea paid feature.

Estrategia mejor que estos 6: los `good first issue` viejos están saturados; CONTRIBUTING sugiere explícitamente reportar/arreglar bugs frescos. Filtrar issues `bug` creados en las últimas 2–4 semanas en áreas backend (`team/feature-flags`, cohorts, HogQL) da menos competencia y el mismo protocolo.

## Protocolo de contribución

- **No asignan issues**: "just create a pull request and link the issue" (CONTRIBUTING.md). Pedir asignación (como hacen decenas en los timelines) es ruido.
- **Sin CLA**. Licencia MIT salvo `ee/` (propietario); **no aceptan contribuciones a paid features**.
- **Antes de review**: tests locales pasando, conflictos resueltos, responder al bot Greptile, cambio enfocado.
- **Política de IA (`AI_POLICY.md`)**: no anti-IA, pero exige (a) disclosure en la sección "Agent context" del PR template, (b) demo (screenshot/GIF) para frontend, (c) tests + descripción de estrategia de test para backend, (d) entender el código sin re-promptear. **2 PRs cerrados por incumplir → bloqueo de cuenta.** Issues generados por IA sin revisar se cierran sin respuesta.
- Review: el "Support Hero" semanal del equipo dueño es el primer contacto; CONTRIBUTING advierte "a few days to a couple of weeks depending on load".

## Salud / velocidad de merge

- Monorepo hiperactivo (~35.5k stars, push hoy mismo, ~100 merges/día), dominado por empleados y bots.
- **Caso favorable**: #66505 (externo, `apoorva-01`): abierto 27-jun → review con CHANGES_REQUESTED sustantivo → mergeado 2-jul (**5 días**), con `haacked` empujando los nits él mismo ("Nice work! I'm going to push some minor nits and merge it"). Tono excelente.
- **Caso desfavorable**: #57345 y #58401 (externos, completos) llevan **6–10 semanas sin review humana**, con el stale-bot amenazando cierre semanal. La varianza depende de si un maintainer del equipo dueño engancha.
- Tono en reviews: cordial y concreto; sin señales de hostilidad en nada de lo revisado.

## Setup mínimo

- **Stack completo**: `git clone --filter=blob:none`, `brew install flox`, `flox activate`, `hogli start` → Docker (recomiendan OrbStack) levanta ClickHouse, Kafka, Postgres, Redis, Zookeeper, SeaweedFS; Django/Celery/Node/React corren en host. 8 GB RAM recomendados, 4 cores. App en `localhost:8010`.
- **Subset ligero frontend**: `hogli storybook` y `hogli test frontend/src/` corren sin el stack completo — suficiente para issues tipo #19367/#14579.
- **Issues de queries (#29916)**: sí o sí ClickHouse + Postgres del `docker-compose.dev.yml`; los tests relevantes viven en `ee/clickhouse/models/test/`.

## Merch y contratación (verificado)

- Un bot envía email con **merch code al abrir un PR** en la org; hasta **$100** en merch por PR de producto y **$25** por PRs a posthog.com, a discreción ([docs/contribute/recognizing-contributions](https://posthog.com/docs/contribute/recognizing-contributions)). Cualquier empleado puede dar merch ("Merch them" es respuesta cultural); CONTRIBUTING dice que a veces dan merch **incluso si el PR no se mergea**.
- **Contratación**: PostHog confirma en su [newsletter/handbook](https://posthog.com/newsletter/open-source-benefits) que contratan gente que contribuyó a su open source — les da candidatos que ya conocen el codebase.

## Riesgos

1. **Competencia intensa** en `good first issue`: cada issue validado tenía 1–2 PRs abiertos y varios aspirantes; el trabajo puede duplicarse sin aviso porque no asignan.
2. **Latencia de review bimodal**: 5 días si enganchas maintainer, 10+ semanas si no; el stale-bot obliga a pings semanales.
3. **AI policy con dientes**: 2 strikes → bloqueo; frontend exige demo grabada.
4. **Paid features (`ee/`)** vetadas y no siempre es obvio qué es de pago (caso #31267).
5. **Escala del repo**: monorepo enorme (Python + TS + Rust + Node); el clone y el entorno no son triviales (Flox + 6 servicios Docker).
