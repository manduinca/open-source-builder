# Deep dive: lichess-org/lila — 2026-10-12

**Actualización posterior del mismo día:** se publicó el [draft #22064](https://github.com/lichess-org/lila/pull/22064) para #21960. El cambio de atributos de enlaces compila y pasa Scalafmt; revisión, reproducción y pruebas humanas siguen pendientes. El análisis que sigue conserva el estado anterior a la implementación; evidencia y seguimiento actuales en [2026-10-12.md](2026-10-12.md#lichess-21960-draft-publicado).

**Veredicto: sí, con reservas.** Lichess tiene actividad y respuestas constructivas, pero su backend Scala y el coste de levantar y probar la aplicación elevan la barrera frente a nuestros proyectos Python/Java. La primera entrada recomendada es [#21960: descubrimiento de feeds Atom](https://github.com/lichess-org/lila/issues/21960), siempre que podamos dedicar una sesión humana a reproducir y verificar el cambio.

## Encaje y alcance

Se evaluó `lichess-org/lila`, aplicación web de Lichess; no todos los repositorios de su organización. El perfil de `config/interests.yaml` prioriza geociencias/minería, imágenes, Python, Java, C++, Go y Rust. El ajedrez y Scala no son un encaje directo: aquí pesa el interés explícito del usuario en Lichess y la oportunidad de aprender una aplicación de producción sobre la JVM. No se verificaron bounties ni una vía de empleo vinculada a estos issues.

La información procede de una recolección determinista de GitHub del 12 de octubre de 2026: 25 issues abiertos recientes, una muestra de 20 PRs mergeados y lectura completa de seis hilos candidatos, con sus referencias cruzadas. No es un censo de todos los issues ni una medición de todas las contribuciones externas.

El [repositorio](https://github.com/lichess-org/lila) registra **18.821 estrellas**, lenguaje principal **Scala**, licencia **AGPL-3.0** y último push el **11 de octubre de 2026 a las 23:25 de Lima** (12 de octubre a las 04:25 UTC).

## Salud y respuesta de la comunidad

- El [perfil de comunidad de GitHub](https://api.github.com/repos/lichess-org/lila/community/profile) marca **87 %** de cobertura: hay README, licencia, CONTRIBUTING, plantilla de PR y [código de conducta de la organización](https://github.com/lichess-org/.github/blob/main/CODE_OF_CONDUCT.md). Esa puntuación mide archivos y prácticas detectables, no la calidad del trato ni una probabilidad de merge.
- La [API de participación](https://api.github.com/repos/lichess-org/lila/stats/participation) devuelve 52 bloques semanales. Los últimos 12 suman **2.967 commits**; los últimos cuatro registran **185, 167, 287 y 232**, respectivamente. Son ventanas semanales de la API, no una delimitación de días exactos ni un conteo de PRs externos.
- Hay merges recientes, incluidos [#22052](https://github.com/lichess-org/lila/pull/22052) y [#22044](https://github.com/lichess-org/lila/pull/22044), del 11 de octubre.
- En la muestra de 20 PRs mergeados hay 19 de autores humanos —9 autores distintos— y uno de `github-actions`. La mediana entre apertura y merge de los 19 humanos es **10,8 horas**. Esta cifra está condicionada a PRs ya aceptados y a la selección de la muestra: **no predice** el tiempo de nuestro primer PR ni mide cuánto esperan los abiertos.
- Doce PRs humanos de esa muestra muestran `authorAssociation=CONTRIBUTOR`, seis `MEMBER` y uno `COLLABORATOR`. Estas etiquetas indican relación con GitHub, **no permiten distinguir empleados, mantenedores o contribuidores externos**. No se calcula una tasa de aceptación externa con estos datos.
- En [#21960](https://github.com/lichess-org/lila/issues/21960), una persona con asociación `COLLABORATOR` respondió a la propuesta de un interesado en unos 6 minutos y a una pregunta de setup en unos 30 minutos. El tono fue constructivo, con orientación hacia `lila-docker` y el canal de onboarding. Es una buena señal concreta, no un SLA general.
- Los issues etiquetados como entrada pueden estar ocupados o desactualizados: [#22005](https://github.com/lichess-org/lila/issues/22005) ya tiene PR y [#12926](https://github.com/lichess-org/lila/issues/12926) ya no parece describir correctamente el área restante por arreglar.

## Barrera técnica y cómo empezar

La aplicación combina Scala 3.8.2, Liplay 3.2, MongoDB, Redis y frontend TypeScript. La guía del repositorio indica Java 21, Node 24.20+ y pnpm 12.9.0. Verificar nuevamente estas versiones al comenzar: son el estado observado, no requisitos congelados. Fuentes: [AGENTS.md](https://github.com/lichess-org/lila/blob/master/AGENTS.md), [onboarding](https://github.com/lichess-org/lila/wiki/Lichess-Development-Onboarding) y [lila-docker](https://github.com/lichess-org/lila-docker).

1. Crear el fork y clonarlo en el scratchpad, con el fork como `origin` y `lichess-org/lila` como `upstream`; establecer inmediatamente `git config ledger.attribution false`.
2. Seguir el onboarding oficial y disponer de los servicios requeridos. Evaluar `lila-docker` si resulta más sencillo; no asumir que elimina el coste de recursos. En #21960 el interesado se retiró precisamente por no poder ejecutar el entorno en su portátil.
3. Instalar dependencias con `pnpm install`, construir el frontend con `./ui/build` y arrancar con `./lila.sh` según la configuración del onboarding.
4. Reproducir personalmente el caso antes de modificarlo. Las entradas de tests documentadas son `pnpm test` y `./lila.sh test`; después, ejecutar las pruebas del área afectada y una verificación manual del flujo real.
5. Conservar evidencia humana —capturas o vídeo— y preparar una explicación propia del cambio. No se ha levantado el entorno ni ejecutado tests durante este análisis.

## Oportunidades: una validada y una condicional

### 1. #21960 — Hacer descubribles los feeds Atom de blogs

[Issue y conversación](https://github.com/lichess-org/lila/issues/21960). Abierto, sin asignar y sin PR abierto en las referencias cruzadas revisadas. Las búsquedas adicionales de PRs abiertos por `21960` y `Atom feeds` tampoco devolvieron resultados; no descartan trabajo aún no publicado. Tiene labels `good first issue`, `scala` y `SEO`. El interesado previo se retiró explícitamente el **7 de octubre**; no se interpreta su mensaje inicial como una reserva vigente.

**Esfuerzo estimado:** bajo en código, medio/alto de entrada por setup y prueba humana. Es una estimación, no una duración comprometida.

**Qué tocar, contrastado con el código:** [`UblogUi.scala`](https://github.com/lichess-org/lila/blob/master/modules/ublog/src/main/ui/UblogUi.scala) en `blogPage` y `community`, y [`UblogPostUi.scala`](https://github.com/lichess-org/lila/blob/master/modules/ublog/src/main/ui/UblogPostUi.scala). Las tres vistas **ya construyen enlaces** mediante `atomLinkTag`, incluidos los títulos traducidos donde corresponde, pero les faltan `type="application/atom+xml"` y `rel="alternate"`. [`app/views/base/page.scala`](https://github.com/lichess-org/lila/blob/master/app/views/base/page.scala) inserta el tag tal cual (`p.atomLinkTag | dailyNewsAtom`), sin completar esos atributos. El alcance inicial sería añadir los atributos a los enlaces existentes, no crear enlaces duplicados. Se inspeccionó el código mediante API; falta verificar el HTML renderizado y realizar la prueba humana exigida.

**Delimitar el primer PR:** la conversación acepta separar el tratamiento de `X-Robots-Tag: noindex`. Empezar por enlaces y descubrimiento; revisar los cambios de idioma relacionados con #21961 antes de implementar. Validar tanto portada como entrada individual, blogs en diferentes idiomas y la página comunitaria. No añadir funcionalidad editorial ni cambiar reglas de indexación incidentalmente.

**Antes de empezar:** revalidar si apareció un PR y coordinar el alcance en caso necesario. No se ha publicado ningún comentario de reserva.

### 2. #22051 — Toggle local de chat cuando hay otras pestañas (condicional)

[Issue y conversación](https://github.com/lichess-org/lila/issues/22051). Abierto, sin asignar, con label `no scala` y sin PR enlazado detectado. El reporte delimita una preferencia local: ocultar mensajes y entrada, conservar acceso a Notes y otras pestañas, persistir la elección y permitir teclado/móvil.

**Esfuerzo estimado:** medio, por interacciones de selección de pestaña y accesibilidad. Las áreas concretas señaladas por el reporte son [`chatCtrl.ts`](https://github.com/lichess-org/lila/blob/master/ui/lib/src/chat/chatCtrl.ts), [`renderChat.ts`](https://github.com/lichess-org/lila/blob/master/ui/lib/src/chat/renderChat.ts) y [`discussion.ts`](https://github.com/lichess-org/lila/blob/master/ui/lib/src/chat/discussion.ts): `chatEnabled`, `ctrl.isOptional` y `ChatCtrl.getTab()`.

**Condición antes de invertir:** la única respuesta, de una persona con asociación `MEMBER`, considera que la propuesta técnicamente revierte el sistema de chat anterior. No hay aprobación del cambio de producto. Primero aclarar si aceptan exponer el control conservando el diseño nuevo; no interpretar `no scala` como aceptación del alcance. Solo después reproducir los flujos y diseñar la solución. Por esa incertidumbre, **no es todavía un issue listo para implementar**.

No se completa artificialmente una lista de 3–5 recomendaciones: las siguientes opciones revisadas están ocupadas o necesitan redefinición.

## Descartes y reservas

| Issue | Decisión y evidencia |
|---|---|
| [#22005 — SoftwareApp structured data](https://github.com/lichess-org/lila/issues/22005) | No duplicar: existe [PR #22006 abierto](https://github.com/lichess-org/lila/pull/22006). |
| [#14116 — Racing Kings practice color](https://github.com/lichess-org/lila/issues/14116) | No duplicar: existe [PR #20864 abierto](https://github.com/lichess-org/lila/pull/20864), además de múltiples intentos cerrados. No es una entrada limpia aunque conserve aspecto de bug pequeño. |
| [#22042 — Glifos borrosos al borde del tablero](https://github.com/lichess-org/lila/issues/22042) | No duplicar: el hilo enlaza [chessground #410 abierto](https://github.com/lichess-org/chessground/pull/410). Además, hay restricciones de capas y visualización; no es simplemente cambiar un `z-index`. |
| [#12926 — Enroque 960 en editor](https://github.com/lichess-org/lila/issues/12926) | No empezar por el título: comentarios de enero y agosto de 2026 indican que el editor ya restringe esos derechos. El resto se reproduce por acceso directo al análisis y apunta a `scalachess`; requiere redefinir alcance y confirmar comportamiento esperado. |

## Política de IA y requisitos de publicación

**Clasificación: exige disclosure y responsabilidad/revisión humana de código y comunicación; no es una prohibición total de asistencia con IA.** Fuentes: [AI_POLICY.md](https://github.com/lichess-org/lila/blob/master/AI_POLICY.md) y [CONTRIBUTING.md](https://github.com/lichess-org/lila/blob/master/CONTRIBUTING.md).

La comprobación organizacional de `lichess-org/community` devolvió HTTP 404; [lichess-org/.github](https://github.com/lichess-org/.github) contiene el código de conducta y el perfil, sin otra política de IA detectada en esa inspección. No se interpreta el 404 como garantía de inexistencia de normas en otros canales.

La política exige declarar el uso de IA, entender y revisar el resultado, y revisar/editar humanamente la comunicación. Para código, `CONTRIBUTING` exige reproducir el bug personalmente, ejecutar y probar el cambio y aportar evidencia de pruebas humanas, preferentemente vídeo. También pide indicar la herramienta y los prompts usados en el mensaje del PR o en los commits. Un PR no probado debe permanecer como draft.

Antes de publicar, el usuario debe decidir y validar el disclosure y realizar las comprobaciones humanas exigidas. Esta evaluación no autoriza al agente a presentar pruebas automáticas como pruebas humanas. La regla de este sistema de **no añadir `Co-Authored-By` de IA a commits externos** sigue vigente: el disclosure puede ir en la descripción del PR; no es necesario añadir ese trailer.

No se verificó un requisito de CLA separado en los materiales revisados; comprobar las plantillas y políticas vigentes antes de enviar una contribución. No se han enviado comentarios, PRs, commits ni pushes.
