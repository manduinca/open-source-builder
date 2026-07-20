# Pipeline CNCF + ecosistema Eddú — 2026-07-17

Validación de 25 repos (workflow, un agente por repo). Cada issue verificado
por timeline real (no labels), con protocolo y política de IA por repo.

## Tier A — entrar ya (5 repos)

| Repo | Lang | Issue limpio | Esfuerzo | Protocolo |
|---|---|---|---|---|
| [opentelemetry-java-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation) | Java | [#14395](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14395) spring-cloud-gateway library instrumentation (miembro indicó el camino) | medio | CLA (ya firmaste EasyCLA); discutir en issue antes de feature; sin política IA |
| [prometheus/client_java](https://github.com/prometheus/client_java) | Java | [#2292](https://github.com/prometheus/client_java/issues/2292) bug de quantiles (fresco, 0 rivales) | medio | PR directo + DCO; no usan labels GFI |
| [open-feature/java-sdk](https://github.com/open-feature/java-sdk) | Java | [#1588](https://github.com/open-feature/java-sdk/issues/1588) cache merged context; [#1934](https://github.com/open-feature/java-sdk/issues/1934) provider shutdown | medio | PR directo + DCO, **sin CLA**; `mvn verify` local |
| [1Password/shell-plugins](https://github.com/1Password/shell-plugins) | Go | [#200](https://github.com/1Password/shell-plugins/issues/200) plugin Splunk (observabilidad, 0 rivales) | medio | PR por template + commits firmados, sin CLA; Eddú mergea aquí |
| [apache/skywalking-java](https://github.com/apache/skywalking-java) | Java | [#13945](https://github.com/apache/skywalking-java/issues/13945) tracing ThreadPoolExecutor.invokeAll (fresco) | medio | Apache; PRs de plugin exigen tests E2E (sube esfuerzo) |

## Tier B — posible con reservas (14 repos), issues limpios destacados

| Repo | Issue | Tipo | Nota |
|---|---|---|---|
| **[opentelemetry.io](https://github.com/open-telemetry/opentelemetry.io)** | [#10252](https://github.com/open-telemetry/opentelemetry.io/issues/10252), [#7841](https://github.com/open-telemetry/opentelemetry.io/issues/7841) | docs | ⭐ **Localización al español** — fit único por idioma |
| [cloudevents/sdk-python](https://github.com/cloudevents/sdk-python) | [#247](https://github.com/cloudevents/sdk-python/issues/247) | docs | mejorar docstring; esfuerzo bajo, limpio |
| [cloudevents/sdk-java](https://github.com/cloudevents/sdk-java) | [#585](https://github.com/cloudevents/sdk-java/issues/585) | tests | benchmarks para CloudEvents SQL |
| [dapr/docs](https://github.com/dapr/docs) | [#3985](https://github.com/dapr/docs/issues/3985) | docs | instalación de State Store |
| [dapr/python-sdk](https://github.com/dapr/python-sdk) | [#853](https://github.com/dapr/python-sdk/issues/853) | docs | alinear ejemplos de workflow |
| [prometheus/client_python](https://github.com/prometheus/client_python) | [#1107](https://github.com/prometheus/client_python/issues/1107) | código | unbundle dependency `decorator` |
| [kubernetes-client/python](https://github.com/kubernetes-client/python) | [#2435](https://github.com/kubernetes-client/python/issues/2435) | código | bug de deployment spec |
| [jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) | [#5506](https://github.com/jaegertracing/jaeger/issues/5506) | código | habilitar reglas revive (Go) |
| [vitessio/vitess](https://github.com/vitessio/vitess) | [#18664](https://github.com/vitessio/vitess/issues/18664) | código | bug de log spamming |
| backstage, litmuschaos | — | — | ver detalle en journal del workflow |

Reserva clave de **otel-python** (Tier B): política de IA **estricta** —
comentarios solo humanos, y PRs con asistencia de IA exigen acordar dirección
con maintainers en el issue *antes* de implementar. Requiere cuidado especial.

## Tier C — descartar por ahora (6 repos, con motivo)

- **testcontainers/testcontainers-java** (ecosistema Eddú): repo sano pero
  **cero issues limpios** — los 7 GFI (2018-2024) están todos disputados con
  PRs rivales o enfoques ya rechazados. Entrar hoy es competir en cola.
  Reconsiderar si aparece un GFI fresco o proponiendo algo propio.
- opentelemetry-java (core): sin puerta de entrada (todo disputado/gobernanza).
- kubernetes-client/java, open-feature/python-sdk, kedacore/keda, grafana:
  sin issues abordables limpios ahora.

## Lectura estratégica

- El carril **Java + observabilidad** es el más rico: otel-java-instrumentation,
  prometheus/client_java, open-feature/java-sdk, skywalking-java.
- La localización al español de **opentelemetry.io** es un diferenciador único.
- "Masivo" realista con el listón de calidad = ~12-15 PRs de calidad
  distribuidos (1-2 por repo), NO 50 baratos. Llegar a más exige validar en
  profundidad los backlogs Tier B, no bajar el estándar.

## Lote 1 — ejecutado (resultados)

3 publicados, 1 descartado con criterio. Tasa real de conversión con el listón
de calidad: ~75%.

| Issue | Resultado |
|---|---|
| [cloudevents/sdk-python#302](https://github.com/cloudevents/sdk-python/pull/302) (Fixes #247) | ✅ Publicado — docstring atributos-vs-data. DCO, sin CLA. |
| [prometheus/client_java#2316](https://github.com/prometheus/client_java/pull/2316) (Fixes #2292) | ✅ Publicado — fix de CKMS quantiles que colapsaban al mínimo (18 tests OK verificados). DCO. |
| [opentelemetry.io#10897](https://github.com/open-telemetry/opentelemetry.io/pull/10897) (Part of #7841) | ✅ Publicado — traducción ES de zero-code/js. Reclamado por comment primero; checkbox de IA declarado; EasyCLA ✅. |
| open-feature/java-sdk#1588 | ❌ Descartado — obsoleto: resuelto por PR #1717 (v1.19.0) del propio autor. Alternativa limpia: #1934. |

Lección de escala confirmada: el cuello de botella no es la calidad ni las
ideas, es la **cuota de cómputo** (4 agentes en paralelo la agotan). Escalar
sostenible = lotes de 2-3 espaciados, no 15 de golpe.

## Lote 2 — candidatos (pendiente)

Tier A sin tocar: otel-java-instrumentation #14395 (spring-cloud-gateway),
apache/skywalking-java #13945. Tier B docs: dapr/docs #3985, dapr/python-sdk
#853, cloudevents/sdk-java #585. Validar timeline antes de cada uno.
