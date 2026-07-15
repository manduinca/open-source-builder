---
name: deep-dive
description: Análisis profundo de un repositorio open source concreto (owner/repo) para decidir si conviene contribuir y por dónde empezar. Usar cuando el usuario pida analizar, evaluar o "hacer deep dive" a un repo específico.
---

# /deep-dive <owner/repo> — Análisis de un repo para contribuir

Si no se pasó un repo como argumento, pregunta cuál antes de continuar.

## Recolección (inline, gh)

- `gh api repos/<owner/repo>` — stars, lenguaje, licencia, pushed_at, forks.
- `gh api repos/<owner/repo>/community/profile` — CONTRIBUTING, CoC, templates.
- `gh api repos/<owner/repo>/stats/participation` — actividad de commits.
- PRs recientes de externos: `gh pr list --repo <owner/repo> --state merged --limit 20 --json author,mergedAt,title` — ¿mergean PRs de no-mantenedores? ¿en cuánto tiempo?
- Issues abiertos con labels de contribución (ver `config/interests.yaml`),
  descartando asignados o con PR enlazado.
- Clona shallow si hace falta inspeccionar el código:
  `git clone --depth=1` en el scratchpad (nunca en este repo).

## Análisis (agentes en paralelo si el repo es grande)

1. **Salud de comunidad**: velocidad de respuesta en issues, tono de los
   mantenedores, ratio de PRs externos mergeados vs. cerrados sin merge.
2. **Barrera de entrada técnica**: setup de desarrollo (¿hay guía?, ¿tests
   corren fácil?), arquitectura general, calidad de los good-first-issues.
3. **Encaje con el perfil**: relevancia para los dominios de
   `config/interests.yaml` y para el stack del usuario.

## Salida

Informe en `reports/deep-dive-<repo>-YYYY-MM-DD.md`:

- Veredicto en una línea: ¿vale la pena contribuir aquí? (sí / sí con
  reservas / no, y por qué).
- Cómo empezar: pasos concretos de setup + 3–5 issues recomendados ordenados
  por esfuerzo, cada uno con una nota de qué tocar en el código.
- Riesgos: señales de comunidad hostil, backlog de PRs ignorados, CLA, etc.
