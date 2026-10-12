# Odoo Community y OCA — 2026-10-12

**Veredicto: sí con reservas; OCA tiene el mejor encaje técnico, pero no hay un arreglo pequeño libre validado en esta muestra.** Se interpretó provisionalmente «Odoo Community» en ambos sentidos: el core `odoo/odoo` y la Odoo Community Association. Para OCA se evaluó `OCA/server-tools`, no toda la organización. No se modificó `config/interests.yaml`.

## Encaje y actividad

Python, PostgreSQL, integraciones, auditoría y operaciones encajan bien con el perfil. El valor de negocio es transferible, aunque ERP no sea uno de los dominios prioritarios de geociencias/minería. El core exige aprender ORM, recordsets, seguridad y convenciones de versiones. OCA permite acotar el trabajo a un módulo técnico. No se verificaron bounties ni promesas de contratación.

| Señal al consultar | Odoo core | OCA/server-tools |
|---|---|---|
| Estrellas | 54.977 | 959 |
| Rama por defecto | `20.0` | `19.0` |
| Último push UTC | 2026-10-12 05:55 | 2026-10-11 10:47 |
| Commits en últimos 12 bloques semanales de la API | 3.277 | 39 |
| Últimos cuatro bloques | 342, 199, 156, 91 | 0, 3, 4, 0 |
| Perfil comunitario GitHub | 75 % | 87 % |

