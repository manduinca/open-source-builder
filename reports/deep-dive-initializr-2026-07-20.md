# Deep-dive: spring-io/initializr — 2026-07-20

## Veredicto

**Sí, con reservas.** Comunidad genuinamente sana y de respuesta rápida
(maintainers de Spring, no bots) — mejor de lo que sugiere el dato crudo de
"PRs mergeados". Pero el catálogo de issues abordables está flojo: nada
recién priorizado, sin `good first issue` activos ahora mismo, y los mejores
candidatos necesitan alinear diseño con un maintainer antes de tocar código.

## Salud de comunidad

- **DCO, no CLA** desde enero 2026 (`Signed-off-by` obligatorio en cada
  commit) — fricción mínima comparado con CLA tradicional.
- **Dato engañoso a corregir**: de los últimos ~20 PRs "cerrados sin merge"
  de contribuidores externos en 2026, la mayoría **no son rechazos** — el
  maintainer (mayormente Moritz Halbritter) aplica el cambio por su cuenta y
  cierra con un simple "Thanks @usuario!" (el flujo interno de Spring no
  siempre pasa por el botón "Merge" de GitHub, así que `mergedAt` queda
  `null` aunque el trabajo entró). Solo encontré **un** rechazo real por
  scope (#1770, "Allow annotation processors for tests"), y vino con una
  explicación técnica extensa y respetuosa, no un cierre seco.
- Commits activos cada semana (participation: 1,0,1,3,4,0,1,6,0,0,3,6 en las
  últimas 12 semanas) — equipo trabajando, no en piloto automático.
- eddu (contacto del usuario) logró merge de una feature completa
  (Docker Compose healthcheck) en 4 días — buena señal de tiempo de
  respuesta, aunque no es garantía de trato preferente: no es maintainer
  aquí.

## Barrera de entrada técnica

- Build estándar: `./mvnw clean install` (Maven Wrapper, JDK 8+).
- Convenciones: Spring JavaFormat + Checkstyle (`./mvnw validate`), Javadoc
  con `@author`, header de licencia ASF en archivos nuevos.
- Sin plantillas de issue/PR (`issue_template`/`pr_template` = false en el
  community profile), pero `CONTRIBUTING.adoc` es claro y detallado.
- No hay `good first issue` activo. Existe la label `status:
  first-timers-only` pero está **vacía** ahora mismo — nadie la usó
  recientemente.

## Encaje con el perfil

Java, carril de la red de eddu (contribuyó, no es maintainer). Empresa
Spring/VMware/Broadcom con historial de contratar del ecosistema — coherente
con la ruta de reputación hacia empleo backend que ya persigues en
cloud-native. No es geociencias/minería, es puramente el carril Java.

## Cómo empezar

1. Fork + `./mvnw clean install` para confirmar que el build corre limpio.
2. Configura el signoff DCO: `git commit -s` en cada commit.
3. Empieza por algo de bajo esfuerzo para calibrar el ritmo de review antes
   de comprometerte a algo mayor.

| Issue | Esfuerzo | Nota |
|---|---|---|
| [#1428](https://github.com/spring-io/initializr/issues/1428) — Apply dependency-management plugin consistently to docs | **Bajo** | Solo docs (`.adoc`), inconsistencia ya señalada por un maintainer de Boot. Buen primer PR para probar el ritmo de review. |
| [#1479](https://github.com/spring-io/initializr/issues/1479) — CLI: allow major/minor `bootVersion` | **Medio** | Cambia el parsing de versión + tests. Sin diseño pendiente, alcance claro. |
| [#1742](https://github.com/spring-io/initializr/issues/1742) — Record reasons for JVM version change | **Medio** | Feature nueva sobre `InvalidJvmVersionHelpDocumentCustomizer`; el issue da el archivo de partida. Sin label de diseño pendiente. |
| [#1633](https://github.com/spring-io/initializr/issues/1633) — Support interfaces as `TypeDeclaration` | **Medio-alto** | Tiene `status: pending-design-work` — **hay que discutir el enfoque con un maintainer en el issue antes de codear**, no ir directo a PR. |
| [#1549](https://github.com/spring-io/initializr/issues/1549) — Executable flag on archive entries | **Alto** | Ya hubo un intento cerrado sin merge (#1545, "Fix executable file permissions in archives"). Investigar por qué no prosperó antes de reintentar — puede haber una razón técnica no evidente en el issue. |

## Riesgos

- **Catálogo de issues envejecido**: los abordables van de 2015 a 2026, la
  mayoría sin actividad reciente — nadie los está empujando activamente, así
  que no hay urgencia ni contexto fresco; confirma con un comentario en el
  issue que sigue vigente antes de invertir tiempo.
- **#1633 y similares con `pending-design-work`**: entrar con código
  directo sin alinear diseño es la forma más común de que un PR se quede
  varado. Comenta primero.
- Sin `good first issue` activo ahora mismo — el filtro de entrada de la
  skill (`config/interests.yaml`) no encuentra nada aquí; hay que curar a
  mano como se hizo en este deep-dive.
