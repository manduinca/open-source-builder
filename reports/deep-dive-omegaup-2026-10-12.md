# omegaUp — evaluación para contribuir

Fecha de consulta: 2026-10-12 (America/Lima). Repositorio: [omegaup/omegaup](https://github.com/omegaup/omegaup).

**Veredicto: sí, con reservas.** Hay integración real de aportes externos y revisión constructiva; el impacto educativo latinoamericano es atractivo. La reserva principal es operativa: los arreglos pequeños revisados ya tienen gente trabajando, incluso cuando GitHub los muestra sin asignar. No conviene entrar duplicando esos esfuerzos.

## Encaje con el perfil

La plataforma de educación y concursos de programación amplía el portafolio hacia producto educativo, algoritmos y comunidad regional. No pertenece a los dominios prioritarios de geociencias, minería o procesamiento de imágenes de `config/interests.yaml`. El trabajo visible de esta revisión se concentra en PHP, SQL, TypeScript/Vue y CI, un encaje menos directo que Python, Java, C++, Go o Rust.

Las áreas más razonables para una primera contribución serían una regresión reproducible de backend, un test acotado o una mejora medida de infraestructura. Las propuestas grandes de funciones educativas requieren validación de producto antes de invertir en implementación. No se verificó un programa de bounties ni una ruta concreta a contratación.

## Salud y receptividad

El repositorio tiene **376 estrellas**, lenguaje principal PHP y push registrado el 12 de octubre a las 03:11 UTC (11 de octubre a las 22:11 en Lima). El endpoint de participación devuelve **128 commits en las últimas 12 semanas**, con 13, 7, 11 y 14 en las cuatro últimas posiciones semanales. Su perfil comunitario marca 87 % y detecta README, CONTRIBUTING, código de conducta, licencia y plantilla de PR. Ese porcentaje mide presencia de documentos, no calidad de la comunidad.

La muestra de 20 PRs mergeados, ordenada por última actualización, contiene 18 autores con asociación `CONTRIBUTOR` y dos con `COLLABORATOR`. Entre los 18 primeros, el tiempo desde apertura hasta merge tiene mediana de **10,3 días**, con un rango de **0,47 a 227,5 días**. Ejemplos recientes son [#10281](https://github.com/omegaup/omegaup/pull/10281), [#10290](https://github.com/omegaup/omegaup/pull/10290) y [#10249](https://github.com/omegaup/omegaup/pull/10249).

Esta muestra **no permite calcular una tasa de aceptación**: fue seleccionada entre PRs mergeados, no entre todos los PRs externos cerrados. La asociación de GitHub es una señal de relación con el repositorio, no prueba de empleo o independencia contractual.

En [#9785](https://github.com/omegaup/omegaup/issues/9785), `pabo99` respondió en unos tres días con una distinción técnica concreta entre el contrato del componente y la respuesta de API. En [#10304](https://github.com/omegaup/omegaup/issues/10304), respondió el mismo día pidiendo medidas del beneficio y corrigiendo supuestos desactualizados sobre el gestor de paquetes. Son señales de revisión útil, no de hostilidad. También muestran que describir un cambio plausible no sustituye reproducirlo y probar su beneficio.

## Flujo de contribución

Según [CONTRIBUTING.md](https://github.com/omegaup/omegaup/blob/main/CONTRIBUTING.md):

1. Usar un fork y una rama de trabajo; los PRs apuntan a `main`.
2. Mantener cambios pequeños, enlazar el issue y esperar a tener CI verde antes de solicitar review. Usar Draft PR cuando aún se trabaja en el cambio.
3. Los commits siguen preferentemente prefijos convencionales como `fix:` o `docs:`.
4. El bot `/assign` solo funciona si el autor del issue tiene asociación `OWNER`, `MEMBER` o `COLLABORATOR`; un contribuidor nuevo necesita además al menos un PR previamente mergeado. El máximo es dos asignaciones activas.
5. Un issue sin `assignees` no equivale a trabajo libre: varias solicitudes de asignación fallan por esas reglas, aunque ya exista código preparado.

Para nuestros futuros clones se mantiene la regla local: scratchpad, fork como `origin`, proyecto como `upstream`, `git config ledger.attribution false` y ningún trailer de coautoría de IA. Esta revisión no creó un fork ni publicó comentarios o PRs.

## Setup y calidad exigida

La [guía oficial de entorno](https://github.com/omegaup/omegaup/blob/main/frontend/www/docs/Development-Environment-Setup-Process.md) ofrece una instalación Docker y una ruta local para tests JavaScript/TypeScript:

1. Preparar Docker con Compose 2. Clonar el fork en un scratchpad, como usuario normal, y configurar `upstream` y la atribución antes de trabajar.
2. Inicializar dependencias con `git submodule update --init --recursive`. La falta de submódulos como `pagedown` produce errores de importación en tests.
3. Ejecutar `docker compose pull` y `docker compose up`; la aplicación se sirve en `http://localhost:8001`. Las cuentas de desarrollo están documentadas en la guía. No usar credenciales ni datos de producción.
4. Para tests de frontend fuera del contenedor, usar la versión de `.nvmrc` —la guía actual indica Node 24—, después `corepack enable`, `pnpm install` y `pnpm test`.
5. Validar estilo con `./stuff/lint.sh validate` y ejecutar los tests pertinentes antes de preparar cualquier commit. La guía de PHP exige que todos los tests ejecutados pasen; no es una afirmación de cobertura del 100 %.

Los [Coding guidelines](https://github.com/omegaup/omegaup/blob/main/frontend/www/docs/Coding-guidelines.md) exigen código y comentarios en inglés, tipos en interfaces, pruebas para cambios de comportamiento, Psalm para PHP, TypeScript y mypy para Python. El frontend debe preservar localización, accesibilidad aplicable y modo oscuro; para componentes se recomienda Storybook. El monolito web incluye controladores, DAOs, plantillas Smarty y frontend Vue/TypeScript, y las correcciones de evaluación pueden cruzar hacia el grader Go.

**Barrera de entrada media:** hay documentación útil y entorno integrado, pero Docker, base de datos, submódulos y herramientas de varios lenguajes amplían el arranque. La guía aún menciona Yarn en un prerrequisito pese a que sus comandos actuales usan pnpm; seguir los archivos de versiones y el flujo actual del repositorio, no copiar instrucciones antiguas. No se instaló ni ejecutó este entorno durante la evaluación, por lo que su funcionamiento local no está verificado.

## Política de IA y otros riesgos

**Clasificación: sin política explícita de IA encontrada, al 2026-10-12.** Se revisaron nombres de archivos de política/AGENTS en el árbol, CONTRIBUTING, la plantilla de PR y Coding guidelines; no se encontró prohibición ni requisito de disclosure. Las consultas a `omegaup/.github` y `omegaup/community` devolvieron 404. Esto describe lo consultado y no garantiza ausencia de otras normas; repetir la comprobación del repositorio y de los hilos antes de publicar.

El [LICENSE](https://github.com/omegaup/omegaup/blob/main/LICENSE) contiene el texto de una licencia permisiva de tres condiciones, tipo BSD-3-Clause, con excepciones donde otros archivos indiquen otra licencia. GitHub la clasifica como `NOASSERTION`/`Other`: ese valor no significa que el proyecto carezca de licencia. No se encontró una exigencia de CLA en las guías revisadas; comprobar también los checks al preparar un futuro PR.

La reserva comunitaria más importante es la competencia por issues aparentemente libres. [#10309](https://github.com/omegaup/omegaup/issues/10309) muestra por qué leer el hilo y dependencias previas resulta esencial: otro PR duplicó trabajo pendiente y el contribuidor decidió dar un paso atrás tras aclararlo. No hay razón para repetir ese conflicto.

## Issues revisados y descartados

Estos cinco casos no son recomendaciones de trabajo disponible:

| Issue | Qué se tocaría | Motivo de exclusión |
|---|---|---|
| [#10319 — HTML de páginas de error](https://github.com/omegaup/omegaup/issues/10319) | `frontend/www/{400,404,500,503}.html`, cierre de etiquetas y validación Prettier | `manishpatel00`, autor del issue, pidió asignación el 11 de octubre para abrir su PR. |
| [#10318 — estructura de problem tags](https://github.com/omegaup/omegaup/issues/10318) | `frontend/server/src/Controllers/Problem.php` y tests de entrada JSON | `RAJJADHAV10` ya propone investigar; además reconoce que aún no confirmó una reproducción. |
| [#9785 — tipo Rank generado](https://github.com/omegaup/omegaup/issues/9785) | `Rank.vue`, `api_types.ts`, `user/rank.ts` y tests | `Satyam087` ya implementó y probó una propuesta y mantiene diálogo técnico activo con el mantenedor. |
| [#10273 — límite de usuarios del gráfico](https://github.com/omegaup/omegaup/issues/10273) | `frontend/www/js/omegaup/arena/ranking.ts` y test Jest | `SajalDevX` ya tiene un fix; existe además el [PR abierto #10292](https://github.com/omegaup/omegaup/pull/10292). El mantenedor pide evidencia visual del comportamiento. |
| [#10304 — optimización del CI Cypress](https://github.com/omegaup/omegaup/issues/10304) | `.github/workflows/ci.yml`, validación de artefactos y medición de tiempos | `manishpatel00` tiene implementación y benchmarks en su fork; no tomarlo como oportunidad libre. |

La ampliación a otros siete hilos tampoco produjo una lista de arreglos pequeños libres:

- [#1043 — penalidad por tiempo](https://github.com/omegaup/omegaup/issues/1043), [#1191 — concursos archivados](https://github.com/omegaup/omegaup/issues/1191) y [#1222 — países localizados](https://github.com/omegaup/omegaup/issues/1222): `deepak0x` volvió a reproducirlos y pidió trabajarlos entre el 8 y el 10 de octubre.
- [#10312 — Bootstrap 5](https://github.com/omegaup/omegaup/issues/10312): `manishpatel00` pidió asignación el 10 de octubre.
- [#10309 — plantillas en Ephemeral Grader](https://github.com/omegaup/omegaup/issues/10309): depende del trabajo abierto de `deepak0x`; existe el [PR #10316](https://github.com/omegaup/omegaup/pull/10316) y el hilo ya documenta un conflicto de trabajo duplicado. No entrar.
- [#10130 — lenguajes y estado de resolución](https://github.com/omegaup/omegaup/issues/10130): sin asignación ni trabajo reclamado en el hilo, pero con referencias a [omegajail #61](https://github.com/omegaup/omegajail/pull/61) y [#62](https://github.com/omegaup/omegajail/pull/62), ambos mergeados. No se comprobó si el defecto persiste ni si esos cambios lo resuelven por completo; conservar como diagnóstico pendiente, no como fix listo para tomar.

No se infiere disponibilidad a partir del listado superficial. La revisión de los doce hilos incluyó todos los comentarios y referencias cruzadas devueltos, sin páginas adicionales pendientes.

## Candidato exploratorio: #10322

[#10322 — invalidar caché de ranking al completar una calificación AC](https://github.com/omegaup/omegaup/issues/10322) estaba abierto, sin asignación, sin comentarios y sin referencias cruzadas a PRs al consultar. **No hay evidencia de una reclamación explícita de trabajo, pero tampoco aprobación del diseño**: el autor presenta una propuesta y pide opinión al mantenedor. Coordinar con ambos antes de implementar; no asumir que está disponible solo por carecer de asignación.

- **Esfuerzo estimado: medio-alto**, no un `good first issue` listo para resolver. Implica coordinar el backend PHP con el grader Go, y es más cercano al interés en sistemas/backend que los cambios cosméticos revisados.
- El issue apunta a `frontend/server/src/Controllers/Run.php`, la invalidación en `User.php`, el simulador `frontend/tests/Utils.php` y `quark/cmd/omegaup-grader/frontend_handler.go`. La inspección de `Run.php` confirma la llamada incondicional de invalidación en `apiCreate`; aún no se reprodujo su impacto ni se validó el flujo completo del callback propuesto.
- Antes de quitar la invalidación actual, demostrar el flujo de un envío normal y de un envío de concurso. Verificar la autenticación y el comportamiento al fallar el nuevo callback; un cache obsoleto después de un AC sería una regresión mayor que el ahorro de invalidaciones.
- Tests mínimos propuestos: un envío todavía no calificado no altera el ranking; `AC` normal actualiza la caché; `WA`/`TLE`/`MLE`/`CE` no afectan el conteo de problemas resueltos; los test runs quedan excluidos; rejudge y cambios posteriores de veredicto conservan las garantías previas. Añadir casos de fallo/reintento del callback según el diseño aceptado.
- Las necesidades de un scoreboard de concurso pueden ser distintas del conteo de problemas resueltos. No trasladar automáticamente la regla «solo AC» a todos los caches sin comprobar sus consumidores.

**Recomendación operativa:** no abrir todavía otro PR en omegaUp. Primero confirmar un alcance aceptado para #10322 o reproducir #10130 después de los fixes enlazados. La evidencia no sostiene tres a cinco issues libres y acotados; no se rellena la lista con trabajo ocupado.
