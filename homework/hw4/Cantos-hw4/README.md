# DEBER 4-PAULO CANTOS- 326682 - 9/12/202 5

La creciente integración de sistemas de inteligencia artificial en procesos críticos ha convertido la
protección de datos personales en un pilar esencial para salvaguardar la seguridad jurídica y los
derechos fundamentales de los ciudadanos. En este contexto, la Ley Orgánica de Protección de Datos
Personales establece principios clave como La **legalidad**, la transparencia y la seguridad, que resultan
indispensables para regular el entrenamiento, el diseño y el despliegue de modelos algorítmicos.
Estos principios aseguran que la innovación tecnológica no comprometa la privacidad ni la
autodeterminación informativa de los titulares.
El presente informe organiza su análisis en torno a tres ejes fundamentales. En primer lugar, se
aborda el marco normativo ecuatoriano, con especial énfasis en el derecho a no ser objeto de
decisiones basadas exclusiva o parcialmente en procesos automatizados. Esta disposición impone a
las organizaciones la obligación de garantizar mecanismos de intervención humana significativa en
los sistemas de IA, especialmente cuando estos producen efectos jurídicos o impactan derechos
fundamentales. En segundo lugar, se examinan las políticas de tratamiento de datos adoptadas por
proveedores líderes del sector, diferenciando entre servicios dirigidos al consumidor y soluciones
empresariales. Este apartado permite evidenciar la tensión entre los mecanismos de exclusión
voluntaria y el principio de consentimiento informado exigido por la normativa vigente. Finalmente,
se identifican y analizan los principales riesgos técnicos y éticos asociados al uso de estas tecnologías,
como la reproducción de sesgos discriminatorios en sistemas de policía predictiva, la exposición de
información sensible a través de ataques de inyección de instrucciones, y la filtración involuntaria de
datos privados debido a la memorización no intencionada por parte de modelos de lenguaje.
El propósito de este documento es evaluar los desafíos de cumplimiento normativo y los riesgos
operativos que surgen en la convergencia entre la regulación local, las prácticas adoptadas por la
industria tecnológica y las vulnerabilidades inherentes al funcionamiento de los sistemas de
inteligencia artificial, sin anticipar conclusiones ni juicios previos sobre los hallazgos que se
desarrollan en el cuerpo del informe.

### Criterios mínimos de tratamiento de la LOPDP y su aplicación en IA

La Ley Orgánica de Protección de Datos Personales establece principios rectores que actúan como
criterios mínimos para cualquier operación de tratamiento de datos. En el contexto de la inteligencia
artificial, estos principios adquieren matices específicos para garantizar un desarrollo ético y legal. La
**legalidad** exige que el tratamiento de datos se realice conforme a la Constitución, la ley y las
normativas aplicables. En IA, esto significa que el entrenamiento y uso de modelos debe sustentarse
en fundamentos legales válidos como el consentimiento claro o el cumplimiento de una obligación
jurídica. El principio de **lealtad y transparencia** implica que el titular comprenda cómo se usan sus
datos. En IA, se requiere explicabilidad algorítmica, es decir, que el sistema sea transparente y que el
usuario sepa que interactúa con una inteligencia artificial, evitando usos desleales o ilícitos de sus
datos. La **finalidad** establece que los datos deben utilizarse para fines específicos, legítimos y
explícitos. En IA, impide que datos recopilados para un servicio concreto, como atención al cliente,
sean reutilizados sin autorización para otros fines, como entrenar modelos generales o vender
perfiles. La **pertinencia y minimización** exigen limitar el tratamiento a lo estrictamente necesario. En
IA, esto significa emplear la menor cantidad posible de datos personales, favoreciendo la
anonimización o el uso de datos sintéticos cuando sea viable. La **seguridad y confidencialidad**
requieren implementar medidas técnicas que protejan los datos frente a amenazas. En IA, esto
implica seguridad desde el diseño y por defecto en todas las fases: entrenamiento, calibración,
pruebas y despliegue. Finalmente, la **responsabilidad proactiva** obliga al responsable a demostrar el
cumplimiento de la normativa mediante mecanismos verificables. En IA, esto se traduce en
evaluaciones de impacto y auditorías algorítmicas para detectar riesgos o sesgos antes de poner el
sistema en funcionamiento.
### Derecho a no ser objeto de decisiones automatizadas

