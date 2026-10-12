# Deep dive: Plane — 2026-10-12

**Veredicto: sí con reservas.** El backend Python/Django encaja con el perfil, pero el setup es pesado y las oportunidades pequeñas revisadas tienen competencia activa. Conviene entrar con un bug reproducible y acotado de API, no empezar una funcionalidad grande sin acuerdo previo.

## Alcance y método

Repositorio: [makeplane/plane](https://github.com/makeplane/plane), rama por defecto `preview`. Evaluación contra `config/interests.yaml`; esta petición explícita amplía la exploración, pero no modifica sus dominios ni repos semilla.

Metadata consultada: 60.697 estrellas, lenguaje principal TypeScript, licencia identificada por GitHub como AGPL-3.0 y último push el 9 de octubre de 2026. Proyecto activo según el umbral de 90 días del perfil. La búsqueda de `good first issue` no aportó entradas; el análisis amplió la revisión a bugs concretos sin asignar.

Datos recogidos mediante GitHub CLI/API el 12 de octubre de 2026. Los issues se comprueban por asignados, conversación y referencias a PRs: «sin asignado» no equivale a «libre». No se ha clonado ni ejecutado Plane, ni publicado comentarios o contribuciones.

## Encaje y barrera técnica

- **Buen encaje:** API Python/Django y contratos REST, pruebas de regresión, despliegues Docker y observabilidad. Son transferibles las contribuciones previas del usuario a Dapr y OpenTelemetry.
- **Encaje secundario:** frontend TypeScript y traducciones. Pueden dar entradas acotadas, pero TypeScript no figura entre los lenguajes preferidos del perfil.
- **Sin especialización sectorial:** es gestión de proyectos horizontal, no geociencias, minería ni procesamiento científico de imágenes. No desplaza por sí solo la prioridad de esos dominios.
- **Coste local alto:** la guía pide Docker, Node.js 20+, PostgreSQL 14, Redis 6.2.7 y recomienda al menos 12 GB de RAM. Python 3.12 y `uv` se necesitan para ejecutar la API fuera de Docker.

## Salud de comunidad: señales y límites

La API de participación devuelve 115 commits en las últimas 12 semanas de su serie; las últimas cuatro suman 44 (15, 11, 15 y 3, con la última semana potencialmente incompleta). El perfil comunitario identifica guía de contribución, código de conducta, licencia y plantilla de PR, con `health_percentage: 100`. Ese indicador mide la presencia documental, no la calidad ni la rapidez de la revisión humana.

La muestra de 20 PRs merged contiene 14 autores con asociación `MEMBER`, 2 `COLLABORATOR` y 4 `CONTRIBUTOR`. Son asociaciones de GitHub, **no prueba de relación laboral ni de contribución externa**. Además, la muestra está ordenada por actualización y contiene incluso un PR de 2023: no representa los últimos 20 merges cronológicos ni permite calcular una tasa de aceptación.

Hay señales concretas de integración activa: [#9950](https://github.com/makeplane/plane/pull/9950), migración de dependencias Python a `uv`, se integró el 7 de octubre; [#9963](https://github.com/makeplane/plane/pull/9963), actualización de imagen MinIO, el 8. Un cambio pequeño de traducción, [#9851](https://github.com/makeplane/plane/pull/9851), se integró en aproximadamente 1 h 43 min el 17 de septiembre. Ese caso no predice el plazo de una contribución nueva.

Los cinco hilos candidatos iniciales no muestran respuestas con asociación `MEMBER` o `COLLABORATOR` en los comentarios recogidos. No hay base suficiente para afirmar una respuesta habitual inferior a 14 días ni para medir un ratio de PRs externos aceptados frente a rechazados. Sí existe competencia visible: varios contribuidores reclaman los mismos bugs y algunos ya tienen PR.

## Oportunidades descartadas para evitar trabajo duplicado

| Issue | Motivo de descarte |
|---|---|
| [#9967: preferencias de inicio de semana sin traducir al español](https://github.com/makeplane/plane/issues/9967) | Reclamado en comentarios y dos PRs abiertos: [#9975](https://github.com/makeplane/plane/pull/9975) y [#9985](https://github.com/makeplane/plane/pull/9985). |
| [#9955: ID de pertenencia ausente en API de miembros](https://github.com/makeplane/plane/issues/9955) | Reclamado y con [#9957](https://github.com/makeplane/plane/pull/9957) abierto. |
| [#9023: reordenar módulos por API/MCP](https://github.com/makeplane/plane/issues/9023) | Reclamado y con [#9958](https://github.com/makeplane/plane/pull/9958) abierto. |
| [#9594: formas inconsistentes del campo `labels`](https://github.com/makeplane/plane/issues/9594) | Dos solicitudes de asignación y un tercer contribuidor indica haber encontrado una implementación pendiente. No está libre aunque no haya asignado. |
| [#8577: separar endpoints de S3 y de lectura](https://github.com/makeplane/plane/issues/8577) | Reclamado; un participante advierte que [#9114](https://github.com/makeplane/plane/pull/9114) ya resuelve el problema. No duplicar sin verificar su alcance. |
| [#9983: evitar peticiones duplicadas y secuenciales del frontend](https://github.com/makeplane/plane/issues/9983) | Con [#9984](https://github.com/makeplane/plane/pull/9984) abierto. |
| [#9970: evitar subir portadas estáticas repetidas a S3](https://github.com/makeplane/plane/issues/9970) | El autor propone hacerse cargo y otra persona lo reclama en comentarios. |
| [#9054: limitar publicación de imágenes de ramas de desarrollo](https://github.com/makeplane/plane/issues/9054) | Reclamado y con [#9959](https://github.com/makeplane/plane/pull/9959) abierto. |
| [#9364: invitados modifican estados de workflow](https://github.com/makeplane/plane/issues/9364) | Un participante informa que ya no reproduce en `preview` por `ProjectEntityPermission`. No es una verificación nuestra; requiere contrastar versión y código antes de proponer trabajo. |
| [#9857: dropdowns sin selección en React 19](https://github.com/makeplane/plane/issues/9857) | Reclamado y con [#9859](https://github.com/makeplane/plane/pull/9859) abierto. |

También se excluyen los issues ya asignados de la muestra, como #9965 (búsqueda de enteros), #9977 (rate limit de Caddy) y #8968 (invitaciones por API).

**Resultado: 0 entradas libres verificadas entre estos diez candidatos.** No se fuerza una lista de 3–5 recomendaciones. Mantener Plane en reserva es preferible a competir con implementaciones abiertas o arreglar un comportamiento que pudiera estar resuelto; esto no significa que no existan oportunidades en el resto del backlog.

## Cómo empezar cuando haya un candidato disponible

1. Volver a comprobar issue, comentarios y PRs equivalentes. Las funcionalidades nuevas requieren propuesta previa según [CONTRIBUTING.md](https://github.com/makeplane/plane/blob/preview/CONTRIBUTING.md).
2. Crear el fork y clonarlo en scratchpad, con fork como `origin` y proyecto como `upstream`. Aplicar `git config ledger.attribution false`; no incluir trailers de coautoría de IA en commits externos.
3. Partir de `upstream/preview`, crear una rama `codex/<cambio>` y seguir la guía: `./setup.sh`, `docker compose -f docker-compose-local.yml up`, `pnpm dev`.
4. Registrar administrador en `http://localhost:3001/god-mode/` y entrar en `http://localhost:3000` con las mismas credenciales.
5. Reproducir antes de editar y añadir specs de regresión: la guía exige pruebas para bugs y funcionalidades. Para API, revisar primero `apps/api`; no se ha validado aquí un entorno local.
6. Ejecutar los checks indicados en `AGENTS.md`: `pnpm check` cubre formato, lint y tipos; `pnpm check:types` verifica tipos de forma específica. Añadir tests según el framework de cada paquete. Para API, el flujo documentado usa `docker compose -f docker-compose-test.yml up --build --abort-on-container-exit --exit-code-from api-tests`, después del setup. La alternativa focalizada es `docker compose -f docker-compose-test.yml run --rm --build api-tests pytest -m unit`.
7. Si se ejecuta API fuera de Docker, usar la versión exacta de `uv` que indique `apps/api/pyproject.toml`, `uv sync` y herramientas vía `uv run`. Dentro de contenedores dev/test, la guía exige `uv sync --inexact` para no desinstalar `pip` del Python del sistema.

## Políticas y riesgos

- **Política de IA: sin política explícita encontrada en los documentos revisados**, no permiso irrestricto. Se leyeron `CONTRIBUTING.md`, [`AGENTS.md`](https://github.com/makeplane/plane/blob/preview/AGENTS.md) y el [PR template](https://github.com/makeplane/plane/blob/preview/.github/pull_request_template.md) del repositorio, además del template organizacional de `makeplane/.github`. La consulta del árbol de `makeplane/community` devolvió HTTP 404: no se obtuvo allí una política pública adicional. No se encontraron exigencias explícitas de CLA o DCO en las fuentes revisadas; no se afirma que no existan otras condiciones o checks.
- La guía requiere reproducción mínima para bugs, pruebas y respeto de los formateadores/linter compartidos (OxLint y oxfmt).
- Revalidar políticas del repositorio y organización antes de cualquier publicación; el análisis no autoriza enviar un PR ni reclamar un issue.
- Las muestras disponibles no demuestran bounties activos ni contratación de contribuidores. No se asigna puntuación extra por esos incentivos.
- No interpretar estrellas o actividad de mantenimiento como garantía de revisión rápida. El principal riesgo observado es duplicar trabajo ya iniciado, además del coste de entorno.
