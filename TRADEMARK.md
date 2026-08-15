# Swarmbly Trademark Policy

> **STATUS — READ THIS FIRST.**
>
> **The "Swarmbly" and "Swarmbly AI" marks and the Swarmbly logo are NOT
> registered trademarks in any jurisdiction as of the date of this document
> (2026-08-13).** No application has been filed. No entity currently exists to
> hold them (see `GOVERNANCE.md` Section 3).
>
> This document is therefore a **statement of intent**: it describes how the
> project intends the marks to be used, and how it intends to administer them
> once a legal entity exists to do so. It is not an assertion of registered
> rights, and it should not be read as one.
>
> Nothing here is legal advice. The scope of any unregistered rights that may
> arise from use varies by jurisdiction and **has not been verified** in the
> preparation of this document.
>
> **Contact for all trademark questions and permission requests:**
> `sebas_saeu@hotmail.com` — placeholder; the author must replace
> this with a working address before publication.

---

## 1. Why a trademark policy at all

Swarmbly is licensed under AGPL-3.0-or-later. That license deliberately grants
very broad rights: anyone may copy the code, modify it, run it, and
redistribute it, including commercially. The project does not want to narrow
that, and this policy does not narrow it. **Nothing in this document restricts
any right granted by the AGPL.**

What the AGPL does *not* grant is the right to use the project's name. That
omission is standard and it is useful, because copyright and trademark protect
different things:

- **Copyright** governs the code. Under the AGPL it is maximally open.
- **Trademark** governs the *name* — the signal that tells a user what they
  are getting and who stands behind it.

The project's governance model depends on this split. Forking must stay easy,
so that the exit option is real and the maintainers stay accountable. But a
fork must not be able to present itself as Swarmbly, because then a user has no
way to tell whether the thing calling itself Swarmbly follows the
specification, honours the protocol's privacy properties, or does anything the
project has committed to. The marks are the project's principal governance
instrument for exactly this reason — see `GOVERNANCE.md` Section 6.

This policy follows the structure used by the Rust Foundation's trademark
policy: a clear list of uses permitted without asking, and a clear list of uses
that require permission, so that the overwhelming majority of the community
never has to write to anyone. The wording, scope, and specific rules here are
Swarmbly's own; only the shape is borrowed.

## 2. The marks

- The word mark **Swarmbly**
- The word mark **Swarmbly AI**
- The Swarmbly logo, once one exists *(no logo currently exists; when one is
  adopted it will be listed here together with its license)*

The protocol is named **Swarmbly**. The project as published is **Swarmbly AI**.
The repository is `Swarmbly-AI`.

## 3. Uses permitted without asking

You do **not** need to contact anyone for any of the following. Please just go
ahead.

### 3.1 Redistributing Swarmbly unmodified

You may redistribute unmodified copies of Swarmbly under its name, in any
medium, including commercially and including as part of a larger distribution.
Packaging unmodified Swarmbly for a Linux distribution, a container registry, a
package index, or a mirror is expressly fine.

Small changes that do not alter behaviour — build flags, packaging metadata,
patches required by a distribution's policy, backported upstream fixes — do
not count as "modified" for the purposes of this policy.

### 3.2 Factual, descriptive reference

You may use the marks to refer to the project truthfully. This includes:

- Writing about Swarmbly: articles, blog posts, papers, reviews, criticism,
  comparisons, benchmarks, and teaching material. **Including unfavourable
  ones.** This policy will not be used to suppress criticism or unflattering
  benchmark results, and any attempt to use it that way should be treated as
  the governance failure it would be.
- Stating that your software is *compatible with*, *works with*, *built on*,
  *supports*, or *speaks* Swarmbly, where that is accurate.
- Describing yourself as a Swarmbly contributor, node operator, or user, where
  that is accurate.
- Academic citation. Please cite it — see `CITATION.cff`.

The test is whether a reasonable reader would be misled into thinking the
project endorses, produced, or is responsible for your thing. If they would
not, it is fine.

### 3.3 Community events and groups

You may organise and name non-commercial community events and groups using the
marks, without asking: meetups, user groups, study groups, hackathons, reading
groups, conference tracks. "Swarmbly Berlin Meetup", "Swarmbly study group",
"Swarmbly users of Santiago" — all fine.

Please make it clear the event is community-run and not an official project
event. Charging enough to cover venue, food, and travel does not make an event
commercial for this purpose.

### 3.4 Nominative use in non-commercial projects

You may name a personal, non-commercial, clearly-third-party tool with a name
that includes "Swarmbly" where it accurately describes what the tool does —
`swarmbly-node-monitor`, `swarmbly-bench`, `swarmbly.el` — provided the project
description makes clear it is unofficial. Prefixed and suffixed package names
in a package index follow the ecosystem's normal conventions and are fine.

### 3.5 Merchandise for yourself and your group

Print a T-shirt, a sticker, a mug. Make some for your meetup. Selling
merchandise at scale is Section 4.

## 4. Uses that require approval

