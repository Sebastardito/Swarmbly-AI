# Swarmbly AI

### La barrera para servir inteligencia artificial deja de ser el capital y pasa a ser la participación

**Sebastián Espinoza** · Pontificia Universidad Católica del Ecuador · University of Saskatchewan
Whitepaper v1.4 · especificación v0.2 · implementación de referencia y primeras mediciones publicadas
AGPL-3.0-or-later (software) · CC BY 4.0 (texto) · `github.com/Sebastardito/Swarmbly-AI`

---

## La asimetría

El conocimiento para construir inteligencia artificial es público. Los pesos de los modelos, las recetas de entrenamiento y los motores de inferencia se publican abiertamente y mejoran cada mes. **El capital para operarla no lo es.** Los centros de datos consumieron 415 TWh en 2024 —cerca del 1,5 % de la electricidad mundial— con proyecciones de 945 TWh para 2030, y esa curva de crecimiento pasa por la construcción, que solo está al alcance de quien puede financiarla.

De modo que una tecnología cuyo conocimiento es de todos termina controlada por quien puede pagar los edificios. No por una patente. Por un contrato de energía.

**Mientras tanto, el hardware ya existe, encendido y ocioso.** La plataforma insignia del cómputo voluntario agrega hoy alrededor de **700.000 dispositivos activos, 4 millones de núcleos de CPU, 560.000 GPU y 93 PetaFLOPS**, desde una comunidad que ha *encogido* un 80 % en dos décadas. Esa cifra es un suelo, tomado de un único nicho en declive, no una proyección. A nivel de una sola máquina, se reporta que una RTX 4090 ociosa sirve inferencia de modelos de lenguaje a **$0,111–0,149 por millón de tokens**, al 62–78 % del rendimiento de una H100 por aproximadamente la mitad del costo.

La capacidad de inferencia ociosa del mundo no es una hipótesis. Lo que faltaba era un protocolo bajo el cual pudiera usarse.

## Por qué nadie lo ha logrado todavía

Todos los intentos serios hasta ahora han repartido el **modelo**: distribuyen capas del transformer entre máquinas, de modo que las activaciones intermedias cruzan la internet pública en cada token generado. Ese diseño choca de frente con un muro físico: la interconexión de un centro de datos mueve 900 GB/s; la subida doméstica mueve unos 60 Mbps. **Una razón de aproximadamente 120.000×**, y de cuatro a cinco órdenes de magnitud en latencia.

Los resultados medidos coinciden con la predicción. Petals, la implementación de referencia de ese enfoque, pierde el 31 % de su rendimiento solo por la red al pasar de un enlace de laboratorio a uno realista; un enjambre geodistribuido real de catorce servidores alcanza 0,83 pasos por segundo.

Eso no es una mala implementación. Es la respuesta correcta a la pregunta equivocada.

## El replanteamiento

Swarmbly hace otra pregunta: no *cómo ejecutar un modelo grande repartido entre muchas máquinas*, sino **cómo ejecutar muchos modelos pequeños completos sobre un problema grande.**

Un orquestador pequeño, en el computador del propio usuario, descompone la petición en microtareas semánticas. Cada una se despacha **una sola vez**, de forma asíncrona, a un nodo voluntario que ejecuta un modelo pequeño completo. Los fragmentos devueltos —*contigs*, en el vocabulario del ensamblaje de genomas que el diseño toma prestado deliberadamente— se verifican, se seleccionan y se empalman localmente.

**La red se cruza una vez por fragmento y por sesión, en lugar de una vez por capa y por token.** Ese único cambio mueve la arquitectura del lado del muro de 120.000× donde pierde, al lado donde el hardware doméstico puede siquiera participar. Repartir un modelo crea una cadena, donde cada máquina espera a la anterior. Repartir un problema crea un conjunto, donde todas trabajan a la vez. Ese contraste es arquitectónico: el rendimiento y la latencia de Swarmbly todavía no se han medido, y esta página no hace ninguna afirmación de velocidad en su nombre.

## Lo que ya está medido

El diseño descansa sobre una afirmación falsable: **cuanto más contexto compartido lleve cada fragmento, menos calidad se pierde al volver a juntar las piezas.** Se registró públicamente un criterio de continuar o abandonar *antes de que existiera dato alguno*: si la pérdida no bajaba del 5 % en ninguna categoría de tarea, había que descartar la arquitectura.