La LOPDP reconoce el derecho de las personas a no ser sometidas a decisiones basadas única o
parcialmente en procesos automatizados, incluyendo la elaboración de perfiles, cuando estas
decisiones tengan efectos jurídicos o afecten derechos fundamentales. Este derecho permite al
titular solicitar una explicación razonada de la decisión, presentar observaciones, impugnarla ante el
responsable, pedir información sobre los datos y los criterios utilizados por el sistema, y exigir la
intervención humana en la revisión de la decisión. No se aplica este derecho cuando la decisión es
necesaria para un contrato, está autorizada por ley o por orden judicial, se basa en el consentimiento
explícito o no causa impactos graves ni riesgos verificables. El responsable del tratamiento debe
informar expresamente al titular sobre este derecho desde la primera comunicación y no puede
exigir su renuncia mediante contratos de adhesión.
### Impacto operativo en sistemas de IA

Este derecho impone importantes restricciones operativas a los sistemas de IA, obligando a evitar la
automatización total en procesos críticos. Para que una decisión no se considere automatizada, la
intervención humana debe ser significativa, no simbólica. Debe realizarse por una persona con
autoridad y capacidad real para modificar el resultado. Si un humano aprueba de forma rutinaria lo

que recomienda el sistema sin análisis, sigue siendo una decisión automatizada. En procesos
sensibles como la contratación de personal o el otorgamiento de créditos, los sistemas de IA no
pueden operar autónomamente si generan consecuencias jurídicas o discriminatorias. Las
organizaciones deben implementar registros y procedimientos que garanticen la revisión o anulación
por parte de una persona. Está prohibido el uso de decisiones completamente automatizadas en
sectores sensibles, como el financiero o laboral, salvo que se cumplan las excepciones legales. Los
sistemas deben ser herramientas de apoyo, no decisores finales, para evitar la indefensión de los
titulares ante decisiones opacas o injustificadas.
### Restricciones a la transferencia internacional de datos

La transferencia internacional ocurre cuando se envían datos personales a un destinatario fuera del
país. La ley establece requisitos distintos según el nivel de protección del país receptor. Se permite la
transferencia a países o entidades reconocidas como con un nivel adecuado de protección. Si no
existe esta declaración, el responsable debe ofrecer garantías adecuadas, como cláusulas
contractuales estándar o instrumentos jurídicos vinculantes que aseguren la protección de los datos.
Los grupos empresariales pueden transferir datos internamente si cuentan con normas corporativas
aprobadas por la autoridad. También se permiten transferencias sin estos requisitos en ciertos casos
excepcionales, como el consentimiento explícito del titular informado sobre los riesgos, la necesidad
de cumplir un contrato, razones de interés público o la protección de intereses vitales del titular.
### Rol de la Autoridad de Protección de Datos y fricción operativa

La Superintendencia de Protección de Datos Personales es el organismo de control encargado de
supervisar el cumplimiento de la ley y sus regulaciones. Tiene funciones que impactan directamente
la operación de las empresas tecnológicas. Entre sus competencias está aprobar normas corporativas
vinculantes y códigos de conducta, autorizar transferencias internacionales en situaciones especiales
y mantener el registro nacional de protección de datos personales, en el que deben inscribirse tanto
los responsables como las transferencias internacionales. La autoridad también puede imponer
sanciones, ordenar el cese de actividades de tratamiento y aplicar multas si se incumple la
normativa. Para empresas extranjeras que tratan datos de residentes en Ecuador, existe la obligación
de registrar bases de datos, transferencias y designar un apoderado legal domiciliado en el país. Esto
genera una carga administrativa y legal significativa. Esta situación genera fricción operativa,
especialmente para proveedores de servicios en la nube que operan a nivel global, quienes deben
adaptar sus contratos y estructuras legales a las exigencias locales. La ausencia de una declaración
oportuna de países con nivel adecuado de protección complica el flujo ágil de datos, obligando a
recurrir a mecanismos alternativos como cláusulas contractuales o consentimientos individuales.

## 2. Gestión de Datos en Servicios de IA, Mecanismos de Control y Controversias Legales

### Comparación entre proveedores de IA: Servicios de consumo vs. empresariales

