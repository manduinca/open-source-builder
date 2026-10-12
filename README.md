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
CLAUDE.md                # instrucciones del repo
.claude/skills/          # las skills agénticas (/scan-oss, /deep-dive)
AGENTS.md -> CLAUDE.md   # lo mismo, donde Codex lo busca
.agents/skills/ -> ...   # symlink a .claude/skills/
APRENDIZAJES.md          # lecciones operativas acumuladas
reports/                 # reportes Markdown por fecha
dashboard/index.html     # último dashboard generado
```

### El espejo para Codex

El proyecto se trabaja indistintamente desde Claude Code y desde Codex, que
lee `AGENTS.md` y `.agents/skills/` en vez de `CLAUDE.md` y `.claude/skills/`.
Ambos son symlinks versionados a su gemelo, así que no hay nada que
sincronizar: una skill nueva en `.claude/skills/` aparece sola del otro lado.
Por eso `CLAUDE.md` no nombra al agente que lo lee.

## Reportes

Dos tipos, ambos en `reports/` y ninguno se sobrescribe:

- `YYYY-MM-DD.md` — lo contribuido ese día (PRs abiertos, reviews atendidas,
  merges) con la evidencia de validación de cada uno.
- `YYYY-MM-DD-scan.md` — un escaneo de oportunidades: qué se buscó, con qué
  método y qué issues quedaron verificados como libres.

## Requisitos

- Claude Code o Codex
- `gh` (GitHub CLI) autenticado

## Repositorios de seguimiento habitual

Cartera de **36 repositorios**, definida en `seguimiento_habitual` de
`config/interests.yaml`: 31 con contribuciones previas y cinco incorporaciones
solicitadas el 12 de octubre de 2026 (Lichess, omegaUp, Odoo, OCA y Plane).
Además se conservan otras semillas para descubrir oportunidades. Los repos de
cursos y comunidad antiguos figuran por separado como históricos.

| Tipo | Repositorios |
| --- | --- |
| Geociencias y meteorología | [gempy-project/gempy](https://github.com/gempy-project/gempy), [fatiando/harmonica](https://github.com/fatiando/harmonica), [fatiando/boule](https://github.com/fatiando/boule), [simpeg/simpeg](https://github.com/simpeg/simpeg), [Loop3D/LoopStructural](https://github.com/Loop3D/LoopStructural), [DASDAE/dascore](https://github.com/DASDAE/dascore), [seisbench/seisbench](https://github.com/seisbench/seisbench), [GlacioHack/xdem](https://github.com/GlacioHack/xdem), [Unidata/MetPy](https://github.com/Unidata/MetPy) |
| Geoespacial y machine learning | [torchgeo/torchgeo](https://github.com/torchgeo/torchgeo) |
| Cloud-native y testing | [dapr/python-sdk](https://github.com/dapr/python-sdk), [dapr/java-sdk](https://github.com/dapr/java-sdk), [testcontainers/testcontainers-java](https://github.com/testcontainers/testcontainers-java), [testcontainers/testcontainers-go](https://github.com/testcontainers/testcontainers-go), [cloudevents/sdk-python](https://github.com/cloudevents/sdk-python) |
| Observabilidad, seguridad y operaciones | [open-telemetry/opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib), [prometheus/client_java](https://github.com/prometheus/client_java), [czerwonk/ping_exporter](https://github.com/czerwonk/ping_exporter), [falcosecurity/falcosidekick](https://github.com/falcosecurity/falcosidekick), [moghtech/komodo](https://github.com/moghtech/komodo) |
| Herramientas y backend Java | [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot), [openrewrite/rewrite-testing-frameworks](https://github.com/openrewrite/rewrite-testing-frameworks), [OpenAPITools/openapi-generator](https://github.com/OpenAPITools/openapi-generator), [keycloak/keycloak](https://github.com/keycloak/keycloak), [apache/lucene](https://github.com/apache/lucene) |
| Desktop, lenguaje e IA | [wailsapp/wails](https://github.com/wailsapp/wails), [Automattic/harper](https://github.com/Automattic/harper), [Lightning-AI/litgpt](https://github.com/Lightning-AI/litgpt) |
| Documentación de infraestructura | [kubernetes/website](https://github.com/kubernetes/website), [open-telemetry/opentelemetry.io](https://github.com/open-telemetry/opentelemetry.io) |
| Aplicaciones de comunidad, ERP y gestión | [lichess-org/lila](https://github.com/lichess-org/lila), [omegaup/omegaup](https://github.com/omegaup/omegaup), [odoo/odoo](https://github.com/odoo/odoo), [OCA/server-tools](https://github.com/OCA/server-tools), [makeplane/plane](https://github.com/makeplane/plane) |
| Educación de programación | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) |

El seguimiento incluye repos cuya política limita o prohíbe asistencia con IA:
observar actividad no autoriza a enviarles contribuciones. Los límites conocidos
se registran en `restricciones_contribucion` y se revalidan antes de publicar.
