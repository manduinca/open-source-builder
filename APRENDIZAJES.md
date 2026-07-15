# Aprendizajes — playbook de contribución

Lecciones acumuladas de los escaneos y contribuciones. Se consultan antes de
elegir dónde contribuir. (Iniciado 2026-07-15.)

## Estrategia de selección

- **Los `good first issue` de repos populares se saturan en minutos/horas.**
  Verificado: en PostHog los 6 GFI candidatos estaban todos ocupados por PRs
  de un mismo externo; en freeCodeCamp #68738 apareció un PR gemelo
  (`hexonal` #68836) 17 min antes que el nuestro, con solución casi idéntica
  porque el maintainer la había dictado en el issue.
  → **No apostar una contribución a una carrera.** Preferir nichos sin
  competencia (ecosistema geocientífico: harmonica, SimPEG, PyGMT) donde el
  maintainer incluso ofrece mentoría.

- **Un issue con solución dictada por el maintainer = baja fricción pero alta
  competencia.** Todos convergen a lo mismo; gana el primero. Solo entrar si
  se puede abrir el PR en < 1–2 h.

- **Validar SIEMPRE el estado real del issue**, no solo el label: timeline
  (PRs enlazados), asignados, comments de interés, y si el fix vive en otro
  repo. Labels viejos mienten (issues "abiertos" ya resueltos).

## Políticas de IA por repo (varían — revisar caso a caso)

- **freeCodeCamp**: código con IA permitido explícitamente ("we use Copilot
  and Claude every day"); **respuestas/prosa generada por IA vetadas** en
  issues/PRs/discussions. → Código de nuestro flujo OK; descripción del PR y
  comments los escribe el usuario.
- **PostHog**: `AI_POLICY.md` exige **disclosure obligatoria** en la sección
  "Agent context" del PR template; **2 PRs incumpliendo = bloqueo de cuenta**.
- **Fatiando (harmonica)**: sin política de IA (revisado org-wide).
  → Regla operativa: revisar CONTRIBUTING de cada repo antes de contribuir;
  donde haya política explícita, se respeta (ver [[estilo-comunicacion-github]]).

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
- Empleo desde comunidad: **Supabase** (precedente peruano: Steve Chávez /
  PostgREST), PostHog (franja horaria contratable).
- Grants: **NumFOCUS Small Dev Grants** ($10k, conv. sept–oct) los presentan
  proyectos afiliados = scikit-image, napari, SimPEG, Fatiando. Contribuir a
  harmonica construye esa relación. GSoC 2027 vía OSGeo. GDAL paga
  maintenance work units (C++).
