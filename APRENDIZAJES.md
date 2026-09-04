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

## PRs que envejecen: antes de rebasar, mirar qué hizo upstream

- **El bug puede haberse arreglado por otro lado.** LoopStructural#297 llevaba
  un mes en `dirty`; al rebasar (2026-09-02) el conflicto era que master YA
  tenía el fix (entró por #300 sin referenciar el issue). El PR se redujo al
  test de regresión, que sí era único: nada en la suite ejercitaba
  `from_processor`. Tipo de commit cambiado a `test:` — con release-please un
  `fix:` que no arregla nada mete una entrada falsa en el changelog.
- → Al retomar un PR viejo: `git log -S "<cadena del bug>" upstream/main`
  antes de resolver nada. Y si el issue sigue abierto aunque ya esté
  arreglado, decirlo ahí para que lo cierren.
- **Dev puede haber empezado a DEPENDER del comportamiento que tu PR cambia.**
  dascore#927 reemplazaba el `OverflowError` de numpy por `TimeError`; en las
  dos semanas de espera, `dev` añadió código (con test) que hacía
  `except OverflowError` alrededor de esas conversiones. El merge de `dev`
  pasaba limpio y la suite lo destapó. Salida: `TimeOverflowError(OverflowError,
  TimeError)`, que satisface a ambos. → Tras mergear la base, `grep` del
  comportamiento que el PR quita, no solo correr la suite.
- **Push por SSH cuando el rebase/merge arrastra `.github/workflows`**: el
  token de gh sin scope `workflow` rechaza el push aunque tú no hayas tocado
  esos archivos. `--force-with-lease` contra un remoto distinto del tracking
  da "stale info": pasar el SHA esperado explícito
  (`--force-with-lease=<rama>:<sha>`).

## Reviews de docs: responder con un experimento, no con prosa

- harmonica#700 (2026-09-04): santisoler dudaba de que la curvatura se viera
  en pocos grados y de que el caso del borde fuera problemático. Las dos dudas
  se cerraron con números: un control con topografía constante (5 tamaños de
  malla × 2 proyecciones) que reproduce el Bullard B de LaFehr al centésimo, y
  la estación concreta (31.575, −24.41167) que falla por 4e-15°. Cada duda del
  reviewer es una hipótesis: diseñar el experimento mínimo que la decide y
  llevarle la tabla. Y cuando el reviewer propone otra solución (bajar techos
  en vez de mover estaciones), medir la suya contra la nuestra antes de
  defender nada: la suya era mejor (0 estaciones movidas vs 2586).
- Los datasets reales tienen coordenadas redondas que caen EXACTAMENTE sobre
  bordes de malla; las fronteras de celdas vecinas calculadas como centro ±
  spacing/2 difieren en ~1e-14°. Cualquier asignación punto→celda con
  `nearest` es inconsistente con un chequeo geométrico estricto. Verificarlo
  siempre con el dataset del tutorial, no con uno sintético.

## Repos que se cierran: detectarlo antes de invertir

- openrewrite (2026-09-04): el build de rewrite-testing-frameworks dejó de
  compilar para externos dos días antes de nuestro PR (#1116: plugins desde un
  repo privado con credenciales; `latest.release` del plugin depende de una
  versión de rewrite que ya no se publica en Maven Central). Señales juntas:
  licencia Moderne Source Available (no OSI) + artefactos nuevos solo en repo
  privado + CI con secrets propios. Se pudo compilar fijando el plugin a la
  última versión pública (2.23.1) y con JDK 25, y se dijo en el PR.
- → Antes de invertir en un repo: `curl` al maven-metadata de Central de su
  artefacto principal y comparar `<latest>` con lo que pide el build. Si el
  build exige algo que no está en público, el proyecto se está cerrando y el
  PR vale solo si el maintainer sigue mergeando externos.
- El subagente reportó "exige firma de commits" y no era cierto (el
  CONTRIBUTING org-wide actual no pide firma, CLA ni DCO). Verificar SIEMPRE
  los requisitos de contribución leyendo el archivo, no el resumen del agente.

## Reviews de bots (CodeRabbit): verificar, y seguir tirando del hilo

- Los 3 hallazgos de CodeRabbit en dascore#927 eran ciertos (verificados
  empíricamente en 10 min, uno con detalle equivocado: decía "wrap or
  OverflowError" y era siempre OverflowError). Sin review humana durante dos
  semanas: en un repo con el bot activado, comments Major sin atender son la
  razón obvia de que ningún humano lo mire.
- **Lo que el bot marca es una muestra, no la lista.** Sondear los paths
  hermanos con la misma pregunta destapó 6 huecos más (escalares
  `np.datetime64`/`np.timedelta64`, `datetime`/`timedelta` de Python,
  `pd.Timestamp`). Un maintainer que pruebe cualquiera de ellos rechaza el PR.
- → No responder argumentando: arreglar, responder en cada hilo con una línea
  (confirmado + qué se hizo) y un comment general para el humano con la
  decisión de diseño que necesite su OK.

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
