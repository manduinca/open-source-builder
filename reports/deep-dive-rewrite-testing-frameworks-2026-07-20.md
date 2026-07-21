# Deep-dive: openrewrite/rewrite-testing-frameworks — 2026-07-20

**Veredicto: sí, con reservas.** Comunidad sana y rápida mergeando PRs
externos, pero la barrera técnica es real: hay que aprender el framework de
"recetas" propio de OpenRewrite (LST, `JavaVisitor`, Refaster templates)
antes de poder tocar código, y el catálogo de entrada (`good first issue`)
está prácticamente vacío y desactualizado.

## Salud de comunidad

- 99★, 103 forks, push hoy (2026-07-20) — muy activo.
- `community/profile` health 62%: tiene CONTRIBUTING.md y PR template; sin
  issue template ni Code of Conduct.
- PRs externos mergeados con velocidad real: Jammy-Louie (3 días),
  steve-aom-elliott, vlsi, juherr, neil-mushell — todos mismo día o pocos
  días. Solo 4 PRs cerrados sin merge en el histórico reciente, y de
  contribuidores recurrentes (no rechazos de primerizos).
- El repo está dominado por `timtebeek` (staff de Moderne, la empresa detrás
  de OpenRewrite), que concentra la mayoría de merges — normal en un
  proyecto respaldado por una empresa, no señal de hostilidad.

## Barrera de entrada técnica

Alta para un primer PR de código. No es Java "plano": cada recipe se escribe
sobre el LST (Lossless Semantic Tree) de OpenRewrite con `JavaVisitor` o
Refaster templates — es una API propia con curva de aprendizaje, no algo que
se infiera leyendo el código una vez. Para docs/config el listón es normal.

## Cómo empezar

Setup: Maven/Gradle estándar, sin fricción reportada. El punto de entrada
real es aprender `org.openrewrite.java.testing.*` viendo recipes existentes
como plantilla antes de escribir una propia.

| Issue | Esfuerzo | Nota |
|---|---|---|
| [#221](https://github.com/openrewrite/rewrite-testing-frameworks/issues/221) "Replace `graphql.Assert` with test assertions" | Bajo–medio | Único `good first issue` etiquetado, pero de 2022, cero comentarios — **verificar primero si sigue vigente** (puede estar resuelto o descartado silenciosamente). |
| [#1051](https://github.com/openrewrite/rewrite-testing-frameworks/issues/1051) `MockitoWhenOnStaticToMockStatic` falla con `_` (unnamed var) | Medio | Bug reciente (13-jul-2026), reproducible, sin comentarios ni PR. Requiere entender el recipe existente de Mockito static mocking. |
| [#743](https://github.com/openrewrite/rewrite-testing-frameworks/issues/743) `@ParameterizedClass` en JUnit4→5 | Medio–alto | Feature bien definida pero toca el recipe más usado del repo (JUnit4to5Migration); alto escrutinio esperado. |

**No recomendado ahora:** [#772](https://github.com/openrewrite/rewrite-testing-frameworks/issues/772)
("recipe para detectar tests sin @Test") — el maintainer `timtebeek` expresó
reservas explícitas sobre el diseño ("potencial de hacer daño"), discusión de
alcance sin resolver. Mismo patrón que harmonica#353: no entrar hasta que
converja.

## Riesgos

- Sin issue template ni CoC — proyecto funcional pero con menos
  formalización que otros del ecosistema Spring/CNCF.
- El catálogo de `good first issue` es prácticamente inexistente y el único
  disponible es viejo — no hay una rampa de entrada clara, hay que picar
  piedra en bugs reales desde el principio.
- Requiere invertir tiempo en aprender la API de recipes de OpenRewrite antes
  de que el primer PR sea productivo; no es un "fork y copia el patrón" como
  MetPy.