Al analizar las políticas de tratamiento de datos de proveedores líderes de inteligencia artificial como
OpenAI y Anthropic, se evidencia una distinción clara entre sus servicios dirigidos al consumidor
general y sus ofertas empresariales. En el caso de OpenAI, la empresa establece que el contenido
enviado por los usuarios a través de sus productos comerciales —como la API, ChatGPT Team y
ChatGPT Enterprise— no es utilizado para entrenar sus modelos. En cambio, en los servicios de
consumo estándar, como la versión gratuita de ChatGPT, la compañía emplea por defecto los datos
compartidos por los usuarios para mejorar el modelo, aunque ofrece opciones para desactivar esta
función. De manera similar, Anthropic, creador del modelo Claude, diferencia entre usuarios de
consumo (planes Free, Pro y Max) y usuarios comerciales (planes Team, Enterprise y API). Para estos
últimos, su política establece que no se utilizan indicaciones ni contenidos enviados bajo términos
comerciales para entrenar modelos, salvo que el cliente lo autorice explícitamente, por ejemplo,
mediante un programa de colaboración. En contraste, a partir de agosto de 2025, los usuarios de
consumo pueden optar por permitir que sus datos se utilicen para mejorar futuros modelos, política
que se aplica a conversaciones nuevas o reanudadas.
### Uso de datos para entrenamiento

En los servicios dirigidos al público general, los proveedores pueden utilizar distintas categorías de
información proporcionada por los usuarios para entrenar sus sistemas. En el caso de OpenAI, la
compañía conserva y analiza ciertos datos de las interacciones realizadas en su chatbot. Esto significa
que los modelos pueden alimentarse de la información compartida durante las conversaciones para
identificar patrones y mejorar el rendimiento del sistema. Por ejemplo, si un usuario proporciona una
imagen sensible como la fotografía de un menor, y tiene activada la opción de mejora del modelo,
esa imagen podría ser utilizada para el entrenamiento. Este proceso implica que los algoritmos de
aprendizaje automático ajusten sus parámetros internos a partir de los datos recibidos, lo cual les
permite mejorar la calidad de sus predicciones y respuestas automáticas.
### Proceso de exclusión (opt-out)

Con el fin de evitar que los datos personales sean empleados en el entrenamiento de modelos, los
proveedores ofrecen mecanismos de exclusión voluntaria. En el caso de ChatGPT, el procedimiento
consiste en ingresar a la cuenta del usuario, acceder a la configuración desde el perfil, dirigirse a la
sección de controles de datos, ubicar la opción denominada "Mejora el modelo para todos" y
desactivarla para que el contenido ya no sea utilizado. Finalmente, se debe confirmar el cambio. En
el caso de Google Gemini, el usuario debe acceder al apartado denominado "Actividad en las
aplicaciones de Gemini" y seleccionar la opción "Desactivar" o "Desactivar y eliminar actividad". Si

este paso no se realiza, Google puede conservar las conversaciones y utilizarlas para fines de revisión
y mejora de productos.
### Conflicto con la LOPDP: insuficiencia del mecanismo de exclusión

El sistema de exclusión voluntaria descrito presenta un conflicto directo con los principios de la Ley
Orgánica de Protección de Datos Personales. De acuerdo con esta normativa, todo tratamiento de
datos personales requiere el consentimiento del titular, el cual debe ser libre, específico, informado e
inequívoco. El problema radica en que el modelo de opt-out asume un consentimiento por defecto,
permitiendo el uso de datos sin que exista una manifestación previa de voluntad por parte del titular.
En estos casos, es el usuario quien debe tomar la iniciativa para revocar el tratamiento de datos, en
lugar de otorgar autorización de forma explícita antes de que comience. Esta lógica contradice el
estándar legal, que exige que el consentimiento sea una acción afirmativa clara, y establece que la
inacción, el silencio o las opciones activadas por defecto no constituyen una base válida para tratar
datos personales. Por lo tanto, cuando un proveedor inicia el uso de información sin un
consentimiento previo y explícito, está incumpliendo los principios de legalidad y lealtad previstos en
la LOPDP y en normas internacionales como el Reglamento General de Protección de Datos de la
Unión Europea.
### Caso legal o controversia reciente: Clearview AI