Fuentes: [core](https://github.com/odoo/odoo), [OCA](https://github.com/OCA/server-tools), endpoints `community/profile` y `stats/participation` de ambos. Los porcentajes miden documentación detectada, no calidad de revisión. Las ventanas semanales no equivalen a un intervalo exacto de días; la última puede estar incompleta.

Se recogieron 20 PRs mergeados por repositorio ordenados por actualización. Esa muestra puede incluir merges antiguos con actividad reciente y no permite calcular aceptación o velocidad de PRs externos. OCA muestra contribuciones integradas con asociaciones `CONTRIBUTOR` y `NONE`, por ejemplo [#3734](https://github.com/OCA/server-tools/pull/3734) y [#3752](https://github.com/OCA/server-tools/pull/3752); esas etiquetas no determinan empleo ni rol de mantenedor. En [#3360](https://github.com/OCA/server-tools/issues/3360) hubo invitación constructiva a enviar una corrección, pero el trabajo ya tiene PRs.

## Políticas y barreras de publicación

### Core de Odoo

El [LICENSE](https://github.com/odoo/odoo/blob/20.0/LICENSE) declara LGPLv3, con componentes que pueden tener otras licencias. `NOASSERTION` en la API no significa ausencia de licencia.

La [guía oficial](https://github.com/odoo/odoo/wiki/Contributing) exige CLA, cambios mínimos, tests y rama adecuada. Los bugs se envían a una versión estable soportada y se forward-portean; no hay que duplicar el PR en varias ramas. Al consultar, 18.0/19.0/20.0 aceptan bugfixes, 17.0 no, y las funcionalidades nuevas van a `master`. Los PRs tienen prioridad sobre issues; no hace falta crear otro issue antes de enviar un fix. Las traducciones se gestionan fuera de GitHub. El CLA debe revisarlo y aceptarlo el usuario, no el agente.

**IA: sin política explícita encontrada en las fuentes revisadas.** Se inspeccionaron el árbol de archivos de política, CONTRIBUTING, plantilla de PR y wiki; `odoo/.github` y `odoo/community` devolvieron 404. Esto no garantiza ausencia de normas en otros canales. Revalidar antes de publicar.

### OCA

**IA: exige disclosure y supervisión humana; prohíbe agentes sin supervisión.** La [política organizacional](https://github.com/OCA/.github/blob/master/AI_POLICY.md) exige responsabilidad humana, comprensión del código y `Assisted-by:` cuando interviene IA, también indicado en la descripción. No permite atribuir autoría legal a herramientas mediante `Co-Authored-By`. No publicar reviews generadas por IA como si fueran juicio humano. Evitar tandas masivas y esperar reconocimiento antes de añadir aportes. Cualquier publicación futura requiere acordar con el usuario cómo cumplir estas condiciones.

El repositorio declara AGPL-3.0, pero [su README](https://github.com/OCA/server-tools/blob/19.0/README.md) indica revisar la clave `license` del manifest de cada módulo. CONTRIBUTING remite a la guía de OCA; el sitio no pudo recuperarse en esta sesión, por lo que quedan pendientes sus requisitos adicionales, incluido comprobar el CLA aplicable. `OCA/community` devolvió 404; la política sí está en `OCA/.github`.

## Candidatos condicionados, no listos para implementar

1. **[Odoo #292772 — OAuth invalida sesiones previas](https://github.com/odoo/odoo/issues/292772).** Abierto, sin asignar, sin comentarios ni PR cruzado; búsquedas de PRs abiertos por número y por «OAuth sessions» no devolvieron resultados. El autor pregunta si es comportamiento intencional. La inspección de `addons/auth_oauth/models/res_users.py` en 18.0 confirma que el login escribe `oauth_access_token` y que el campo participa en `_get_session_token_fields`. **Esfuerzo medio-alto y riesgo de seguridad:** reproducir en una versión soportada, precisar qué revocaciones deben invalidar sesiones y acordar el comportamiento. No quitar el campo del token de sesión como arreglo automático. Investigar también la alternativa OCA `auth_oauth_multi_token`. La presencia del código no demuestra por sí sola un defecto.
2. **[OCA #3703 — auditlog y comandos relacionales](https://github.com/OCA/server-tools/issues/3703).** Sin asignar ni PR cruzado. El propio autor no pudo producir una reproducción mínima tras múltiples intentos. En `auditlog/models/rule.py` de 18.0, `write_fast` registra deliberadamente el input antes de que el ORM lo transforme, según su comentario. **Esfuerzo alto/incierto:** primero un test que falle y una especificación del formato de auditoría; no asumir que normalizar valores es el comportamiento deseado. Es una investigación, no un quick win.
3. **[OCA #3702 — pérdida de hooks de auditoría](https://github.com/OCA/server-tools/issues/3702).** Buen detalle técnico y reproducción reportada, sin PR cruzado; **no se ofrece como trabajo libre**, porque el autor se ofrece a abrir el PR si aceptan la dirección. Posible colaboración supervisada: reproducir en una versión soportada y aportar evidencia al autor. Áreas propuestas: hooks de `auditlog` y `base_automation`, cadena `.origin` y reconstrucción del registro; esfuerzo alto y tests de interacción entre módulos.

No se presentan tres fixes listos: estas son rutas condicionadas y requieren coordinación o reproducción. Si buscamos un primer merge rápido, no elegiría ninguna de ellas todavía.

## Descartes comprobados

Se leyeron ocho issues del core y doce de OCA con comentarios y referencias cruzadas. Entre los descartes:

| Issue | Trabajo existente o razón para no empezar |
|---|---|
| Odoo #294159, paginación POS | PR [#294162](https://github.com/odoo/odoo/pull/294162) abierto |
| Odoo #293901, webhook Mercado Pago | PR [#293929](https://github.com/odoo/odoo/pull/293929) abierto |
| Odoo #293516, duplicar journals | PR [#293533](https://github.com/odoo/odoo/pull/293533) abierto |
| Odoo #292315, entregas a tiempo | PR [#292334](https://github.com/odoo/odoo/pull/292334) abierto |
| Odoo #293615, compositor de email | PR [#293698](https://github.com/odoo/odoo/pull/293698) abierto |
| Odoo #293047, attachments en DB | PR [#293193](https://github.com/odoo/odoo/pull/293193) abierto |
| Odoo #292722, milestones | PR [#293294](https://github.com/odoo/odoo/pull/293294) abierto |
| OCA #3784, helper que no ejecuta tests | PR [#3741](https://github.com/OCA/server-tools/pull/3741) abierto relacionado; comprobar alcance antes de intervenir |
| OCA #3768, caché de backups | PR [#3786](https://github.com/OCA/server-tools/pull/3786) abierto; comprobar alcance de versiones, no duplicar |
| OCA #3402, emails case-insensitive | PRs [#3610](https://github.com/OCA/server-tools/pull/3610) y [#3657](https://github.com/OCA/server-tools/pull/3657) abiertos |
| OCA #3667, ignorar excepciones bloqueantes | PR [#3679](https://github.com/OCA/server-tools/pull/3679) abierto |
| OCA #3638, cache ORM en auditlog | PR [#3718](https://github.com/OCA/server-tools/pull/3718) abierto |
| OCA #3613, registros archivados | PRs [#3761](https://github.com/OCA/server-tools/pull/3761) y [#3762](https://github.com/OCA/server-tools/pull/3762) abiertos |
| OCA #3360, módulos solo en DB | PRs [#3674](https://github.com/OCA/server-tools/pull/3674) y [#3691](https://github.com/OCA/server-tools/pull/3691) abiertos |
| OCA #3509, firma fetch_mail | Historial de fixes y PR [#3760](https://github.com/OCA/server-tools/pull/3760) abierto en otra versión; requiere aclarar cobertura |
| OCA #3737, métodos auditados en queue_job | El hilo informa una solución propuesta en [OCA/queue #998](https://github.com/OCA/queue/pull/998); no abrir otro fix sin revisar esa interacción |
| OCA #3368, mass edit | El hilo informa solución en [OCA/server-ux #1289](https://github.com/OCA/server-ux/pull/1289); además pertenece a otro repositorio |

## Cómo preparar el entorno cuando haya un alcance aceptado

1. Elegir versión y módulo antes de clonar. Usar scratchpad, fork como `origin`, proyecto como `upstream`, `git config ledger.attribution false` y rama `codex/<cambio>`; no trailers de coautoría IA.
2. Para Odoo 19, la [documentación oficial de instalación desde fuentes](https://github.com/odoo/documentation/blob/19.0/content/administration/on_premise/source.rst) pide Python 3.10+ y PostgreSQL 13+. Preparar base de datos y usuario **de desarrollo**, entorno virtual y dependencias de sistema/Python de esa rama. No conectar una base de producción.
3. Instalar dependencias con `pip install -r requirements.txt` en el entorno virtual. Arranque base: `python3 odoo-bin --addons-path=addons -d oss_dev`. Para OCA, añadir la ruta del checkout OCA de la misma versión a `--addons-path` e instalar solo el módulo elegido y sus dependencias.
4. Escribir una regresión con el framework de Odoo. La [guía de tests](https://github.com/odoo/documentation/blob/19.0/content/developer/reference/backend/testing.rst) documenta `--test-enable` durante instalación/actualización y `--test-tags /nombre_modulo` para seleccionar pruebas. Seguir asimismo el CI/pre-commit de la rama OCA concreta.
5. Validar reproducción, permisos y efectos ORM; no considerar suficiente un test Python aislado cuando el bug depende del registro, cache o transacciones de Odoo.

No se instaló Odoo/OCA ni se ejecutaron sus tests durante esta evaluación. No se abrió un PR, reclamó un issue, firmó un CLA ni publicó un comentario.