Ya se ha ejecutado contra tres familias de modelos reales. La predicción se sostuvo:

| Contexto compartido (ρ) | Calidad perdida por fragmentar |
|---|---|
| 1,00 | 24,1 % |
| 1,25 | 20,4 % |
| 1,50 | 16,1 % |
| 2,00 | **13,7 %** |

Monótona, tanto en la razón como en la diferencia absoluta que no depende del denominador. **Tres categorías de tarea quedaron por debajo del umbral registrado de antemano, y en dos de ellas el impuesto se volvió negativo: fragmentar el problema y reensamblarlo produjo una respuesta *mejor* que hacerlo de una sola pieza, hasta en un 9,0 %.**

Ese es el argumento central, medido en vez de afirmado: la variable que el diseño señala como variable de control se comporta como variable de control. Dos salvedades viajan con esa tabla en lugar de omitirse: las cifras provienen de uno de los dos instrumentos de coherencia —el segundo no produjo medición utilizable en este corpus— y uno de los ocho prompts no llegó a producir línea base alguna, de modo que sus celdas quedan excluidas.

## Lo que no está demostrado — dicho aquí, no escondido

Una de las contribuciones publicadas **no** sobrevivió a su primera prueba. La arquitectura devuelve un *mapa de confianza*: como familias de modelo independientes responden la misma microtarea, su acuerdo puede puntuarse por unidad, y un proveedor centralizado único no tiene nada que alinear. El mecanismo funciona. Pero la primera medición no encontró **relación alguna entre el acuerdo y la calidad juzgada** (*r* = −0,030 sobre 597 unidades). El instrumento era débil —el juez automático aceptó el 93 % de todo—, así que la afirmación honesta es que la propiedad está **sin sustento, no refutada**. Se ha degradado en el whitepaper en consecuencia, en el mismo documento que primero la anunciaba.

Las mediciones son además pequeñas: ocho prompts —uno de ellos sin línea base utilizable—, una semilla, modelos de 2–3 B. Una señal sobre la que actuar, no un banco de referencia.

**Cuatro cosas que este proyecto no afirma.** **No es más rápido que una API comercial** para quien ya tiene el equipo para usarla: la decodificación especulativa en un solo nodo le gana en latencia a cualquier esquema de fragmentación, y la latencia propia de Swarmbly ni siquiera está medida. **No ofrece contexto ilimitado**, solo un límite mucho más alto que vive en la máquina del usuario en vez de en el plan de precios de un proveedor. **No es cifrado**: fragmentar encarece la reconstrucción y nada más, y por eso el trabajo realmente sensible se enruta a un círculo cerrado o se mantiene enteramente local. Y **no ha demostrado un beneficio ambiental**: el argumento es sólido, la medición todavía no está hecha, y el proyecto se compromete a publicarla sea cual sea el resultado.

Esta sección existe porque un proyecto que esconde su primer resultado negativo no se ha ganado el primero positivo.

## Por qué ahora, y qué existe hoy

Los modelos pequeños cruzaron hace poco la línea de capacidad que hace esto posible; la brecha de ancho de banda que mató al reparto de modelos no se está cerrando. La oportunidad es de temporización.

Publicado y público a agosto de 2026: un whitepaper de 27 páginas con 90 referencias, una especificación completa del protocolo, una implementación de referencia con **178 pruebas en verde**, un corpus de evaluación etiquetado, un banco de pruebas que reporta sus propios fallos de medición, y las primeras mediciones reales completas. Todo bajo AGPL-3.0-or-later para que un despliegue alojado no pueda cerrarlo, con un registro de anterioridad fechado públicamente.

**Lo que necesita a continuación no es financiación primero: son participantes.** La forma más probable de que esto fracase no es un fallo de ingeniería; es que nadie se conecte. El cómputo voluntario lleva veinte años en declive, y el mejor protocolo del mundo no vale nada en una red vacía.

El conocimiento ya es público. El hardware ya está construido. Lo que faltaba es el protocolo, y ya está sobre la mesa, donde cualquiera puede revisarlo.

---

*Argumento técnico completo: `docs/WHITEPAPER_ES.md`. Versión divulgativa: `docs/DIVULGACION_ES.md`. Mediciones completas: `docs/RESULTS_V0_V3C.md`. Versión en inglés de esta página: `ONEPAGER_EN.md`.*