Un ejemplo emblemático sobre el uso indebido de inteligencia artificial y la vulneración del derecho
a la privacidad es el caso de Clearview AI. Esta empresa estadounidense ha enfrentado múltiples
denuncias y sanciones en Europa por crear una base de datos masiva de reconocimiento facial a
partir de la recolección automatizada de imágenes públicas. La empresa recopiló miles de millones
de fotografías de rostros humanos extraídas de redes sociales, sitios web y otras fuentes abiertas, sin
el consentimiento ni el conocimiento de los titulares. Luego, convirtió esas imágenes en
identificadores biométricos únicos, que eran ofrecidos como servicio de búsqueda y vigilancia a
fuerzas del orden y agencias gubernamentales. Este tratamiento generó fuertes cuestionamientos
legales. Las autoridades de protección de datos de países como Francia, Italia y los Países Bajos
impusieron multas millonarias al determinar que el uso de datos biométricos —considerados
información especialmente protegida— carecía de base legal y de transparencia. Además, la
organización NOYB presentó una denuncia penal en Austria alegando que la construcción de esta
base de datos representa una violación grave del derecho a la privacidad y de las disposiciones
establecidas en el Reglamento General de Protección de Datos. Este caso ilustra cómo el uso masivo
de información personal por parte de sistemas de inteligencia artificial, sin las salvaguardas
necesarias, puede derivar en sanciones legales severas y en un amplio rechazo social.

## 3. Riesgos de la Inteligencia Artificial en el Tratamiento de Datos Personales

### Aplicación de IA de alto riesgo: escenarios de daño severo y acceso no autorizado

Las aplicaciones de inteligencia artificial consideradas de alto riesgo son aquellas que pueden afectar
la seguridad, los derechos fundamentales o el bienestar de las personas, especialmente en sectores
críticos como la salud, la justicia o las infraestructuras esenciales. Un ejemplo preocupante es el
ataque conocido como "prompt injection", una técnica que busca manipular modelos de lenguaje
mediante la inserción de instrucciones maliciosas ocultas en los datos de entrada. Este tipo de
ataque puede forzar al sistema a ignorar sus normas de seguridad internas. En contextos sensibles,
como el sector bancario o el sanitario, un atacante podría lograr que un asistente virtual revele
información confidencial, realice transacciones no autorizadas o proporcione datos falsos, todo sin
activar las defensas tradicionales de ciberseguridad. Además, el uso no regulado de herramientas de
IA por parte de empleados, fenómeno conocido como "Shadow AI", incrementa significativamente
los riesgos. Cuando los trabajadores utilizan estas tecnologías sin supervisión del área de TI, se
expone información confidencial y propiedad intelectual, ampliando la superficie de ataque sin los
controles necesarios para su mitigación.
### Policía predictiva y sesgos históricos

El uso de inteligencia artificial en sistemas de policía predictiva plantea serias preocupaciones éticas
y legales debido al riesgo de discriminación algorítmica. Estos sistemas suelen entrenarse con datos

estudios han demostrado que estas herramientas tienden a recomendar un despliegue policial más
intensivo en barrios habitados mayoritariamente por personas negras, latinas o de bajos ingresos, no
necesariamente por ser zonas con mayor criminalidad, sino porque han sido históricamente más
vigiladas. Esto genera un ciclo de retroalimentación en el cual la mayor presencia policial produce
más registros de incidentes, reforzando el sesgo del algoritmo y perpetuando la estigmatización. Esta
práctica vulnera varios principios fundamentales. La utilización de datos distorsionados, conocidos
como "datos sucios", compromete la calidad del tratamiento, mientras que el principio de lealtad se
ve afectado porque las decisiones basadas en estos datos resultan injustas para ciertos grupos.
Además, al utilizar perfiles probabilísticos en lugar de hechos concretos, se pone en entredicho la
presunción de inocencia.
### Memorización del modelo y fuga de privacidad

Una de las vulnerabilidades más críticas en los modelos de inteligencia artificial es el fenómeno
conocido como memorización del modelo o fuga de privacidad. Esta situación ocurre cuando el
sistema retiene y reproduce información confidencial que ha sido parte de su conjunto de

