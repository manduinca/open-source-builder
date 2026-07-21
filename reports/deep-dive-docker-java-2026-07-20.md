# Deep dive — docker-java/docker-java (2026-07-20)

## Veredicto

**Sí, con reservas.** El repo está vivo (push hace 7 días, 3190★, licencia
Apache-2.0, `CONTRIBUTING.md` presente) y sí mergea PRs externos, pero la
capacidad de revisión humana es delgada: de los últimos 25 merges, 19 son
`dependabot` y 19 (de un total de ~40 merges no-bot en el historial visible)
son del propio **eddumelendez**, quien de facto actúa como maintainer aquí
aunque no lo sea oficialmente. `stats/participation` marca solo 1 semana con
commits humanos de las últimas 12. Hay una **cola visible de PRs externos
esperando review** (ver riesgos) — entrar aquí es plausible pero no rápido.

## Salud de comunidad

- `CONTRIBUTING.md`: sí. `CODE_OF_CONDUCT`: no. Health score de GitHub: 50%.
- Autores con PR merged (últimos 100 merges): `dependabot` (61),
  **eddumelendez (19)**, y ~15 contribuidores externos con 1 merge cada uno
  (LarsSven, mwiede, ok2c, henri-tremblay, etc.) — sí aceptan gente nueva,
  pero de forma esporádica, no como flujo constante.
- **Riesgo concreto**: issue #2625 (mayo 2026) tiene PR #2626 abierto desde
  entonces, sin review. El autor tuvo que **ping directo a eddumelendez**
  pidiendo atención ("not sure if this issue and associated PR have caught
  the attention of docker-java maintainers or if it was lost in the noise").
  Mismo patrón en #2547 (PR #2630 sin mergear) y #2555 (PR #2556 sin
  mergear). Conclusión: **abrir PR no es el cuello de botella — conseguir
  review sí lo es.**

## Barrera de entrada técnica

- Maven multi-módulo estándar (`docker-java-transport-*` + core). Setup
  normal: `mvn -pl <módulo> -am test`. Sin guía de dev-environment más allá
  del CONTRIBUTING genérico.
- Arquitectura por transportes intercambiables (netty, jersey, okhttp,
  httpclient5, zerodep) — entender cuál módulo tocar requiere leer el
  issue con cuidado antes de codear.

## Verificación de #2651 (candidato original) — DESCARTADO

**No es un issue de código.** Investigué el módulo `docker-java-transport-zerodep`
(maven-shade-plugin, `createDependencyReducedPom`) y el pom de
`docker-java-transport-httpclient5`: **el `main` actual ya pinea
`httpclient5:5.5.1`** (que arrastra una versión de HttpCore5 no afectada por
las CVE-2026-54399/54428 reportadas). El JAR shaded vulnerable es el de la
**última release publicada, 3.7.1 (2026-03-18)** — construida antes del bump.
No hay línea que cambiar: se resuelve **cortando una nueva release**, algo
que solo puede hacer un maintainer. Cero comentarios en el issue porque no
hay nada que un contribuidor externo pueda hacer ahí. Descartar.

## Cómo empezar — issues recomendados (verificados: abiertos, sin asignar, sin PR enlazado)

| # | Issue | Esfuerzo | Nota |
|---|---|---|---|
| [#2617](https://github.com/docker-java/docker-java/issues/2617) | Support for Jackson 3 | Medio-alto | Sin comentarios, sin PR. Migración de Jackson 2→3 toca serialización en varios módulos; requiere entender bien el uso de Jackson en el core antes de tocar. Buen "segundo PR" si el primero sale bien, no punto de entrada. |
| [#2651](https://github.com/docker-java/docker-java/issues/2651) | HttpCore5 vulnerable embebido | — | **Descartado**: no es código, requiere release del maintainer. |

No encontré un issue de esfuerzo bajo, abierto, sin PR enlazado y sin
ambigüedad de diseño. Los "fáciles" recientes (#2625, #2547, #2555) ya
tienen PR de otra persona atascado esperando review — sumarse ahí no ayuda.

## Riesgos

1. **Cuello de botella de review**, no de aceptación: varios PRs externos
   llevan meses sin mergear pese a tener solución lista. Antes de invertir
   tiempo en un PR, hay que aceptar que puede quedar en cola indefinidamente
   — mismo patrón que ya viviste en fCC#68837, pero aquí sin competencia,
   solo sin bandwidth de review.
2. Sin CODE_OF_CONDUCT — no es señal de hostilidad, pero sí de proyecto
   con gobernanza informal.
3. eddu concentra casi toda la revisión humana real — si él está ocupado
   en testcontainers-java/shell-plugins (como está ahora), este repo puede
   quedar aún más lento.

**Recomendación práctica**: si se contribuye aquí, hacerlo sabiendo que el
retorno (review, merge) puede tardar meses, no días. No es el mejor uso del
tiempo comparado con MetPy/Fatiando, donde ya hay tracción y menos backlog.
