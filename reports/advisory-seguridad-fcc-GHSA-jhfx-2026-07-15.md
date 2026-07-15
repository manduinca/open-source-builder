# Advisory de seguridad fCC GHSA-jhfx-pvhv-hmjg — análisis y decisión (2026-07-15)

**Decisión: NO contribuir un fix. Esperar / coordinar solo por canal privado.**

## Qué es

Advisory *published* de freeCodeCamp, severidad media (CVSS 5.7), CWE-294
(capture-replay) + CWE-613 (insufficient session expiration): "Email address
change requests can be replayed with attacker's address". Publicado
2026-01-14, **"Patches: Not yet"**.

Lo detectamos por casualidad al investigar la raíz de nuestro bug de UX
(#68738): el `authToken` del flujo de cambio de email no está amarrado al
email destino, así que un link se puede *replay* cambiando la dirección.

## Por qué NO lo tocamos

1. **Ya tiene remediation asignada en privado** a `ojeytonwilliams` (core dev
   del `api/`, autor del `/confirm-email`) con `ShaunSHamilton` como verifier.
   Un PR nuestro colisiona con su trabajo.
2. **fCC prohíbe explícitamente PRs/issues públicos de seguridad.** Canal:
   `possible-security-issue@freecodecamp.org`. El advisory describe impacto,
   no mecanismo ni parche — un PR con el diff sería disclosure no coordinada.
3. **Riesgo reputacional**: un PR de seguridad no solicitado cae mal.

## El fix real (documentado por si se retoma por el canal correcto)

Raíz en `api/src/routes/protected/settings.ts`: `createAuthToken(user.id)`
ata el token solo a `userId`; `/confirm-email` valida `targetUser.newEmail ===
email` (el pending *actual*, no el email para el que se emitió el token).

- **Opción (a), recomendada**: añadir `email String?` a `model AuthToken`
  (`api/prisma/schema.prisma`), guardarlo al crear el token, y validar
  `authToken.email === email` en `/confirm-email`. ~1 campo + 3 líneas + tests.
- **Opción (b), complemento**: invalidar tokens previos al crear uno nuevo
  (resuelve el TODO existente de "clean up other tokens").
- Tests en `api/src/routes/protected/settings.test.ts` (`describe
  '/confirm-email'`): añadir `email` al seed del token + un caso de replay.

## Fuente del protocolo de seguridad

- https://contribute.freecodecamp.org/security/ ("Don't create public GitHub
  issues for security problems"; email `possible-security-issue@`; acuse
  48–72h, disclosure coordinado ≤90 días; reconocimiento en Hall of Fame,
  sin bounties).