entrenamiento. Si un modelo ha sido expuesto a datos personales, como historiales médicos,
secretos comerciales o identificadores individuales, es posible que, bajo ciertos prompts diseñados
estratégicamente, reproduzca esa información textualmente. Esto se conoce como ataque de
inferencia. La gravedad de este problema radica en que transforma al propio modelo en un canal de
exposición de datos privados, representando una violación directa al principio de confidencialidad.
En entornos donde se espera una protección estricta de la información, esta capacidad de los
modelos para recordar datos sensibles representa un riesgo operativo y legal significativo.
### Violación de derechos bajo la LOPDP en entornos sanitarios

El uso de inteligencia artificial en instituciones de salud plantea riesgos específicos en relación con la
Ley Orgánica de Protección de Datos Personales. Si un chatbot interno revela información sensible de
pacientes debido a una falla de seguridad o una alucinación del modelo, se estarían vulnerando
derechos fundamentales. En primer lugar, se compromete la protección de los datos de salud,
considerados como datos sensibles cuya utilización está prohibida salvo bajo condiciones muy
estrictas. También se infringe el principio de confidencialidad, que obliga a garantizar el sigilo incluso
después de terminada la relación entre el responsable del tratamiento y el titular de los datos.
Asimismo, se vulnera el principio de seguridad, que exige implementar medidas técnicas y
organizativas adecuadas para prevenir accesos no autorizados o filtraciones de datos. Ante una
vulneración de este tipo, la ley obliga a notificar el incidente tanto a la autoridad de protección de
datos como a la ARCOTEL en un plazo máximo de cinco días. Además, si el incidente representa un
riesgo para los derechos del paciente, se debe informar directamente al titular afectado en un plazo
de tres días. El incumplimiento de estas obligaciones puede derivar en sanciones administrativas
severas, incluyendo multas proporcionales al volumen de negocio del responsable.
### Ejemplos reales de incidentes

Diversos casos recientes ilustran la materialización de los riesgos descritos. Clearview AI, por
ejemplo, desarrolló una base de datos de reconocimiento facial extrayendo miles de millones de
imágenes de redes sociales sin obtener el consentimiento de los titulares. Fue sancionada en varios
países europeos por procesar datos biométricos de forma ilegal y violar derechos de privacidad. Otro
caso es el de PredPol, una herramienta de predicción delictiva utilizada en ciudades como Plainfield,
Nueva Jersey. Investigaciones revelaron que el sistema recomendaba patrullajes desproporcionados
en barrios con alta presencia de minorías, perpetuando patrones de discriminación racial, pese a que
la empresa aseguraba que el algoritmo era neutral. Finalmente, se han registrado incidentes
relacionados con la fuga de información confidencial a través del uso irresponsable de herramientas
de IA generativa en entornos corporativos. Un ejemplo destacado es el de empleados de Samsung
que introdujeron código propietario en plataformas públicas, exponiendo secretos comerciales sin

control institucional. Este tipo de prácticas, impulsadas por el uso no autorizado de IA por parte de
empleados, refleja los peligros del fenómeno conocido como Shadow AI y destaca la urgencia de
establecer políticas claras y mecanismos de supervisión efectiva.

El análisis integral de la normativa ecuatoriana y la operatividad de los sistemas de Inteligencia
Artificial (IA) revela una tensión significativa entre las garantías jurídicas locales y las prácticas
globales de la industria tecnológica. Si bien la Ley Orgánica de Protección de Datos Personales
(LOPDP) establece salvaguardas robustas —como la prohibición de decisiones puramente
automatizadas y la exigencia de un consentimiento libre e informado—, estas entran en conflicto con
las políticas de uso de datos de los principales proveedores de IA, cuyos modelos de consumo suelen
basarse en mecanismos de exclusión voluntaria ( opt-out ) y en la reutilización de información para
entrenamiento, contraviniendo el principio de finalidad.
A esta fricción normativa se suman vulnerabilidades técnicas críticas, como el riesgo de filtración de
datos por memorización del modelo ( data leakage ) y la perpetuación de sesgos discriminatorios en
sistemas predictivos. Para el despliegue de IA en Ecuador, esto implica que las organizaciones no
pueden depender pasivamente de las configuraciones predeterminadas de los proveedores; deben
implementar controles estrictos sobre la transferencia internacional de datos y garantizar la
seguridad desde el diseño para evitar sanciones y daños reputacionales.
En definitiva, la adopción de estas tecnologías exige una gobernanza que priorice la supervisión
humana significativa sobre la eficiencia automatizada. Solo mediante una responsabilidad proactiva
que audite la opacidad algorítmica y asegure la intervención humana en procesos con efectos
jurídicos, será posible armonizar la innovación tecnológica con el respeto irrestricto a los derechos
fundamentales y la autodeterminación informativa de los titulares.