Please write to `sebas_saeu@hotmail.com` before doing any of the
following. Requests will be answered; the default posture for good-faith
community use is yes.

### 4.1 Distributing a *modified* version under the Swarmbly name

You may fork and modify Swarmbly freely — that is the AGPL, and it is not in
question. What requires approval is distributing your **modified** version
under the Swarmbly name, in a way that suggests it is Swarmbly.

If you have changed behaviour, the protocol, the defaults, or the security or
privacy properties, and you do not have approval, please rename. You may of
course say truthfully that your project is "a fork of Swarmbly" or "based on
Swarmbly" — Section 3.2 covers that. What is not fine is calling the fork itself
Swarmbly, so that a user cannot tell which one they are running.

This is the core rule of this policy, and it exists so that "it says Swarmbly"
continues to mean something.

### 4.2 Commercial products and services named "Swarmbly X"

Naming a commercial product, hosted service, or consultancy offering "Swarmbly
Cloud", "Swarmbly Enterprise", "Swarmbly Pro", "Swarmbly Hosting", or similar
requires approval. So does any name that would reasonably read as an official
Swarmbly offering.

You do not need approval to say, truthfully, that your commercially-offered
service *runs on* or *is built with* Swarmbly. "Acme Inference — powered by
Swarmbly" is descriptive and permitted; "Swarmbly Cloud by Acme" is not, without
approval.

(Separately, and independent of trademark: if you run a modified version as a
network service, clause 13 of the AGPL obliges you to offer users its Corresponding Source.
See `NOTICE`.)

### 4.3 Domain names

Registering a domain whose second-level label is or contains "swarmbly" —
`swarmbly-cloud.com`, `getswarmbly.io`, `swarmbly.<tld>` — requires approval,
because such domains read as official whatever the site says. Subdomains of
your own domain (`swarmbly.acme.com`) and paths (`acme.com/swarmbly`) do not
require approval where the use is otherwise permitted under Section 3.

The project asks that anyone holding a `swarmbly` domain in good faith be
willing to transfer it to the Foundation once one exists, at cost.

### 4.4 The logo

Once a logo exists, modifying it, incorporating it into another logo, or using
it as your own product's or company's mark requires approval. Using the
unmodified logo to refer to the project — in an article, a slide, a
"compatible with" badge — will be permitted under Section 3.2 and its license.

### 4.5 Commercial merchandise at scale

Selling Swarmbly-branded merchandise as a business requires approval.

### 4.6 Certification, endorsement, and compatibility claims

Do not describe anything as "Swarmbly certified", "Swarmbly official", "Swarmbly
approved", or "Swarmbly compliant" without approval. No certification programme
exists yet; if one is created it will be described here.

### 4.7 Company, organisation, and entity names

Naming a company, association, or foundation with a name containing "Swarmbly"
requires approval. This includes entities presented as adjacent to the project
— an "ecosystem foundation" or similar — which `GOVERNANCE.md` Section 7 identifies
as a capture vector.

## 5. How to ask

Email `sebas_saeu@hotmail.com` with:

1. who you are;
2. the exact name or mark you want to use;
3. what the thing is, and whether it is commercial;
4. whether it is modified Swarmbly, and if so, how;
5. where it will appear.

Expect a written answer. Approvals will be specific and in writing; assume no
approval has been given unless you have one. Given the project's current stage
(one maintainer, no entity), response times are best-effort and no service
level is promised.

## 6. General conditions

- **This policy does not restrict the AGPL.** If any part of it is ever read
  as conflicting with a right the AGPL grants, the AGPL prevails and this
  policy is wrong on that point.
- **Do not misrepresent.** Do not imply endorsement, affiliation, or official
  status you do not have. Everything in this policy reduces to that.
- **Do not use the marks in a way that damages them** — malware, fraud, or
  deliberately misleading distribution.
- **The policy may change.** Changes go through the SWIP process
  (`CONTRIBUTING.md` Section 6). Uses that were permitted when begun will be given a
  reasonable transition period if a change affects them.
- **Custody.** The marks are intended to be assigned to the Swarmbly Foundation
  once it exists (`GOVERNANCE.md` Section 4). Until then they are held personally by
  the author, in a personal and non-affiliated capacity. They are not held by,
  licensed to, or in any way associated with any employer.

## 7. Unverified items

Stated explicitly so nobody relies on something that was not checked:

- **Registration status:** unregistered. Not filed. Not searched — no clearance
  search has been performed, so it is **not** known whether "Swarmbly" conflicts
  with an existing mark in any class or jurisdiction. This must be checked
  before any filing and before any enforcement is attempted.
- **Jurisdictional scope of unregistered rights:** not verified.
- **Registration classes, costs, and timelines:** not verified.
- **Enforceability of this policy in its current form:** not reviewed by
  counsel.

---
---

# Política de marca de Swarmbly — resumen en español

