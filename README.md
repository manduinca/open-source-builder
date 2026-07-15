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
.claude/skills/          # las skills agénticas (/scan-oss, /deep-dive)
reports/                 # reportes Markdown por fecha
dashboard/index.html     # último dashboard generado
```

## Requisitos

- Claude Code
- `gh` (GitHub CLI) autenticado
