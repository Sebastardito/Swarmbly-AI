# Governance · Gobernanza — Swarmbly AI

**Language / Idioma:** [English](#english) · [Español](#español)

> **Status of this document.** This is a statement of current practice and of
> declared intent. The legal structures described as *intended* (Swiss Verein,
> later Stiftung) **do not exist yet**. Nothing here has been reviewed by
> counsel, and no filing has been made. Where a statement is an intention
> rather than a fact, it is marked as such.
>
> **Estado de este documento.** Es una descripción de la práctica actual y una
> declaración de intenciones. Las estructuras jurídicas descritas como
> *previstas* (Verein suizo, más adelante Stiftung) **todavía no existen**.
> Nada de esto ha sido revisado por asesoría legal ni se ha presentado ante
> ningún registro. Cuando algo es una intención y no un hecho, se marca.

> **Contact / Contacto:** `sebas_saeu@hotmail.com`

---

<a name="english"></a>

# English

## 1. Where the project is today

**Status: pre-foundation. Benevolent maintainer.**

Swarmbly AI is currently maintained by its author, **Sebastián A. Espinoza-Ulloa**, in a
personal and non-affiliated capacity. This is a personal project. It carries no
institutional or employer affiliation of any kind, and no employer's name,
resources, or endorsement should be inferred from it.

In practice this means:

- One person holds commit rights and makes final decisions.
- Decisions are made in public, in issues and PRs, but they are not yet made
  *by* a body — they are made by an individual who is expected to explain
  himself.
- There is no board, no membership, no vote, and no legal entity.

This is the honest description of a project at this stage, and pretending
otherwise would be worse than admitting it. A governance document that
describes an elaborate structure nobody is operating is a liability: it
misleads contributors about what protections they actually have. What follows
distinguishes carefully between what exists now and what is intended.

The benevolent-maintainer phase is explicitly **transitional**. It is a
starting condition, not a destination, and Section 3 describes what it is meant to
become.

## 2. How decisions are made now

1. **Bugs, tests, docs, refactors.** Maintainer merges on review. No ceremony.
2. **Protocol changes.** Require a SWIP (see `CONTRIBUTING.md` Section 6). Minimum
   14-day review for anything touching wire format, security, or privacy;
   7 days otherwise. The maintainer decides, but must respond in writing to
   substantive objections raised during the review window. "Merged without
   comment over an unanswered objection" is a governance failure even when
   the decision is correct.
3. **Direction and scope.** The maintainer sets these. Where a decision is
   contested, the reasoning is written down and merged into the repository
   so that the record survives the argument.
4. **Anything with legal or licensing consequence.** Slower, and stated
   publicly before it is done — never as a fait accompli in a merge commit.

Every consequential decision leaves a written trail in the repository. That is
the only mechanism currently constraining the maintainer, and it is
deliberately the first mechanism, because it is the one that keeps working
after the others are added.

## 3. Intended path: Swiss Verein → Stiftung

**This is an intention, not an accomplished fact. No entity has been formed.**

### Stage 1 — Swiss *Verein* (association)

The intended first legal step is a Swiss *Verein*: a membership association.
The reasons for choosing this form, and for choosing it *first*:

- It is a **membership** body. Members hold governance rights, which gives the
  community a formal seat rather than an implied one. That is the point of
  moving off benevolent-maintainer.
- It is comparatively **light to form and to operate** — appropriate to a
  project of this size, where governance overhead that exceeds engineering
  capacity would strangle the work.
- Switzerland's association and foundation law is well understood in
  open-source and protocol contexts, and its neutrality is meaningful for
  infrastructure intended to be internationally usable.
- It is **reversible enough**. A Verein can be wound up or restructured if the
  project's needs turn out to be different from what was predicted.

Trigger for forming it: when the project needs to hold assets, receive
donations, hold the trademark, or sign anything — whichever comes first.
Forming it before that would be premature bureaucracy.

*Unverified:* the specific formation requirements, minimum member counts,
statutory content, tax treatment, and costs under Swiss law have **not** been
verified in the preparation of this document. They must be confirmed with
Swiss counsel before any filing. No timeline is committed to here.

### Stage 2 — *Stiftung* (foundation)

The intended longer-term structure is a Swiss *Stiftung*: a foundation with a
fixed, chartered purpose and — this is the essential property — **no owners**.

Why a foundation eventually, rather than staying a Verein:

- A foundation's **purpose is locked into its charter** and is supervised.
  A Verein's members can amend its statutes; a foundation's purpose is far
  harder to redirect. That is precisely the protection wanted for
  infrastructure meant to outlast its founder's interest in it.
- **Nobody owns a foundation.** There are no shares, no members with residual
  claims, nothing to acquire. The most common way an open-source project is
  captured is that someone buys the entity that controls it. A foundation
  removes that transaction from the board.
- It is the appropriate long-term custodian for the trademark, which is the
  project's real control lever (Section 5, and `TRADEMARK.md`).

Trigger for the transition: when the protocol has independent implementations
and independent operators, i.e. when the project stops being one person's work
in substance and not merely in form. Converting earlier would create an
institution with no constituency, which is its own failure mode.

*Unverified:* Swiss foundation formation requires endowment, deed, and
supervisory authority approval; the specific thresholds, ongoing supervision
obligations, and costs have **not** been verified here and must be confirmed
with counsel. **No date is committed to.**

## 4. What the Foundation will own

When the Foundation exists, it is intended to hold:

**Yes — copyright.** Insofar as the project holds any copyright (in the
specification, in project-authored documentation, and in whatever the founder
personally assigns), it is intended to sit with the Foundation.

Note the important limit, which follows directly from using a DCO instead of
a CLA: **contributor copyright stays with contributors.** The Foundation will
never hold the whole codebase's copyright, and that is intentional. It means
the Foundation cannot unilaterally relicense the project even if it wanted to.
The Foundation is designed to be *unable* to do the thing that would most
damage the community — a constraint worth more than any promise not to.

**Yes — trademark.** The "Swarmbly" and "Swarmbly AI" marks, and the logo, are
intended to be assigned to the Foundation. This is the substantive transfer.
See Section 5.

**Yes — domains, infrastructure, and the project's accounts.** Custody of
these should not depend on one individual continuing to pay a renewal invoice.

**Yes — donated funds**, held to the chartered purpose, with public accounts.

## 5. What the Foundation will *not* do

### It will not sell proprietary exceptions. Dual licensing is rejected.

This is the sharpest commitment in this document and it is made deliberately.

The project **rejects the dual-licensing / proprietary-exception business
model**: the arrangement where a copyright holder offers the code under AGPL
to the public while selling private, non-copyleft licenses to companies that
would rather not comply.

Why it is rejected:

1. **It is incompatible with the foundation mandate.** A foundation exists to
   hold a purpose in trust for a community. Selling exceptions makes the
   community's copyleft a product, sold to the parties most interested in
   escaping it. The Foundation would be monetising the obligation its
   contributors accepted, which is not custodianship — it is arbitrage against
   the people it is supposed to serve.
2. **It corrupts the incentives around the license.** Under dual licensing,
   every strengthening of the copyleft increases the price of the exception.
   The rights-holder acquires a financial interest in the AGPL being
   *inconvenient*, which is the opposite of the interest a steward should
   have.
3. **It requires the CLA the project has already refused.** Selling exceptions
   requires holding all the copyright, which requires copyright assignment
   from every contributor. The project chose a DCO precisely to avoid that
   (`CONTRIBUTING.md` Section 2). Dual licensing is not merely rejected here — under
   the DCO it is not available. The two decisions lock together, and that
   interlock is the design.
4. **It splits the community into paying and non-paying tiers.** In a
   volunteer-node protocol, where the network's value comes from participants
   who are not paying anyone, that split is corrosive to the thing being
   built.

If the project needs revenue, it will look to donations, grants, sponsorship,
paid support, and paid hosting of services the Foundation itself runs — none
of which require anyone to be sold an exemption from the license everyone else
lives under.

### It will not premine or issue a transferable token

There is **no premine and no transferable token**, and none is planned.

If Swarmbly ever adopts an internal accounting unit for contribution or
reputation, the commitment is that such a unit is **non-transferable** and
exists solely to make the protocol's resource allocation work. A transferable
token creates a class of holders whose interest is the token's price rather
than the network's usefulness, and it converts every technical decision into a
question about that price. This project will not build that constituency.

### It will not act as the sole gatekeeper of implementations

Swarmbly is a protocol. Independent implementations are a success condition,
not a threat. The Foundation may certify compatibility and may govern use of
the name (Section 5, `TRADEMARK.md`), but it will not attempt to make itself the only
permitted implementer.

### It will not accept funding conditioned on protocol direction

Donations and grants are welcome. Donations and grants with strings attached
to technical direction, roadmap priority, or governance seats are not. Funding
sources above a materiality threshold, to be set in the charter, will be
disclosed publicly.

## 6. Trademark as the real control lever

Copyleft governs copying. It does not govern *naming*, and naming is what
users actually rely on when they decide what to trust.

Under the AGPL anyone may fork Swarmbly, change it however they wish, and ship
it. That is correct and the project will not try to prevent it. What that fork
may **not** do is present itself as Swarmbly — because trademark, unlike
copyright, is exactly the right to control what a name is applied to.

This asymmetry is deliberate, and it is why the trademark is the project's
principal governance instrument:

- The code stays maximally free, and forking stays maximally easy. The exit
  option is real, which is what keeps the maintainers honest.
- The *name* remains a signal that the thing behind it follows the
  specification and the project's commitments. A user who sees "Swarmbly"
  should be able to rely on what that implies.
- Enforcement is proportionate. A trademark dispute is about a name, not about
  taking someone's code away. The remedy is that they rename, not that they
  stop.

`TRADEMARK.md` sets out the policy. Note there that **the marks are not
currently registered** and the policy is a statement of intent; registration is
one of the concrete triggers for forming the Verein (Section 3).

## 7. What would count as capture

The project commits to resisting the following. They are listed by name so
that if any of them starts happening, it can be pointed at with this document
in hand rather than argued about in the abstract.

1. **Relicensing away from copyleft.** Any move to a permissive or
   source-available license, or to a "BSL-style" delayed-open license. The DCO
   makes this structurally very hard; that is the point.
2. **Introducing a CLA.** Any request that contributors assign or broadly
   license copyright to a single entity — however it is framed, and
   particularly if framed as an administrative cleanup.
3. **Selling proprietary exceptions.** See Section 5. Watch especially for the
   soft version: a "commercial edition", an "enterprise tier" of the *protocol*
   rather than of a hosted service, or a licence carve-out for one large
   partner.
4. **Acquisition of the entity.** Any structure where the Foundation, or a
   Verein preceding it, can be bought, merged, or brought under another
   organisation's control. A foundation with no owners is the defence; erosion
   of that property is the attack.
5. **Board or maintainer capture by a single sponsor.** One funder holding
   enough seats, staff time, or budget dependence that its preferences become
   the roadmap. Loud versions are rare; the common version is that the only
   people with paid time to do the work all have the same employer.
6. **A token or premine appearing later.** Including via an "ecosystem
   foundation", a "network incentive layer", or an affiliated entity that the
   project describes as separate while sharing its name and its people.
7. **De facto centralisation of the network.** If the great majority of nodes,
   orchestrators, or discovery infrastructure ends up run by one operator, the
   protocol is decentralised only on paper. This is a technical failure with
   governance consequences, and it belongs on this list.
8. **Specification drift toward one implementation.** When "what the reference
   implementation does" quietly replaces "what the specification says",
   independent implementations become impossible and the protocol has one
   owner again.
9. **Governance theatre.** Bodies that exist on paper but do not meet, votes
   that are always unanimous, review windows that are always waived. A process
   that is never inconvenient is not constraining anyone.
10. **Loss of the written record.** Decisions moving to private channels —
    DMs, a closed chat, a call with no notes. Every mechanism in this document
    depends on decisions being written down where they can be read later by
    people who were not in the room.

**Commitment.** If any of these is proposed, it will be proposed *in public,
in writing, in advance*, with reasoning, and with time for objection. The
project may still be captured — no document prevents that — but it will not be
captured quietly.

## 8. Amending this document

Changes to this file go through the SWIP process (`CONTRIBUTING.md` Section 6) with the
long review window, regardless of size. Once the Foundation exists, the
charter governs and this document describes practice under it; where the two
conflict, the charter wins and this file is wrong and must be fixed.

---
---

<a name="español"></a>

# Español

## 1. Dónde está el proyecto hoy

**Estado: pre-fundacional. Mantenedor benevolente.**

Swarmbly AI lo mantiene actualmente su autor, **Sebastián A. Espinoza-Ulloa**, a título
personal y sin afiliación. Es un proyecto personal. No tiene vinculación
institucional ni empresarial de ningún tipo, y de él no debe inferirse el
nombre, los recursos ni el respaldo de ningún empleador.

En la práctica esto significa:

- Una sola persona tiene permisos de escritura y toma las decisiones finales.
- Las decisiones se toman en público, en issues y PRs, pero todavía no las
  toma *un órgano*: las toma un individuo del que se espera que dé
  explicaciones.
- No hay junta, ni socios, ni votación, ni entidad jurídica.

Esta es la descripción honesta de un proyecto en esta etapa, y fingir otra cosa
sería peor que admitirlo. Un documento de gobernanza que describe una
estructura elaborada que nadie está operando es un pasivo: engaña a quienes
contribuyen sobre las protecciones que realmente tienen. Lo que sigue distingue
con cuidado entre lo que existe ahora y lo que se pretende.

La fase de mantenedor benevolente es explícitamente **transitoria**. Es una
condición de partida, no un destino, y la sección 3 describe en qué debe convertirse.

## 2. Cómo se decide ahora

1. **Bugs, pruebas, documentación, refactorizaciones.** El mantenedor integra
   tras revisión. Sin ceremonia.
2. **Cambios de protocolo.** Requieren una SWIP (ver `CONTRIBUTING.md` sección 6).
   Revisión mínima de 14 días para todo lo que toque formato de mensajes,
   seguridad o privacidad; 7 días en el resto. El mantenedor decide, pero debe
   responder por escrito a las objeciones sustantivas planteadas durante la
   ventana de revisión. «Integrado sin comentar sobre una objeción sin
   responder» es un fallo de gobernanza aunque la decisión sea acertada.
3. **Dirección y alcance.** Los fija el mantenedor. Cuando una decisión es
   discutida, el razonamiento se escribe y se integra en el repositorio, para
   que el registro sobreviva a la discusión.
4. **Cualquier cosa con consecuencias legales o de licencia.** Más despacio, y
   anunciada públicamente antes de hacerse — nunca como hecho consumado en un
   commit de merge.

Toda decisión con consecuencias deja rastro escrito en el repositorio. Es el
único mecanismo que hoy limita al mantenedor, y es deliberadamente el primero,
porque es el que sigue funcionando cuando se añaden los demás.

## 3. Ruta prevista: Verein suizo → Stiftung

**Esto es una intención, no un hecho consumado. No se ha constituido ninguna
entidad.**

### Etapa 1 — *Verein* suizo (asociación)

El primer paso jurídico previsto es un *Verein* suizo: una asociación de
personas socias. Las razones para elegir esta forma, y para elegirla
*primero*:

- Es un órgano **de socios**. Las personas asociadas tienen derechos de
  gobernanza, lo que le da a la comunidad un asiento formal y no solo
  implícito. Ese es el sentido de salir del mantenedor benevolente.
- Es comparativamente **ligero de constituir y de operar**, algo apropiado
  para un proyecto de este tamaño, donde una carga de gobernanza que supere la
  capacidad de ingeniería asfixiaría el trabajo.
- El derecho suizo de asociaciones y fundaciones se conoce bien en contextos
  de software libre y de protocolos, y su neutralidad tiene un valor real para
  infraestructura pensada para usarse internacionalmente.
- Es **suficientemente reversible**. Un Verein puede disolverse o
  reestructurarse si las necesidades del proyecto resultan ser distintas de lo
  previsto.

Detonante para constituirlo: cuando el proyecto necesite tener activos,
recibir donaciones, ostentar la marca o firmar algo — lo que ocurra primero.
Constituirlo antes sería burocracia prematura.

*Sin verificar:* los requisitos concretos de constitución, el número mínimo de
socios, el contenido estatutario, el tratamiento fiscal y los costes bajo
derecho suizo **no** se han verificado al preparar este documento. Deben
confirmarse con asesoría jurídica suiza antes de cualquier trámite. Aquí no se
compromete ningún plazo.

### Etapa 2 — *Stiftung* (fundación)

La estructura prevista a largo plazo es una *Stiftung* suiza: una fundación con
un fin fijado en su carta fundacional y —esta es la propiedad esencial— **sin
propietarios**.

Por qué una fundación con el tiempo, y no quedarse en Verein:

- El **fin de una fundación queda blindado en su carta** y está sujeto a
  supervisión. Los socios de un Verein pueden reformar los estatutos; el fin
  de una fundación es mucho más difícil de reorientar. Esa es justamente la
  protección que se quiere para una infraestructura pensada para durar más
  que el interés de su fundador en ella.
- **Nadie es dueño de una fundación.** No hay participaciones, no hay socios
  con derechos residuales, no hay nada que adquirir. La forma más habitual de
  capturar un proyecto libre es comprar la entidad que lo controla. Una
  fundación retira esa operación del tablero.
- Es la custodia adecuada a largo plazo para la marca, que es la palanca de
  control real del proyecto (sección 5 y `TRADEMARK.md`).

Detonante de la transición: cuando el protocolo tenga implementaciones y
operadores independientes, es decir, cuando el proyecto deje de ser el trabajo
de una sola persona en sustancia y no solo en la forma. Convertirlo antes
crearía una institución sin base social, que es otro modo de fallo.

*Sin verificar:* constituir una fundación suiza exige dotación, escritura y
aprobación de la autoridad de supervisión; los umbrales concretos, las
obligaciones de supervisión continuada y los costes **no** se han verificado
aquí y deben confirmarse con asesoría. **No se compromete ninguna fecha.**

## 4. Qué tendrá la Fundación

Cuando la Fundación exista, se prevé que ostente:

**Sí — derechos de autor.** En la medida en que el proyecto ostente algún
derecho de autor (sobre la especificación, sobre la documentación de autoría
del proyecto y sobre lo que el fundador ceda personalmente), la intención es
que resida en la Fundación.

Nótese el límite importante, que se deriva directamente de usar DCO en lugar
de CLA: **el copyright de quienes contribuyen sigue siendo suyo.** La Fundación
nunca tendrá el copyright de todo el código, y eso es intencionado. Significa
que la Fundación no puede relicenciar el proyecto de forma unilateral aunque
quisiera. Está diseñada para ser *incapaz* de hacer lo que más daño causaría a
la comunidad: una restricción que vale más que cualquier promesa de no
hacerlo.

**Sí — la marca.** La intención es ceder a la Fundación las marcas «Swarmbly» y
«Swarmbly AI» y el logotipo. Esta es la transferencia sustantiva. Ver la sección 5.

**Sí — dominios, infraestructura y las cuentas del proyecto.** Su custodia no
debería depender de que una persona concreta siga pagando una renovación.

**Sí — fondos donados**, afectos al fin fundacional y con cuentas públicas.

## 5. Qué **no** hará la Fundación

### No venderá excepciones propietarias. El doble licenciamiento queda rechazado.

Es el compromiso más tajante de este documento y se asume de forma
deliberada.

El proyecto **rechaza el modelo de negocio de doble licencia / excepción
propietaria**: el arreglo por el cual el titular de los derechos ofrece el
código bajo AGPL al público mientras vende licencias privadas sin copyleft a
las empresas que prefieren no cumplirlo.

Por qué se rechaza:

1. **Es incompatible con el mandato fundacional.** Una fundación existe para
   custodiar un fin en beneficio de una comunidad. Vender excepciones
   convierte el copyleft de esa comunidad en un producto, vendido justamente a
   quienes más interés tienen en eludirlo. La Fundación estaría monetizando la
   obligación que aceptaron quienes contribuyeron: eso no es custodia, es
   arbitraje contra las personas a las que debería servir.
2. **Corrompe los incentivos alrededor de la licencia.** Con doble licencia,
   cada refuerzo del copyleft encarece la excepción. El titular adquiere un
   interés económico en que la AGPL resulte *incómoda*, que es lo contrario
   del interés que debería tener un custodio.
3. **Exige el CLA que el proyecto ya ha rechazado.** Vender excepciones
   requiere ostentar todo el copyright, lo que requiere cesión de derechos de
   cada persona que contribuye. El proyecto eligió DCO precisamente para
   evitarlo (`CONTRIBUTING.md` Section 2). El doble licenciamiento no solo se rechaza
   aquí: bajo el DCO, sencillamente no está disponible. Las dos decisiones se
   encajan entre sí, y ese encaje es el diseño.
4. **Parte la comunidad en niveles de pago y de no pago.** En un protocolo de
   nodos voluntarios, donde el valor de la red viene de participantes que no
   le pagan a nadie, esa división corroe justamente lo que se está
   construyendo.

Si el proyecto necesita ingresos, mirará hacia donaciones, subvenciones,
patrocinio, soporte de pago y alojamiento de pago de servicios que opere la
propia Fundación — nada de lo cual exige venderle a nadie una exención de la
licencia bajo la que vive todo el mundo.

### No habrá premine ni token transferible

**No hay premine ni token transferible**, y no está previsto que lo haya.

Si Swarmbly llegara a adoptar alguna unidad interna de contabilidad para
contribución o reputación, el compromiso es que esa unidad sea **no
transferible** y exista únicamente para que funcione la asignación de recursos
del protocolo. Un token transferible crea una clase de tenedores cuyo interés
es el precio del token y no la utilidad de la red, y convierte cada decisión
técnica en una pregunta sobre ese precio. Este proyecto no va a construir esa
base social.

### No será el guardián único de las implementaciones

Swarmbly es un protocolo. Las implementaciones independientes son una condición
de éxito, no una amenaza. La Fundación podrá certificar compatibilidad y podrá
regular el uso del nombre (sección 5, `TRADEMARK.md`), pero no intentará convertirse
en la única implementadora permitida.

### No aceptará financiación condicionada a la dirección del protocolo

Las donaciones y subvenciones son bienvenidas. Las donaciones y subvenciones
con condiciones sobre la dirección técnica, la prioridad del roadmap o los
asientos de gobernanza, no. Las fuentes de financiación por encima de un
umbral de materialidad, que fijará la carta fundacional, se harán públicas.

## 6. La marca como palanca de control real

El copyleft regula la copia. No regula el *nombre*, y el nombre es en lo que
realmente se apoyan las personas usuarias cuando deciden en qué confiar.

Bajo la AGPL cualquiera puede bifurcar Swarmbly, cambiarlo como quiera y
distribuirlo. Eso es correcto y el proyecto no intentará impedirlo. Lo que ese
fork **no** puede hacer es presentarse como Swarmbly — porque la marca, a
diferencia del copyright, es exactamente el derecho a controlar a qué se le
aplica un nombre.

Esta asimetría es deliberada, y es la razón de que la marca sea el principal
instrumento de gobernanza del proyecto:

- El código sigue siendo máximamente libre y bifurcarlo sigue siendo
  máximamente fácil. La opción de salida es real, que es lo que mantiene
  honestos a quienes mantienen el proyecto.
- El *nombre* sigue siendo una señal de que lo que hay detrás cumple la
  especificación y los compromisos del proyecto. Quien vea «Swarmbly» debería
  poder fiarse de lo que eso implica.
- La defensa es proporcionada. Una disputa de marca va sobre un nombre, no
  sobre quitarle el código a nadie. El remedio es que se cambien de nombre, no
  que dejen de existir.

`TRADEMARK.md` desarrolla la política. Ténganse en cuenta allí dos cosas: las
marcas **no están registradas actualmente** y la política es una declaración
de intenciones; el registro es uno de los detonantes concretos para constituir
el Verein (sección 3).

## 7. Qué contaría como captura

El proyecto se compromete a resistir lo siguiente. Se enumera con nombre y
apellidos para que, si alguna de estas cosas empieza a ocurrir, se pueda
señalar con este documento en la mano en vez de discutirlo en abstracto.

1. **Relicenciar fuera del copyleft.** Cualquier movimiento hacia una licencia
   permisiva, «source-available» o de apertura diferida tipo BSL. El DCO lo
   hace estructuralmente muy difícil; de eso se trata.
2. **Introducir un CLA.** Cualquier petición de que quienes contribuyen cedan
   o licencien ampliamente su copyright a una única entidad — se presente como
   se presente, y en especial si se presenta como una limpieza
   administrativa.
3. **Vender excepciones propietarias.** Ver la sección 5. Ojo sobre todo con la versión
   suave: una «edición comercial», un «nivel enterprise» del *protocolo* y no
   de un servicio alojado, o una exención de licencia para un socio grande.
4. **Adquisición de la entidad.** Cualquier estructura en la que la Fundación,
   o el Verein que la precede, pueda comprarse, fusionarse o quedar bajo el
   control de otra organización. Una fundación sin propietarios es la defensa;
   la erosión de esa propiedad es el ataque.
5. **Captura de la junta o del equipo mantenedor por un solo patrocinador.**
   Un financiador con suficientes asientos, horas de personal o dependencia
   presupuestaria como para que sus preferencias sean el roadmap. Las versiones
   escandalosas son raras; la habitual es que todas las personas con tiempo
   pagado para hacer el trabajo tengan el mismo empleador.
6. **Que aparezca un token o un premine más adelante.** Incluido por la vía de
   una «fundación del ecosistema», una «capa de incentivos de red» o una
   entidad afiliada que el proyecto describa como separada mientras comparte
   su nombre y su gente.
7. **Centralización de hecho de la red.** Si la gran mayoría de nodos,
   orquestadores o infraestructura de descubrimiento acaba operada por un solo
   actor, el protocolo está descentralizado solo sobre el papel. Es un fallo
   técnico con consecuencias de gobernanza, y por eso está en esta lista.
8. **Deriva de la especificación hacia una implementación.** Cuando «lo que
   hace la implementación de referencia» sustituye en silencio a «lo que dice
   la especificación», las implementaciones independientes se vuelven
   imposibles y el protocolo vuelve a tener dueño.
9. **Teatro de gobernanza.** Órganos que existen sobre el papel pero no se
   reúnen, votaciones siempre unánimes, ventanas de revisión que siempre se
   dispensan. Un proceso que nunca resulta incómodo no está limitando a nadie.
10. **Pérdida del registro escrito.** Que las decisiones se muden a canales
    privados: mensajes directos, un chat cerrado, una llamada sin acta. Todos
    los mecanismos de este documento dependen de que las decisiones queden
    escritas donde puedan leerlas después quienes no estuvieron en la sala.

**Compromiso.** Si se propone alguna de estas cosas, se propondrá *en público,
por escrito y con antelación*, con su razonamiento y con tiempo para objetar.
El proyecto todavía podría ser capturado —ningún documento lo impide— pero no
lo será en silencio.

## 8. Modificar este documento

Los cambios a este archivo pasan por el proceso SWIP (`CONTRIBUTING.md` sección 6) con
la ventana de revisión larga, sea cual sea su tamaño. Una vez exista la
Fundación, manda la carta fundacional y este documento describe la práctica
bajo ella; si ambos entran en conflicto, gana la carta y este archivo está
equivocado y hay que corregirlo.
