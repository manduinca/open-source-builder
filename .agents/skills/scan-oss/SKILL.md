---
name: scan-oss
description: Escanea GitHub con agentes en paralelo para descubrir proyectos open source relevantes (según config/interests.yaml) y curar oportunidades de contribución. Genera reporte Markdown en reports/ y regenera dashboard/index.html. Usar cuando el usuario pida escanear, buscar proyectos OSS o actualizar el reporte/dashboard.
---

# /scan-oss — Escaneo agéntico de proyectos open source

Objetivo: producir un reporte curado de proyectos y de issues abordables para
contribuir, alineado al perfil de `config/interests.yaml`.

## Fase 0 — Preparación (inline, sin agentes)

1. Lee `config/interests.yaml` completo.
2. Verifica `gh auth status` y `gh api rate_limit` (search necesita margen).
3. Fecha del reporte: `date +%Y-%m-%d`.

## Fase 1 — Recolección determinista (inline, comandos gh)

Para cada dominio del YAML:

- **Descubrimiento por keywords** (2–3 keywords por dominio, no todas):
  `gh search repos "<keyword>" --sort=stars --json fullName,description,stargazersCount,pushedAt,language --limit 15`
- **Repos semilla**: `gh api repos/<owner/repo>` para metadata fresca.
- **Issues de contribución** en los repos candidatos más prometedores
  (activos en los últimos `actividad_maxima_dias` días):
  `gh search issues --repo=<owner/repo> --label="good first issue" --state=open --json title,url,createdAt,labels,assignees --limit 20`
  Repite con `help wanted` si hay pocos resultados. Descarta issues asignados.

Guarda los datos crudos en el scratchpad (JSON por dominio). Respeta el rate
limit de search (30 req/min): agrupa y espacia si hace falta.

## Fase 2 — Curación con agentes (Workflow)

Lanza un Workflow con **un agente curador por dominio** (pipeline, no barrier).
Cada agente recibe: el perfil del YAML, los datos crudos de su dominio y la
ruta de los JSON. Su trabajo:

- Evaluar cada repo candidato: ¿vivo? ¿comunidad sana? (`gh api
  repos/X/community/profile`, actividad de PRs externos) ¿relevante al perfil?
- Seleccionar los 5–10 mejores repos y los 3–8 mejores issues del dominio,
  con una línea de justificación y una estimación de esfuerzo
  (bajo/medio/alto) por issue.
- Marcar los `incentivos` del YAML que apliquen a cada repo: bounties
  (buscar el repo en Algora/Polar.sh o labels tipo `💎 Bounty`), historial
  de contratar contribuidores, PR directo sin asignación.
- Devolver salida estructurada (schema JSON): `{repos: [...], issues: [...]}`.

Tras los curadores, un **agente verificador** revisa las URLs de los issues
seleccionados (que existan, sigan abiertos y sin asignar) y elimina falsos
positivos.

## Fase 3 — Síntesis (inline)

1. Escribe `reports/YYYY-MM-DD.md`:
   - Resumen ejecutivo (5 líneas máx).
   - Sección por dominio: tabla de repos destacados (nombre, ⭐, último push,
     por qué importa) y lista de issues curados (título enlazado, labels,
     esfuerzo estimado, por qué es buen punto de entrada).
   - Sección "Novedades vs. escaneo anterior" si existe un reporte previo.
2. Regenera `dashboard/index.html` (carga antes la skill `artifact-design`):
   tarjetas por proyecto agrupadas por dominio, chips de esfuerzo, enlaces
   directos a issues. Tema claro/oscuro. Publícalo como Artifact (mismo
   archivo → misma URL).
3. Commit: `scan: reporte YYYY-MM-DD` (solo si el usuario ya pidió commits
   antes o lo pide ahora).

## Notas

- **Interpola las rutas de datos directamente en los prompts del script del
  Workflow** (template literals con la ruta absoluta ya resuelta). No dependas
  de `args` para pasar rutas: si llega mal serializado, los agentes reciben
  `undefined` y curan a ciegas (bug observado en el primer escaneo).
- Minería es nicho: la búsqueda por keywords trae ruido (F1 "pit stop",
  tareas de curso). Busca por `--topic=mining-engineering`, `geostatistics`,
  `mineral-exploration` y verifica repos del ecosistema conocido
  (Loop3D, cgre-aachen, opengeostat, Software Underground). Acepta repos
  pequeños (~20★) si están vivos.

- No inventes repos ni issues: todo dato del reporte debe venir de la Fase 1
  o de verificación directa con `gh`.
- Si un dominio no arroja resultados nuevos, dilo explícitamente en el
  reporte en lugar de rellenar con resultados débiles.
