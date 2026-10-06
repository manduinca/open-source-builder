# open-source-builder

Sistema agéntico de descubrimiento y monitoreo de proyectos open source para
contribuir. No es una aplicación: es un repo de configuración + skills
agénticas + reportes generados.

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

## Regla dura: las contribuciones externas no llevan firma de IA

Los commits que van a repos de terceros (todo PR que sale de este sistema)
**nunca** llevan un trailer `Co-Authored-By` de un agente o modelo de IA. Esto
prevalece sobre la atribución por defecto de cualquier agente (Claude Code,
Codex, opencode, Muse Code…). Cuando la política del repo exige declarar el uso
de IA, se declara donde ella indica (descripción del PR, checkbox,
`Assisted-by:`), decidido con el usuario.

- Los clones van al scratchpad, nunca a `~/Projects`, con el fork como `origin`
  y el proyecto como `upstream` (`gh repo fork <owner/repo> --clone`). Apenas
  clonado: `git config ledger.attribution false`.
- [agent-ledger](https://github.com/manduinca/agent-ledger) lo hace cumplir: no
  firma repos de terceros (los reconoce por `upstream` o preguntando a GitHub si
  el `origin` es fork) y su guardia rechaza en `commit-msg` y en `pre-push`
  cualquier co-autor de IA; el `pre-push` mira además el destino, así que también
  cubre un clon del proyecto original que empuja al fork. Si rechaza un commit, se quita el trailer; nunca se
  desactiva la guardia ni se usa `--no-verify` para esquivarla.
- Antes de cada push, `git log upstream/<rama>..HEAD --format=%B | grep -i co-authored-by`
  tiene que salir vacío.
- Única excepción: que la política escrita del proyecto pida ese trailer. Se
  decide con el usuario y se habilita solo en ese clon con
  `git config ledger.allowAiTrailers true`.

Los commits de **este** repo sí llevan el trailer: open-source-builder es propio.

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
