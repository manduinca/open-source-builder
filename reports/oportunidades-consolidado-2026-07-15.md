# Oportunidades consolidadas — 2026-07-15

Issues verificados hoy (abiertos y sin asignar). Esfuerzo = estimación.

## A. Foco: geociencias (sin competencia, terreno estratégico)

| Repo | Issue | Qué es | Esfuerzo | Encaje |
|---|---|---|---|---|
| fatiando/harmonica | [#293](https://github.com/fatiando/harmonica/issues/293) | Tests de linealidad de forward models | bajo | **Ya es tuyo** — comment puesto, esperando a santisoler |
| fatiando/harmonica | [#352](https://github.com/fatiando/harmonica/issues/352) | Guía de tesseroid layers | bajo | Docs; buen segundo PR |
| fatiando/harmonica | [#353](https://github.com/fatiando/harmonica/issues/353) | Corrección topográfica esférica (guía) | bajo | Natural tras #352 |
| fatiando/harmonica | [#37](https://github.com/fatiando/harmonica/issues/37) | Isostasia de Pratt | medio | Física real (prestigio) |
| GenericMappingTools/pygmt | [#1352](https://github.com/GenericMappingTools/pygmt/issues/1352) | Ejemplo blockmean/blockmedian + surface | bajo | Gridding = geoestadística; maintainers guían |
| GenericMappingTools/pygmt | [#1370](https://github.com/GenericMappingTools/pygmt/issues/1370) | Ampliar docs de `subplot` (figsize) | bajo | Entrada limpia |
| GenericMappingTools/pygmt | [#1393](https://github.com/GenericMappingTools/pygmt/issues/1393) | Plotear texto 3D a distintas alturas | medio | API de plotting 3D |
| simpeg/simpeg | [#627](https://github.com/simpeg/simpeg/issues/627) | Unidades de frecuencia sin especificar (docs EM) | bajo | Inversión geofísica; minería |
| simpeg/simpeg | [#629](https://github.com/simpeg/simpeg/issues/629) | Flag `verbose` de `Utils.download` incompleto | bajo | Bug puntual |
| obspy/obspy | [#2730](https://github.com/obspy/obspy/issues/2730) | `PPSD.plot()`: aceptar Figure/Axes | medio | Ruido sísmico |
| pyvista/pyvista | [#3387](https://github.com/pyvista/pyvista/issues/3387) | Error confuso por mismatch dimensional | medio | Mapeo puntos/celdas VTK |
| pyvista/pyvista | [#1629](https://github.com/pyvista/pyvista/issues/1629) | Mejorar ejemplos del módulo plotting | bajo | Docs |

PyGMT es el de mayor oferta (~29 abordables) y mejor onboarding. Verde,
GSTools, GemPy, LoopStructural, geoh5py y GDAL están vivos pero hoy sin issues
de novato libres (abrir conversación primero).

## B. Pagados (bounty o ruta a empleo)

| Repo | Issue / vía | Pago | Esfuerzo | Nota |
|---|---|---|---|---|
| commaai/openpilot | [#32425](https://github.com/commaai/openpilot/issues/32425) fuzz tx messages test | $100–300 (Algora) | medio | **Python puro, sin hardware — el más viable** |
| commaai/openpilot | [#30693](https://github.com/commaai/openpilot/issues/30693) MetaDrive test en CI | $100–300 | bajo-medio | `good first issue` + CI |
| commaai/openpilot | [#30302](https://github.com/commaai/openpilot/issues/30302) Ford Lightning harness | **$200** | medio | Hardware-dependiente |
| commaai/openpilot | [#33207](https://github.com/commaai/openpilot/issues/33207) MetaDrive en macOS | $100–300 | medio | Usas macOS |
| onyx-dot-app/onyx | [#518](https://github.com/onyx-dot-app/onyx/issues/518) Google Chat connector | ~$250 (clase Algora) | medio | Python/RAG; connectors repetibles |
| supabase/supabase | [#6435](https://github.com/supabase/supabase/issues/6435) newlines en SMS OTP | ruta a **empleo** | bajo | No paga; Supabase contrata de comunidad (precedente peruano) |

**Algora → Perú: CONFIRMADO viable** (Stripe agregó `pe_bank_account` el
2026-02-25). Falta solo crear cuenta y verificar payout en pantalla (login).

## C. Prestigio (poca/ninguna paga, alta visibilidad)

1. [harmonica #37 — Isostasia de Pratt](https://github.com/fatiando/harmonica/issues/37) — física de la Tierra sólida; tu nombre en un método científico.
2. [Loop3D/LoopStructural #145 — fallas curvas/segmentadas](https://github.com/Loop3D/LoopStructural/issues/145) — feature de modelado estructural; alto, alta visibilidad.
3. **GDAL — maintenance work units** (C++) — programa pagado vía PSC/NumFOCUS.
4. **NumFOCUS Small Development Grant ($10k)** — co-escribir propuesta con
   Fatiando/SimPEG (conv. sept–oct 2026). Aquí converge todo: cada PR en el
   ecosistema es el historial que la hace creíble.

## Lectura estratégica

Profundizar en **Fatiando + PyGMT** para construir historial → **openpilot
#32425/#30693** como ingreso paralelo por bounty → objetivo de fondo: **grant
NumFOCUS** (3–6 meses). Repos populares (fCC/PostHog) solo como oportunismo
puntual, no foco.
