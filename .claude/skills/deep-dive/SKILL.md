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
  `git clone --depth=1` en el scratchpad (nunca en este repo). Todo clon de un
  repo de terceros se marca al crearlo: `git config ledger.attribution false`
  (regla dura en CLAUDE.md: sin firma de IA en contribuciones externas).
- **Política de IA** (obligatorio): buscar `AI.md`, `AI_POLICY.md`,
  `AGENT_POLICY.md`, `AGENTS.md`, la sección de IA del CONTRIBUTING y el PR
  template (también los del repo `<org>/community` o `<org>/.github`).
  Clasificarla en: **prohíbe** contribuciones hechas por agentes o comunicación
  escrita con IA (descartar el repo o que el usuario lo haga a mano) /
  **exige disclosure** (va en la descripción del PR) / **exige comunicación
  humana** (Claude puede preparar código, pero comments y replies los escribe
  el usuario) / **sin política**.

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
- Riesgos: señales de comunidad hostil, backlog de PRs ignorados, CLA,
  política de IA (con su clasificación), etc.

## Antes de cada publicación (PR, comment, reply)

Las políticas de IA aparecen a mitad de un PR: fatiando adoptó la suya con
tres PRs nuestros abiertos y lucene la suya dos días antes de que abriéramos.
Revisarlo en el deep-dive no basta:

1. Volver a buscar la política de IA del repo y de su organización.
2. Leer **todos** los comments nuevos del hilo, no solo los últimos.
3. Si la política exige disclosure, incluirlo; si prohíbe la comunicación
   escrita con IA, no redactar en la voz del usuario: preparar los hechos y
   que él escriba.
4. Verificar que ningún commit lleve co-autor de IA:
   `git log upstream/<rama>..HEAD --format=%B | grep -i co-authored-by` vacío.