> **ESTADO.** Las marcas «Swarmbly» y «Swarmbly AI» y el logotipo de Swarmbly
> **no están registradas en ninguna jurisdicción** a fecha de este documento
> (13-08-2026). No se ha presentado ninguna solicitud y todavía no existe una
> entidad que las ostente (`GOVERNANCE.md` sección 3). Este documento es una
> **declaración de intenciones**, no una afirmación de derechos registrados, y
> no constituye asesoramiento jurídico. En caso de discrepancia, la versión en
> inglés es la de referencia.
>
> **Contacto:** `sebas_saeu@hotmail.com` (marcador de posición).

**Por qué existe.** La AGPL regula el código y lo abre al máximo; no regula el
nombre. El proyecto quiere que bifurcar sea fácil —la opción de salida real es
lo que mantiene honesto a quien mantiene el proyecto— pero que una bifurcación
no pueda presentarse como Swarmbly, porque entonces nadie podría saber si lo que
se llama Swarmbly cumple la especificación. Por eso la marca es la palanca de
gobernanza principal del proyecto (`GOVERNANCE.md` sección 6). **Nada de esta política
restringe ningún derecho concedido por la AGPL.** La estructura sigue la de la
política de marca de la Rust Foundation: una lista de usos libres y una lista
de usos que requieren permiso, para que casi nadie tenga que escribir a nadie.

**Usos permitidos sin pedir permiso**

- Redistribuir Swarmbly **sin modificar**, en cualquier medio, incluso
  comercialmente y como parte de una distribución mayor. Los cambios de
  empaquetado que no alteran el comportamiento no cuentan como modificación.
- **Referencia descriptiva y veraz**: escribir sobre Swarmbly (artículos,
  papers, reseñas, comparativas, benchmarks, crítica — **también la
  desfavorable**; esta política no se usará para acallar críticas); decir que
  tu software es *compatible con* o *está construido sobre* Swarmbly cuando sea
  cierto; describirte como colaborador, operador de nodo o usuario. Citarlo
  académicamente (ver `CITATION.cff`).
- **Eventos y grupos de comunidad** sin ánimo de lucro: meetups, grupos de
  usuarios, hackatones, grupos de estudio. Indica que es comunitario y no
  oficial. Cobrar para cubrir local, comida y viajes no lo vuelve comercial.
- **Uso nominativo en proyectos personales no comerciales**:
  `swarmbly-node-monitor`, `swarmbly-bench`, siempre que quede claro que no es
  oficial.
- **Merchandising para ti y tu grupo**: camisetas, pegatinas, tazas.

**Usos que requieren aprobación** (escribe al contacto de arriba; para uso
comunitario de buena fe la respuesta por defecto es que sí)

- Distribuir una versión **modificada** bajo el nombre Swarmbly. Bifurcar y
  modificar es libre —eso es la AGPL—; lo que requiere permiso es distribuir tu
  versión modificada de forma que parezca ser Swarmbly. Si has cambiado el
  comportamiento, el protocolo o las propiedades de seguridad o privacidad,
  cambia el nombre. Puedes decir con verdad que es «un fork de Swarmbly».
- **Productos y servicios comerciales llamados «Swarmbly X»**: «Swarmbly Cloud»,
  «Swarmbly Enterprise», etc. Sí puedes decir con verdad que tu servicio
  *funciona sobre* Swarmbly. (Aparte: si operas una versión modificada como
  servicio de red, la cláusula 13 de la AGPL te obliga a ofrecer el código fuente
  correspondiente; ver `NOTICE`.)
- **Nombres de dominio** cuyo dominio de segundo nivel sea o contenga
  «swarmbly». Subdominios y rutas dentro de tu propio dominio, no.
- **El logotipo**: modificarlo, incorporarlo a otro logo o usarlo como marca
  propia.
- **Merchandising comercial a escala.**
- **Certificación o respaldo**: «certificado Swarmbly», «oficial», «aprobado».
  No existe todavía ningún programa de certificación.
- **Nombres de empresas, asociaciones o fundaciones** que contengan «Swarmbly»,
  incluidas las entidades presentadas como adyacentes al proyecto — que
  `GOVERNANCE.md` sección 7 identifica como vía de captura.

**Condiciones generales.** Esta política no restringe la AGPL; si alguna vez se
leyera en conflicto con un derecho que la AGPL concede, prevalece la AGPL. No
des a entender respaldo, afiliación ni carácter oficial que no tengas — todo lo
demás se reduce a eso. Los cambios de política pasan por el proceso SWIP. Las
marcas se cederán a la Fundación Swarmbly cuando exista; hasta entonces las
ostenta el autor a título personal y sin afiliación, y no están vinculadas a
ningún empleador.

**Sin verificar.** No se ha hecho ninguna búsqueda de anterioridades, así que
**no se sabe** si «Swarmbly» colisiona con una marca existente en alguna clase o
jurisdicción; hay que comprobarlo antes de cualquier registro o reclamación.
Tampoco se han verificado el alcance de los derechos no registrados, las clases
de registro, los costes ni los plazos, y esta política no ha sido revisada por
asesoría jurídica.
