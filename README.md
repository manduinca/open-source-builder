# open-source-builder

Sistema agéntico para descubrir y monitorear proyectos open source relevantes
para Deep Skill y para manduinca: geociencias, minería, procesamiento de
imágenes y librerías base (Python, Java, Go, Rust).

## ¿Qué hace?

Agentes de Claude Code que:

1. **Descubren** repositorios activos en los dominios de interés (búsqueda en
   GitHub por keywords + repos semilla en `config/interests.yaml`).
2. **Curán** oportunidades de contribución: issues `good first issue` /
   `help wanted` en proyectos con comunidades sanas.
3. **Reportan** los hallazgos en `reports/` (Markdown versionado) y en un
   dashboard HTML (`dashboard/index.html`, publicable como Artifact).

## Uso

Dentro de Claude Code, en este directorio:

- `/scan-oss` — escaneo completo: descubre, cura y genera reporte + dashboard.
- `/deep-dive <owner/repo>` — análisis profundo de un repo: salud de la
  comunidad, guía de contribución, issues abordables ordenados por
  esfuerzo/impacto.

## Configuración

Todo el perfil de intereses vive en `config/interests.yaml`: dominios,
keywords, repos semilla, lenguajes preferidos y criterios de curación.
Edítalo y vuelve a correr `/scan-oss`.

## Estructura

```
config/interests.yaml    # qué buscar y cómo priorizar
CLAUDE.md                # instrucciones del repo para Claude Code
.claude/skills/          # las skills agénticas (/scan-oss, /deep-dive)
AGENTS.md                # espejo de CLAUDE.md para Codex
.agents/skills/          # espejo de .claude/skills/ para Codex
APRENDIZAJES.md          # lecciones operativas acumuladas
reports/                 # reportes Markdown por fecha
dashboard/index.html     # último dashboard generado
```

### El espejo para Codex

El proyecto se trabaja indistintamente desde Claude Code y desde Codex, que
lee `AGENTS.md` y `.agents/skills/` en vez de `CLAUDE.md` y `.claude/skills/`.
Son **copias**, no enlaces: `.agents/skills/*/SKILL.md` es byte a byte igual a
su gemelo, y `AGENTS.md` sólo cambia la línea que nombra al agente. Al tocar
una skill o las instrucciones del repo, copiar el cambio al espejo en el mismo
commit; si divergen, manda la versión de `.claude/`.

## Reportes

Dos tipos, ambos en `reports/` y ninguno se sobrescribe:

- `YYYY-MM-DD.md` — lo contribuido ese día (PRs abiertos, reviews atendidas,
  merges) con la evidencia de validación de cada uno.
- `YYYY-MM-DD-scan.md` — un escaneo de oportunidades: qué se buscó, con qué
  método y qué issues quedaron verificados como libres.

## Requisitos

- Claude Code o Codex
- `gh` (GitHub CLI) autenticado
