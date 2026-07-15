# open-source-builder

Sistema agéntico de descubrimiento y monitoreo de proyectos open source para
contribuir. No es una aplicación: es un repo de configuración + skills de
Claude Code + reportes generados.

## Principios

- `config/interests.yaml` es la única fuente de verdad sobre qué buscar.
  Léelo siempre antes de escanear. Nunca hardcodees dominios o repos en
  las skills.
- La recolección de datos es **determinista** (comandos `gh api` / `gh search`);
  los agentes se usan solo para **evaluar, curar y sintetizar**. No gastes
  agentes en lo que un comando resuelve.
- Los reportes van en `reports/YYYY-MM-DD.md`. Nunca sobrescribas reportes de
  fechas anteriores. El dashboard `dashboard/index.html` sí se regenera
  completo en cada escaneo.
- Idioma de reportes y dashboard: español. Términos técnicos y nombres de
  labels de GitHub (`good first issue`, etc.) quedan en inglés.

## Comandos útiles

- `gh search repos "<keyword>" --language=python --sort=stars --json fullName,stargazersCount,pushedAt,description --limit 20`
- `gh search issues --label="good first issue" --repo=<owner/repo> --state=open --json title,url,createdAt,labels --limit 30`
- `gh api repos/<owner/repo>` — metadata completa (pushed_at, open_issues, license)
- `gh api repos/<owner/repo>/community/profile` — salud: CONTRIBUTING, CoC, etc.

Cuidado con rate limits: `gh api rate_limit`. La search API tiene límite
propio (30 req/min); agrupa búsquedas y usa `--limit` moderados.

## Criterios de curación (resumen; detalle en interests.yaml)

Un issue es una buena oportunidad si: el repo tuvo push reciente, el issue
está abierto y sin asignar, no tiene un PR enlazado ya abierto, y los
mantenedores responden issues. Prioriza issues con contexto claro sobre los
vagos, y dominios de nicho (geociencias/minería) sobre los genéricos.
