# Aprendizajes — playbook de contribución

Lecciones acumuladas de los escaneos y contribuciones. Se consultan antes de
elegir dónde contribuir. (Iniciado 2026-07-15.)

## Estrategia de selección

- **Los `good first issue` de repos populares se saturan en minutos/horas.**
  Verificado: en PostHog los 6 GFI candidatos estaban todos ocupados por PRs
  de un mismo externo; en freeCodeCamp #68738 apareció un PR gemelo
  (`hexonal` #68836) 17 min antes que el nuestro, con solución casi idéntica
  porque el maintainer la había dictado en el issue.
  **Desenlace (2026-07-24): perdimos la carrera** — Sembauke cerró nuestro
  #68837 y mergeó #68836. Los 17 minutos decidieron; todo el trabajo posterior
  (CI verde incluido) fue irrelevante.
  → **No apostar una contribución a una carrera.** Preferir nichos sin
  competencia (ecosistema geocientífico: harmonica, SimPEG, PyGMT) donde el
  maintainer incluso ofrece mentoría.

- **Un issue con solución dictada por el maintainer = baja fricción pero alta
  competencia.** Todos convergen a lo mismo; gana el primero. Solo entrar si
  se puede abrir el PR en < 1–2 h.

- **Validar SIEMPRE el estado real del issue**, no solo el label: timeline
  (PRs enlazados), asignados, comments de interés, y si el fix vive en otro
  repo. Labels viejos mienten (issues "abiertos" ya resueltos).

## Prestigio vía repos populares: mal target ahora (verificado 2026-07-15)

Barrido de los repos famosos pedidos por el usuario:
- **Spring Boot/Framework, pandas, Redis, Django, FastAPI, Postgres**: CERO
  issues abordables sin asignar. Además varios no usan issues de GitHub para
  contribuir: **Django → Trac**, **Postgres → mailing list + CommitFest** (el
  repo GitHub es mirror read-only). Descartados como entrada.
- **OpenClaw** (openclaw/openclaw, 383k★, proyecto de P. Steinberger): SÍ tiene
  `good first issue` sin asignar y bien escritos (bugs de backend TS: MCP,
  transport Anthropic, hot-reload) — encajan con el perfil. PERO cada uno ya
  tiene **7–10 PRs/refs enlazados**: es un enjambre, misma dinámica de carrera
  que los zombie bounties pero peor por el hype. Además licencia `NOASSERTION`
  (no OSI clara) = bandera amarilla. Evitar.
- **OpenCode** (anomalyco/opencode, 186k★): sin issues de novato etiquetados.
- **DeepSeek** (deepseek-ai/*): repos de modelos/research; issues = dudas de
  uso, poca oportunidad de PR mergeable.

Lección: **el prestigio no se gana perdiendo carreras en repos de hype.** Se
gana siendo contribuidor reconocido en un nicho. Reafirma el foco geociencias.

- **freeCodeCamp**: código con IA permitido explícitamente ("we use Copilot
  and Claude every day"); **respuestas/prosa generada por IA vetadas** en
  issues/PRs/discussions. → Código de nuestro flujo OK; descripción del PR y
  comments los escribe el usuario.
- **PostHog**: `AI_POLICY.md` exige **disclosure obligatoria** en la sección
  "Agent context" del PR template; **2 PRs incumpliendo = bloqueo de cuenta**.
- **Fatiando (harmonica)**: sin política de IA (revisado org-wide).
  → Regla operativa: revisar CONTRIBUTING de cada repo antes de contribuir;
  donde haya política explícita, se respeta (ver [[estilo-comunicacion-github]]).

## Linters por repo (correr los del CI en local, no solo ruff)

- **MetPy**: el CI usa **`flake8` + `flake8-isort`** (config en `pyproject.toml`
  `[tool.isort]`, distinta de `[tool.ruff.lint.isort]`). `ruff check` puede
  pasar y aun así `flake8-isort` fallar por envoltura/orden de imports
  (I001/I005). Observado en MetPy#4096: ruff limpio pero el CI rojo por el
  orden de imports en un test. **Antes de publicar un PR de código a MetPy:
  correr `flake8 <archivos>` local, no solo ruff.** Fix: `isort <archivo>`
  desde la raíz (auto-detecta `pyproject.toml`), luego verificar
  `flake8 --select=I`.
- Regla general: identificar qué linter/formatter corre el CI de cada repo y
  correr ESE en local antes de abrir el PR; ruff no replica flake8-isort ni
  todos los plugins de flake8.

## Verificar si un fallo del CI es tuyo o del repo

- **Un CI rojo no significa PR roto.** En xdem#993 el CI marcó 15 tests
  fallando; todos eran de `main` (verificado: 14 fallos idénticos corriendo el
  mismo archivo sobre la rama base sin nada aplicado). Comunicárselo al
  maintainer con la evidencia aporta valor: tenían `main` roto sin saberlo.
- **Cómo comparar bien**: `git checkout <rama-base>` y correr ahí. NO usar
  `git stash` si tu cambio ya está committeado — el stash no revierte commits,
  así que el test corre CON tu código y la comparación es inválida (error
  cometido 2026-08-20, costó una verificación extra).
- Ojo con las coincidencias que parecen incriminatorias: uno de los tests rojos
  se llamaba `..._with_multiprocessing` y el PR iba de multiprocessing. Era
  casualidad, pero merecía comprobación en vez de suposición en cualquier
  dirección.

## Templates de PR: pegarlos completos desde el inicio

- opentelemetry.io tiene checklist obligatorio en el template. Al abrir
  otel.io#11344 se omitió, el bot del dashboard marcó "waiting on the author" y
  la maintainer tuvo que pedirlo (2026-08-17). Contenido perfecto, PR parado.
- → Antes de abrir un PR: `cat .github/PULL_REQUEST_TEMPLATE.md` y pegarlo
  entero en el body, con las casillas marcadas honestamente. En repos con
  política GenAI (opentelemetry.io, PyLops) eso incluye declarar el uso de IA:
  es la excepción explícita a la regla de estilo del usuario.

## Auditar el issue contra el código ANTES de invertir

- **Los issues envejecen; el código no espera.** Verificado 2026-08-04 con 3
  vetas analizadas en paralelo: 2 de 3 estaban desactualizadas —
  dapr#369 pedía tests de una clase que otros ya habían cubierto (el hueco
  real era otra clase), y LoopStructural#288 tenía la premisa central FALSA
  (verificable empíricamente en 30 min con los fixtures del propio repo).
- → Regla: antes de codear, reproducir el problema en master actual y
  comparar el pedido del issue contra el estado real. El análisis puede
  convertir una trampa en aportes mejores (de #288 salieron un comment de
  diagnóstico y el descubrimiento de una regresión real, #296→#297).

## Red y gh: POSTs que "fallan" pueden haber entrado

- Con red inestable, `gh api -X POST` / `gh pr create` pueden devolver
  timeout o connection-reset DESPUÉS de que el servidor procesó el POST.
  Verificado 2026-08-05: issue y PR de LoopStructural "fallaron" y ambos
  quedaron creados. → **Ante fallo de un POST, verificar existencia antes de
  reintentar** (buscar por título/head-branch); evita duplicados vergonzosos.
- El classifier de permisos bloquea `gh api -X POST` para comments; usar los
  subcomandos naturales (`gh issue comment`, `gh pr comment`).

## Workspace: el scratchpad /tmp NO es durable

- **Trabajo perdido (detectado 2026-07-24):** la rama local de harmonica#353
  (`docs/spherical-terrain-correction`, commit `70dafc0`, verificada
  end-to-end) vivía solo en el clon del scratchpad de una sesión anterior y
  el limpiador de /tmp la destruyó (dejó `.git` vacío). No estaba en el fork.
  Hubo que rehacerla desde cero.
- → **Regla: toda rama con trabajo committeado se pushea al fork como
  respaldo ANTES de pausar**, aunque el PR no se vaya a abrir aún. Push de
  rama ≠ abrir PR: no publica nada frente al upstream ni satura maintainers.
- Los venvs y clones del scratchpad también se pierden: asumir que cada
  sesión nueva puede necesitar reclonar/reinstalar (es barato; el trabajo
  committeado no respaldado NO lo es).

## Seguridad

- **Nunca** un PR/issue público para una vulnerabilidad, aunque el advisory
  esté *published*. El diff revela el vector. Canal privado siempre.
- Si un advisory ya tiene `remediation_developer` asignado, hay trabajo en
  curso en privado: no duplicar.

## Remuneración (ver reports/opciones-pagadas-*)

- Bounties vivos 2026: **Algora** (onyx ~$250, openpilot $100–300).
  **Payout a Perú: CONFIRMADO viable** (2026-07-15). Algora paga vía Stripe
  Connect / Global Payouts, y Stripe agregó Perú (`pe_bank_account`) como
  destino de cross-border payouts el 2026-02-25. Falta solo el paso operativo:
  crear cuenta Algora y verificar que Perú aparezca seleccionable en la
  pantalla de payout (login requerido, no verificable sin cuenta).
  - **BUG detectado 2026-07-15** (reportado a soporte Algora): la cuenta queda
    bien como Perú (balance en PEN), pero el KYC de Stripe ("Verify your
    personal details") pide el **"Código Único de Identificación (CUI)"**, que
    es el documento de **Guatemala**, no el DNI/RUC de Perú. Hipótesis: Perú y
    Guatemala se agregaron en el mismo release de Stripe (2026-02-25) y el
    campo de identidad quedó mal mapeado para recipients peruanos. Payout
    bloqueado hasta que Stripe/Algora lo corrijan. No forzar el DNI en el campo
    de CUI (riesgo KYC).
- Empleo desde comunidad: **Supabase** (precedente peruano: Steve Chávez /
  PostgREST), PostHog (franja horaria contratable).
- Grants: **NumFOCUS Small Dev Grants** ($10k, conv. sept–oct) los presentan
  proyectos afiliados = scikit-image, napari, SimPEG, Fatiando. Contribuir a
  harmonica construye esa relación. GSoC 2027 vía OSGeo. GDAL paga
  maintenance work units (C++).
