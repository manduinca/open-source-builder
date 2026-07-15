# Deep dive: fatiando/harmonica — 2026-07-14

**Veredicto: SÍ, vale la pena contribuir aquí.** Comunidad pequeña, activa y
diseñada para recibir gente nueva; los 4 `good first issue` están libres y
verificados contra el código actual; sin CLA, sin política restrictiva de IA;
el stack (Python + NumPy + pytest + Numba) calza exacto con el perfil.

## El proyecto

- **Qué es**: procesamiento y modelado de datos de gravimetría y magnetometría
  (métodos potenciales), parte del ecosistema Fatiando a Terra.
- 297 ⭐ · 91 forks · BSD-3-Clause · Python · push 2026-07-13.
- Maintainers activos este trimestre: `santisoler`, `leouieda`, `mdtanker`.
- PRs mergeados de forma continua (varios por mes); merges de mismo día a
  ~2 semanas según tamaño. Contribuidores externos reales mergeados
  recientemente (p. ej. `arthursmacedo`).
- Salud GitHub 75%: CONTRIBUTING ✓, CoC ✓, PR template ✓ (sin issue template).

## Protocolo de contribución (guía org-wide de Fatiando)

1. **No asignan issues formalmente**: la guía pide **comentar en el issue
   contando qué planeas hacer** antes de abrir el PR. Sin burocracia extra.
2. PRs **pequeños y lógicos**; cambios grandes se parten en varios.
3. Sin CLA. Autoría generosa (hasta coautoría en papers para contribuciones
   sustanciales, ver AUTHORSHIP.md).
4. **Sin política sobre IA** en CONTRIBUTING (revisado 2026-07-14): no hay
   nada que declarar ni restricción aplicable.
5. Idioma: inglés.

## Setup de desarrollo (verificado en el clon)

```bash
git clone git@github.com:manduinca/harmonica  # tu fork
cd harmonica
conda env create -f environment.yml   # o pip install -e . + env/requirements-tests.txt
make test        # pytest con y sin JIT de Numba
make format      # ruff
make check       # ruff + burocrata
```

## Issues recomendados (orden sugerido)

### 1. [#293 — Add linearity tests for forward models](https://github.com/fatiando/harmonica/issues/293) · esfuerzo bajo ⭐ EMPEZAR AQUÍ

Tests parametrizados que verifiquen que el campo de N cuerpos = suma de los
campos individuales (linealidad física del modelo directo).
- **Tocar**: `test/test_point_gravity.py`, `test_prism.py`, `test_tesseroid.py`
  — agregar `test_linearity` con `@pytest.mark.parametrize("field", ...)`.
- **Verificado**: hoy no existe ningún test de linealidad en `test/`.
- El propio autor del issue (santisoler, maintainer) ofrece mentoría ("💪").
- Por qué primero: pytest puro, sin decisiones de API, spec incluida en el
  issue, y demuestra rigor — la mejor carta de presentación.

### 2. [#352 — Tesseroid layers en la User Guide](https://github.com/fatiando/harmonica/issues/352) · esfuerzo bajo

Página de guía tipo `user_guide/forward_modelling/prism.rst` pero para capas
de teseroides.
- **Tocar**: crear `doc/user_guide/forward_modelling/tesseroid_layer.rst`
  (hoy solo existe `tesseroid.rst`, sin mención a `tesseroid_layer`) +
  índice.
- Ojo: el código de ejemplos migró recientemente a Bordado (PR "Use Bordado
  in code, tests and docs") — imitar los ejemplos más nuevos, no los viejos.

### 3. [#353 — Corrección topográfica esférica en la User Guide](https://github.com/fatiando/harmonica/issues/353) · esfuerzo bajo

Versión en coordenadas esféricas de `user_guide/topographic_correction.rst`
usando capas de teseroides. Natural hacerlo después de #352 (mismo tema).

### 4. [#37 — Pratt isostasy](https://github.com/fatiando/harmonica/issues/37) · esfuerzo medio

Implementar isostasia de Pratt (variación lateral de densidad dada topografía
y profundidad de compensación).
- **Tocar**: `src/harmonica/_isostasy.py` + `test/test_isostasy.py` + docs.
- **Ojo**: el issue (2018) propone `isostasy_pratt`, pero la API actual se
  renombró a `isostatic_moho_airy`. Pratt devuelve densidad, no Moho —
  proponer nombre (¿`isostatic_density_pratt`?) en el comment antes de
  escribir código. Buen segundo/tercer PR, con física real y visibilidad.

## Riesgos (menores)

- Los 4 issues son de 2018–2022: siguen técnicamente vigentes (verificado),
  pero conviene que el primer comment confirme interés y contexto actual.
- Review "no inmediato y proporcional al tamaño del PR" (dicho en su guía):
  PRs chicos.
- Sin issue template: los reports de bugs son informales.

## Primer paso concreto

Comentar en #293 (en inglés, ~3 líneas): confirmar que quieres tomarlo,
mencionar el approach (una `test_linearity` parametrizada por geometría y
campo) y preguntar si prefieren un solo PR o uno por geometría. Luego fork,
rama `linearity-tests`, y PR pequeño.