## Bibliografía:

- Agencia Española de Protección de Datos (AEPD). (2024, 4 de marzo). Evaluación de la intervención humana en las decisiones automatizadas. AEPD.
- Allende & Brea. (2025, 29 de octubre). La DPA de Ecuador impulsa regulación de inteligencia artificial. Estudio Jurídico Allende & Brea.
- Anthropic. (s.f.). Uso de datos. Claude Code Docs.
- Asamblea Nacional del Ecuador. (2021). Ley Orgánica de Protección de Datos Personales. Registro Oficial Suplemento 459.
- AVL Abogados. (2025, 25 de julio). Normativa para la transferencia nacional e internacional de datos personales.
- Castellanos, M. P. (2022, 12 de septiembre). Lo que debería saber sobre la transferencia internacional de datos personales en Ecuador. Datos Personales Latinoamérica.
- Computing. (2025, 1 de julio). La fuga de datos aumenta debido al uso de la inteligencia artificial generativa.
- Cooperativa de Ahorro y Crédito 29 de Octubre Ltda. (2024). Manual Sistema de Protección de Datos Personales (Versión 2.00).
- Dirección Nacional de Registros Públicos (DINARP). (2021). Ley de Protección de Datos Personales. Gobierno de la República del Ecuador.
- Durán, S. (2025, 2 de octubre). Reglamento de protección de datos en uso de IA en Ecuador puede frenar innovación: industria. DPL News.
- Durán San Juan, I. (2025, 9 de diciembre). Evita que ChatGPT use tus datos privados para entrenar su IA. Infobae.
- Ediciones Legales. (2025). Política de tratamiento de datos personales.
- Fair Trials. (2024). Inteligencia artificial en la seguridad pública y en el sistema penal en América Latina: Análisis basado en el debido proceso.
- Flores Miranda, M. (2024, 13 de septiembre). Implicaciones de la Ley de Protección de Datos Personales en Ecuador. Delete Technology.
- García Ureña, J. A. (2025, 26 de febrero). UE AI Act (#3). IA de alto riesgo: ¿qué sistemas deben cumplir más requisitos? AI Health.
- Gil, F., Moraes, A., & Tift, W. (2025). Chatbot para la educación: un asistente conversacional sobre inteligencia artificial [Informe de Proyecto de Grado]. Universidad de la República, Facultad de Ingeniería.
- Google Cloud. (s.f.). Transparencia y protección de datos.
- Grupo Decisión. (2024). Política de Protección de Datos Personales (Versión V.2).
- Hart, R. (2024, 5 de septiembre). Multa de 30 millones: el escándalo detrás de la base de datos ilegal de rostros. Forbes Argentina.
- López Riba, J. M. (2024). Inteligencia artificial y control policial: Cuestiones para un debate frente al hype. InDret, 2.
- Ministerio de Salud Pública del Ecuador. (2020, 13 de agosto). Comunicado: Legislación prohíbe divulgación de datos personales.
- Piray-Rodríguez, P. O., Narváez-Montenegro, B. D., Falconí-Cárdenas, L. M., & Naranjo-Luzuriaga, E. J. (2025). Análisis de la normativa relacionada con seguridad y privacidad de datos personales en universidades ecuatorianas. Verdad y Derecho: Revista Arbitrada de Ciencias Jurídicas y Sociales, 4 (Especial), 293-312.
- SentinelOne. (2025). Los 14 principales riesgos de seguridad de la IA en 2025.
- Superintendencia de Protección de Datos Personales. (2024). Resolución Nº SPDP-SPDP- 2024 - 0002 - R: Guía técnica obligatoria para el registro de los apoderados especiales de responsables, conjuntos o no, y encargados extranjeros.
- Superintendencia de Protección de Datos Personales. (2025). Normativa General para la Garantía del Derecho de Protección de Datos Personales en el Uso de Inteligencia Artificial [Proyecto de Resolución].
- Vergara, A. (2025, 18 de septiembre). Seguridad de IA en la banca: La hoja de ruta esencial. Pragma.






