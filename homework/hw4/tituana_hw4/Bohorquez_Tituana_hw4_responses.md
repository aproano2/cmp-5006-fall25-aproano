# Homework 4 - Respuestas
## Andrés Bohórquez, Gian Tituaña


## 1. Foundational Research: Ecuadorian Data Sovereignty (LOPDP)

### Los tres principios centrales (criterios mínimos) de la LOPDP   

1. Legalidad: El tratamiento debe estar amparado en una base normativa o mandato legal claro (Art. 10).
2. Proporcionalidad: El tratamiento debe ser adecuado, necesario, oportuno, relevante y no excesivo en relación con las finalidades perseguidas (Art. 10).
3. Necesidad: El tratamiento debe limitarse a lo estrictamente indispensable para cumplir la finalidad (Art. 10).
---
### Número de artículo y explicación del derecho ante valoraciones automatizadas

El derecho específico del titular a no ser objeto de una decisión basada únicamente en valoraciones automatizadas se encuentra en el Artículo 20 de la LOPDP.

Este artículo protege al ciudadano frente a decisiones tomadas por algoritmos o procesos automáticos (incluida la elaboración de perfiles) que generen efectos jurídicos o atenten contra sus derechos fundamentales. Las protecciones específicas que otorga este derecho permiten al titular:
- Solicitar una explicación motivada sobre la decisión tomada.
- Presentar observaciones respecto a la decisión.
- Solicitar los criterios de valoración utilizados por el programa automatizado.
- Conocer los tipos de datos utilizados y la fuente de donde se obtuvieron.
- Impugnar la decisión ante el responsable o encargado del tratamiento.
---
### Impacto operativo de este derecho en sistemas impulsados por IA

El Artículo 20 impone obligaciones operativas significativas al responsable del tratamiento (la empresa):

- Obligación de Explicabilidad: La empresa no puede utilizar modelos de "caja negra". Si un sistema de IA deniega un crédito, la por ley puedes exigir una "explicación motivada" y los "criterios de valoración". De manera que la empresa debe tener sistemas que permitan rastrear por qué la IA tomó esa decisión específica.
- Intervención Humana Obligatoria: La disposición obliga al responsable a proveer supervisión humana a través del derecho de impugnación. Si el usuario impugna la decisión automática, la empresa debe tener un proceso donde un humano revise el resultado.
- Transparencia de Datos: Operativamente, la empresa debe estar preparada para revelar qué datos específicos alimentaron la decisión de la IA y de dónde provinieron (fuentes).
---
### Condiciones de la LOPDP para la transferencia internacional de datos personales

1. Nivel Adecuado de Protección: Se permite la transferencia a países u organizaciones internacionales que hayan sido declarados por la Autoridad de Protección de Datos como territorios que ofrecen niveles de protección adecuados y estándares internacionales (Art. 56).
2. Garantías Adecuadas: Si el país de destino no tiene una declaración de adecuación, se puede transferir si el responsable ofrece garantías de que se cumplirán los derechos y principios de la LOPDP, incluyendo la posibilidad de reclamación y reparación integral para el titular. (Art. 57).
3. Normas Corporativas Vinculantes: Grupos empresariales pueden aprobar normas internas autorizadas por la Autoridad para regular transferencias intragrupo (Art. 58).
4. Excepciones Específicas: En ausencia de lo anterior, se permiten transferencias en casos puntuales como: cumplimiento de contratos, consentimiento explícito del titular (tras ser informado de los riesgos), interés público, cooperación judicial, operaciones bancarias/bursátiles, o protección de intereses vitales (Art. 60).
---
### Rol de la Data Protection Authority (DPA) y fricción operativa para multinacionales de IA

La Autoridad tiene un rol centralizado de control y autorización:
- Emitir resoluciones motivadas declarando qué países tienen un nivel adecuado de protección (Art. 56).
- Autorizar las transferencias internacionales que no se encuadren en los mecanismos estándar (Art. 59).
- Gestionar el Registro Nacional de Protección de Datos Personales, donde deben registrarse previamente las informaciones sobre transferencias internacionales (Art. 59).
- Realizar un control continuo y puede revocar la adecuación de un país, prohibiendo transferencias futuras (Art. 61).

 Para una empresa multinacional de IA que utiliza infraestructura de nube centralizada, este esquema crea varias barreras:
1. Carga Burocrática de Registro: La información sobre transferencias internacionales de datos personales deberá ser registradas previamente en el Registro Nacional, lo cual obliga a la empresa a reportar sus flujos de datos antes de operar (Art. 59).
2. Incertidumbre de "Listas Blancas": Si los servidores de la empresa están en un país que Ecuador aún no ha declarado como "adecuado", la empresa debe recurrir a solicitar autorizaciones específicas o implementar garantías contractuales complejas (Art. 56, 57, 59).
3. Riesgo de Interrupción: La facultad de la Autoridad para realizar controles ex post y suspender transferencias si un país deja de ser seguro, crea un riesgo operativo donde el flujo de datos vital para el entrenamiento o inferencia de la IA podría ser legalmente cortado de un día para otro (Art. 56, 61).
---

## 2. Corporate Policy Scrutiny: The Data Repurposing Conflict

### Pricipales proveedores de IA generativa: OpenAI  y Anthropic
Tanto OpenAI como Anthropic establecen políticas distintas para el uso de datos según el tipo de servicio. En general:

- Servicios Empresariales/API (clientes pagos): los datos no se usan para entrenar modelos por defecto.

- Servicios para Consumidores (chatbots gratuitos o personales): los datos sí pueden usarse para entrenamiento, dependiendo de la empresa y de la configuración de consentimiento.

#### OpenAI
**Servicios de Consumidor (ChatGPT gratuito y versiones personales)**

OpenAI afirma que las conversaciones con sus usuarios podrían ser usados para perfeccionar sus modelos.

ChatGPT "se perfecciona mediante el entrenamiento con las conversaciones de los usuarios, salvo que estos se excluyan manualmente".

Los usuarios individuales pueden desactivar el empleo de sus chats para entrenamiento en la configuración de privacidad.

**Servicios Empresariales/API (ChatGPT Enterprise, Team, API)**

OpenAI especifica claramente que no entrena sus modelos con los datos enviados por clientes de negocio por defecto.

La política indica que no entrena sus modelos con las entradas o salidas de sus productos para usuarios empresariales los cuales incluyen ChatGPT Team, Enterprise y el API.

El cliente empresarial está  excluido del uso de datos para entrenamiento, a menos que otorgue un consentimiento explícito (por ejemplo, enviando retroalimentación).


#### Anthropic
**Servicios de Consumidor (Claude Free / Pro / Max)**

Anthropic usa un sistema de opt-in, es decir,
los usuarios pueden permitir el uso de sus chats para entrenamiento si aceptan explícitamente.

En caso de que el usuario otorgue consentimiento, sus conversaciones y sus sesiones de programación pueden usarse para mejorar futuros modelos.

También tiene un modo “incógnito”, donde los chats nunca se usan para entrenar.

**Servicios Empresariales/API (Claude for Work, Claude API, Government, Education)**

Anthropic indica que no usa datos de clientes comerciales para entrenar modelos.

De acuerdo a sus políticas dicen que para “productos comerciales no usaremos sus entradas o salidas para entrenar modelos”.

Las reglas de opt-in no aplican a estos servicios empresariales: Claude for Work, Government, Education y API quedan excluidos del uso para entrenamiento por defecto.

---

### Análisis de Políticas Públicas: OpenAI (ChatGPT)

**Tipos de datos de entrada del usuario que pueden usarse para entrenamiento del modelo:**

Para este ejercicio revisé la política pública de OpenAI dirigida a usuarios de la versión de consumo de ChatGPT. A partir de su documentación identifiqué que la empresa recopila distintos tipos de datos que pueden ser utilizados para entrenar y mejorar sus modelos (OpenAI, 2024). Los principales son:

1. **Contenido de las conversaciones (Chat Content):**
   - Todos los mensajes enviados por el usuario (prompts)
   - El contexto completo de las conversaciones
   - Archivos adjuntos y contenido multimedia compartido durante la sesión

2. **Información de cuenta (Account Information):**
   - Dirección de correo electrónico
   - Nombre de usuario y preferencias del perfil
   - Historial de uso y patrones de interacción

3. **Datos técnicos (Technical Data):**
   - Dirección IP y ubicación geográfica aproximada
   - Tipo de dispositivo, navegador y sistema operativo
   - Marcas de tiempo de las sesiones
   - Datos de rendimiento y logs de error
   - Cookies y tokens de sesión

OpenAI también aclara que existen diferencias entre planes gratuitos y de pago. En los planes Plus, Team y Enterprise, los datos no se usan para entrenamiento por defecto, mientras que en la versión gratuita sí se utilizan salvo que el usuario realice el proceso de exclusión manualmente (OpenAI, 2024).

---

### Proceso Práctico de Opt-Out (Exclusión del Entrenamiento)

Durante mi investigación identifiqué que OpenAI sí ofrece un mecanismo para evitar que los datos del usuario sean usados para entrenar modelos, aunque no está presentado de manera especialmente destacada. Los pasos son:

**1. Acceder a Configuración**
- Iniciar sesión en ChatGPT
- Abrir Settings desde el menú del perfil

**2. Ir a la sección de datos**
- Ingresar a Data Controls
- Buscar Chat History & Training

**3. Desactivar el uso de datos**
- Apagar el interruptor "Improve the model for everyone"
- Esto también desactiva el historial de chats

**4. Confirmar la acción**
- El sistema muestra una advertencia indicando que:
  - El historial dejará de guardarse
  - Los nuevos datos no se usarán para entrenamiento

**Alternativa:**
- Existe un formulario de exclusión más formal, que OpenAI procesa en un plazo aproximado de 30 días

**Limitaciones prácticas:**
- La exclusión no es retroactiva (los datos previos pueden haber sido usados ya)
- El usuario debe renunciar a su historial para ejercer este derecho
- No hay granularidad: es una opción "todo o nada"

---

### Evaluación Crítica: Conflicto con el Mandato de la LOPDP

Al comparar este mecanismo con la LOPDP ecuatoriana (2021), encontré varios conflictos importantes:

#### **1. Opt-out vs. consentimiento previo**

**Mandato LOPDP:**
La LOPDP exige consentimiento previo, libre, informado y expreso (art. 8).

**Práctica de OpenAI:**
OpenAI procesa datos por defecto y el usuario debe desactivar manualmente esta opción, lo cual invierte la lógica exigida por la ley.

**Conflicto identificado:** Esta práctica contradice directamente el principio de consentimiento previo establecido en la LOPDP (2021, art. 8), ya que el procesamiento de datos comienza automáticamente sin que el usuario haya otorgado autorización explícita previamente.

#### **2. Información poco clara o poco visible**

**Mandato LOPDP:**
La LOPDP exige transparencia previa (art. 10).

**Práctica de OpenAI:**
Sin embargo, observé que:
- La información está dispersa en documentos extensos
- El sistema no avisa claramente al usuario nuevo que sus datos alimentan modelos comerciales
- El opt-out no se muestra de manera destacada

**Conflicto identificado:** OpenAI no cumple con el requisito de información "previa y clara" que exige la LOPDP (2021, art. 10), ya que la información relevante está dispersa en documentos legales extensos y no se presenta de forma prominente al usuario.

#### **3. Falta de consentimiento específico**

**Mandato LOPDP:**
La LOPDP exige que el consentimiento sea otorgado para finalidades concretas y determinadas (art. 51).

**Práctica de OpenAI:**
Expresiones como "improve the model" no explican suficientemente:
- Qué modelos se entrenan
- Para qué fines específicos
- Si habrá futuros usos comerciales
- Si habrá transferencia a terceros

**Conflicto identificado:** El lenguaje vago utilizado por OpenAI no cumple con el estándar de finalidad específica de la LOPDP (2021, art. 51).

#### **4. Consentimiento condicionado**

**Mandato LOPDP:**
El consentimiento debe ser dado libremente, sin condicionamientos que limiten el ejercicio de derechos (art. 8).

**Práctica de OpenAI:**
Para ejercer su derecho a no ser entrenado, el usuario debe perder el historial de chats.

**Conflicto identificado:** Esto crea una situación en la que la privacidad implica renunciar a una función básica, lo cual afecta la libertad de consentimiento establecida en la LOPDP (2021, art. 8).

#### **5. Reutilización de datos para nuevas finalidades**

**Mandato LOPDP:**
Los datos solo pueden usarse para las finalidades para las que fueron recolectados (art. 51).

**Práctica de OpenAI:**
El uso original del dato es "proveer servicio de chat", pero luego se reutiliza para "entrenamiento".

**Conflicto identificado:** La LOPDP exige consentimiento nuevo para usos secundarios (2021, art. 51), lo cual no ocurre aquí. OpenAI viola directamente el principio de limitación de finalidad.

#### **Conclusión de esta sección**

En términos generales, el modelo opt-out de OpenAI contradice varios principios centrales de la LOPDP. Mientras que la ley ecuatoriana coloca la carga de protección en el responsable del tratamiento (requiriendo autorización activa previa), el sistema de OpenAI traslada esta carga al usuario (requiriendo exclusión activa posterior).

Para cumplir plenamente la ley ecuatoriana, OpenAI debería solicitar consentimiento explícito antes de usar los datos para entrenamiento, separar claramente finalidades y no condicionar funciones del producto a la cesión de datos.

---

### Escenario de Riesgo Legal: Caso Meta y el Uso de Datos Biométricos

#### **Caso: Meta (Facebook/Instagram) y el Escándalo de Datos Biométricos - Illinois (2023-2024)**

**Contexto del Caso:**

Para este literal analicé el caso de Meta (Facebook/Instagram) relacionado con el uso de datos biométricos sin consentimiento informado. En 2023–2024 la empresa enfrentó múltiples demandas en Estados Unidos por utilizar características faciales de fotos de usuarios para entrenar sistemas de reconocimiento facial sin autorización explícita (Rosenblatt, 2024).

**Naturaleza de la violación alegada:**

- Meta usó fotografías subidas por usuarios con fines sociales para derivar plantillas biométricas
- Las utilizó para entrenar sistemas de reconocimiento facial y etiquetado automático
- No informó claramente sobre esta finalidad
- Usuarios etiquetados en fotografías de terceros también fueron afectados sin haber dado consentimiento

Estos datos son extremadamente sensibles, y la falta de consentimiento informado fue considerada una violación de la Biometric Information Privacy Act (BIPA) en Illinois.

**2. Tipo de Datos Involucrados:**
- **Datos Biométricos:** Geometría facial, mapas de características faciales únicas
- **Metadatos de Imágenes:** Ubicación GPS, timestamps, dispositivos usados
- **Datos de Comportamiento:** Patrones de interacción, círculos sociales inferidos de fotos grupales
- **Contenido Generado por Usuarios:** Millones de fotos y videos subidos a la plataforma

**3. Violación Específica de Privacidad Biométrica:**

El caso se centró en la violación de la **Biometric Information Privacy Act (BIPA)** de Illinois, que tiene paralelismos importantes con los principios de la LOPDP:

- **Falta de Consentimiento Informado:** Meta activó por defecto la función "Tag Suggestions" que usaba reconocimiento facial, sin solicitar autorización explícita
- **No Divulgación de Propósito:** No informó claramente que los datos biométricos serían:
  - Almacenados indefinidamente
  - Usados para entrenar modelos comerciales de IA
  - Potencialmente compartidos con terceros o subsidiarias
- **Ausencia de Política de Retención:** No estableció ni comunicó plazos para eliminar los datos biométricos
- **Imposibilidad de Exclusión Efectiva:** Incluso usuarios que no habían activado la función fueron procesados cuando aparecían en fotos de terceros

**Resultados legales:**

- **Acuerdo de $650 millones (2023)** (Hill, 2023)
- **Acuerdo adicional de $1.4 mil millones (2024)** (Rosenblatt, 2024)
- **Eliminación obligatoria de plantillas biométricas**
- **Eliminación del sistema de etiquetado automático basado en IA**

**Paralelo con la LOPDP:**

Bajo la ley ecuatoriana, esta práctica también habría sido problemática debido a:

- **Art. 5:** Los datos biométricos son datos sensibles
- **Art. 51:** Prohibición de uso para finalidades distintas sin nuevo consentimiento
- **Art. 8:** Requisito de consentimiento previo
- **Art. 66:** Reglas estrictas para datos sensibles

**5. Implicaciones para Empresas de IA:**

Este caso establece precedentes importantes:

- **Reprocesamiento requiere nuevo consentimiento:** No se puede asumir que el consentimiento para una funcionalidad incluye consentimiento para entrenamiento de IA
- **Datos biométricos requieren protección especial:** Su naturaleza inmutable y sensible exige estándares más altos
- **Opt-out no es suficiente:** Especialmente para datos sensibles, se requiere opt-in activo
- **Sanciones económicas significativas:** Las multas pueden ser devastadoras, calculadas por cantidad de violaciones individuales

**Conclusión:**

Esto demuestra el riesgo legal de reutilizar datos para nuevas finalidades sin consentimiento explícito. Bajo el marco de la LOPDP ecuatoriana, estas prácticas constituirían violaciones aún más graves, con potenciales sanciones de hasta el 4% de los ingresos anuales globales (LOPDP, 2021, art. 92).

---

## 3. Technical Risk Assessment and Mitigation

### Aplicación de Alto Riesgo: Sistema de Evaluación Crediticia con IA

**Escenario Detallado:**

Imaginé un sistema bancario llamado "CréditoInteligente", que usa datos personales, comportamiento digital y análisis de textos para tomar decisiones crediticias automatizadas. El sistema analiza:

- Historial crediticio tradicional
- Comportamiento en redes sociales (mediante scraping)
- Patrones de consumo de e-commerce
- Datos de ubicación y movilidad (mediante apps bancarias)
- Análisis de lenguaje de comunicaciones previas con el banco

**Riesgos identificados:**

1. **Exclusión financiera basada en sesgos históricos**
2. **Uso de datos sensibles inferidos (política, religión, salud)**
3. **Fuga o exposición de datos altamente sensibles**
4. **Decisiones opacas sin explicabilidad**
5. **Retroalimentación de errores (feedback loops)**

**3. Fuga de Datos y Acceso No Autorizado:**
- El modelo centraliza información altamente sensible de miles de clientes
- Resultado potencial: Brecha de seguridad expone:
  - Perfiles financieros completos
  - Patrones de comportamiento personal
  - Información de salud inferida
  - Datos de ubicación históricos
- Daño: Exposición a robo de identidad, fraude, extorsión, y discriminación por terceros

**4. Decisiones Opacas Sin Explicación:**
- Los clientes rechazados no reciben explicación comprensible del porqué
- Resultado: Imposibilidad de ejercer el derecho de rectificación o impugnación
- Daño: Violación del Art. 23 de la LOPDP (derecho a conocer el origen y destino de datos personales) y Art. 53 (derecho a no ser objeto de decisiones automatizadas)

**5. Model Drift y Errores Cascada:**
- El modelo se entrena continuamente con decisiones propias (feedback loop)
- Resultado: Errores iniciales se amplifican; el modelo se vuelve progresivamente más sesgado
- Daño: Degradación de calidad decisional afecta a población más amplia con el tiempo

**Medidas de mitigación:**

1. **Evaluación de Impacto (EIPD)** obligatoria antes del despliegue (LOPDP, 2021, art. 47)
2. **Auditorías periódicas** para detectar sesgos
3. **Explicabilidad obligatoria** en decisiones
4. **Revisión humana** en todos los rechazos
5. **Minimización de datos**
6. **Controles de seguridad reforzados**

---

### Análisis del Sistema de Policiamiento Predictivo

**Contexto del Escenario:**

Imaginé un sistema llamado "GuardianIA" que predice zonas de riesgo usando datos históricos (Introna & Wood, 2004). La ciudad de Guayaquil lo implementa para:
- Predecir "zonas calientes" (hotspots) de criminalidad
- Asignar patrullaje preventivo a áreas de mayor riesgo
- Identificar individuos con "alta probabilidad de reincidencia"
- Priorizar investigaciones basadas en "perfiles de riesgo"

**Datos de Entrenamiento Utilizados:**

1. Reportes policiales históricos (2010-2024)
2. Datos de arrestos y detenciones
3. Información sociodemográfica de barrios
4. Llamadas al 911
5. Datos de redes sociales (monitoreo público)

**Problema de Sesgo Histórico:**

En este caso, encontré que los sesgos acumulados por años de prácticas policiales generan un efecto de reproducción de desigualdad (O'Neil, 2016).

**Problemas principales:**

- **Sobre-vigilancia de barrios marginales:** Comunidades de bajos ingresos y con mayor población afrodescendiente o indígena históricamente han tenido mayor presencia policial
- **Resultado:** Más arrestos registrados en estas zonas, no porque haya más crimen real, sino porque hay más policías observando
- **El modelo aprende:** "Alta criminalidad = barrios pobres/étnicamente diversos"

- **Sub-reporte en zonas affluentes:** Delitos económicos, violencia doméstica en barrios de clase alta son menos reportados o investigados
- **Resultado:** El modelo no asocia estos barrios con criminalidad
- **Consecuencia:** Estos barrios reciben menos patrullaje incluso si el crimen per cápita es similar

**Profécías autocumplidas (feedback loops):**

El sistema genera profecías autocumplidas (O'Neil, 2016): más patrullaje → más arrestos → más "riesgo" predicho → más patrullaje.

**Impacto Discriminatorio en Comunidades Marginalizadas:**

**1. Vigilancia Desproporcionada:**
- Residentes de barrios marginales son parados, interrogados y revisados con mayor frecuencia
- Impacto psicológico: Sensación de estar constantemente vigilados
- Estigmatización comunitaria: El barrio entero es marcado como "criminal"

**2. Registros Criminales Inflados:**
- Más vigilancia = más arrestos por delitos menores (posesión de drogas, desorden público)
- Jóvenes de estas comunidades acumulan antecedentes penales
- Impacto a largo plazo: Dificultad para conseguir empleo, educación, vivienda

**3. Perfilamiento Racial y Socioeconómico:**
- El sistema identifica correlaciones entre:
  - Etnia + Ubicación geográfica + Nivel socioeconómico = "Alto riesgo"
- Aunque el modelo no use explícitamente "raza" como variable, la aprende implícitamente (proxy variables)
- Resultado: Discriminación algorítmica sistemática

**4. Negación de Servicios de Protección Equitativos:**
- Barrios de clase alta reciben menos patrullaje preventivo
- Violación del principio de igualdad ante la ley
- Las comunidades marginales son tratadas como "zonas de contención" no como ciudadanos a proteger

**Violaciones a la LOPDP:**

**1. Principio de Proporcionalidad (Art. 52)**

El tratamiento de datos debe ser adecuado, pertinente y proporcional (LOPDP, 2021, art. 52). La afectación de derechos (vigilancia intensiva, estigmatización) es desproporcionada al beneficio alegado.

**2. Derecho a Oponerse a Decisiones Automatizadas (Art. 53)**

Los ciudadanos no son notificados ni tienen mecanismos para impugnar clasificaciones (LOPDP, 2021, art. 53). Las decisiones afectan derechos fundamentales sin debido proceso.

**3. Calidad de Datos (Art. 50)**

Los datos históricos están contaminados con sesgos, omiten criminalidad no reportada en zonas affluentes, y perpetúan patrones obsoletos (LOPDP, 2021, art. 50).

**4. Datos Sensibles (Art. 5 y 66)**

Aunque no use explícitamente "etnia", la ubicación y características socioeconómicas son proxies. Esto constituye tratamiento indirecto de datos sensibles sin justificación legítima (LOPDP, 2021, art. 5, 66).

**Efectos Legales Discriminatorios:**

**1. Violación de Garantías Constitucionales:**
- **Art. 11.2 Constitución del Ecuador:** Prohibición de discriminación por etnia, lugar de nacimiento, condición socioeconómica
- **Art. 66.4:** Derecho a la igualdad formal, material y no discriminación
- El sistema genera discriminación algorítmica sistemática

**2. Violación del Debido Proceso:**
- Ciudadanos son sometidos a vigilancia intensiva sin:
  - Notificación
  - Oportunidad de defensa
  - Revisión judicial
  - Presunción de inocencia

**3. Impacto en Presunción de Inocencia:**
- Comunidades enteras son tratadas como "criminales potenciales"
- Inversión de la carga de la prueba: deben "demostrar" que no son peligrosos

**Medidas necesarias:**

1. **Auditoría de sesgos** obligatoria
2. **Notificación y mecanismos de apelación**
3. **Eliminación de variables proxy**
4. **Intervención humana** obligatoria
5. **EIPD previa** (LOPDP, 2021, art. 47)

**Conclusión:**

Los sesgos en datos históricos no son "errores estadísticos" sino reflejos de discriminación sistemática (O'Neil, 2016). El sistema violaría principios de proporcionalidad, calidad de datos, y no discriminación de la LOPDP.

---

### Model Memorization y Data Leakage en IA Generativa

**Definición general:**

**Memorization:** El modelo retiene fragmentos exactos del entrenamiento (Carlini et al., 2021)

**Data leakage:** El modelo revela esos fragmentos en sus respuestas

**Mecanismo Técnico:**
- Durante el entrenamiento, el modelo ve ciertos fragmentos de texto múltiples veces
- En lugar de abstraer patrones generales, el modelo sobreaprende (overfitting) ejemplos específicos
- Al recibir un prompt similar, el modelo recupera y regurgita el texto memorizado

**Data Leakage (Fuga de Datos):**
Ocurre cuando información confidencial o sensible que estaba presente en los datos de entrenamiento es inadvertidamente revelada por el modelo en sus outputs.

**Diferencia clave:**
- **Memorización:** El modelo "recuerda" datos de entrenamiento
- **Leakage:** El modelo revela estos datos memorados en respuestas a usuarios

**Ejemplo Ilustrativo:**

Durante mi investigación, encontré estudios que demuestran la gravedad de este problema. Por ejemplo, investigadores de Google y otras instituciones demostraron que GPT-3 había memorizado información sensible como números de teléfono, direcciones de correo electrónico extraídos de documentos web, fragmentos literales de artículos con copyright, e información de identificación personal (PII) de datasets supuestamente públicos (Carlini et al., 2021).

---

**Escenario del hospital:**

Supuse un hospital que entrena un chatbot clínico con historias médicas reales. Si la anonimización no es adecuada, el modelo podría devolver datos específicos de pacientes al recibir prompts parecidos.

Esto representa un riesgo muy grave porque los datos de salud son sensibles y están protegidos de forma especial.

**Entrenamiento del Modelo:**
El hospital, buscando personalizar el modelo para su contexto, lo entrena (fine-tuning) con:
- 100,000 historias clínicas anonimizadas (o eso creían)
- Notas médicas de doctores
- Resultados de laboratorio
- Transcripciones de consultas

---

**Violaciones a la LOPDP:**

- **Art. 19** – Confidencialidad
- **Art. 5** – Datos sensibles
- **Art. 34** – Seguridad reforzada
- **Art. 29** – Derecho a la supresión
- **Art. 51** – Finalidad
- **Art. 10** – Deber de información



---



---

**Mitigaciones necesarias:**

1. **Anonimización robusta**
2. **Differential Privacy**
3. **Filtros de PII post-generación**
4. **Auditoría periódica**
5. **Uso de datos sintéticos o aprendizaje federado**
6. **Consentimiento explícito para tratamientos con IA**

---

## Referencias

Anthropic. (2025). Claude (versión de diciembre de 2025) [Modelo de lenguaje de gran escala]. https://claude.ai

Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, U., Oprea, A., & Raffel, C. (2021). Extracting training data from large language models. *30th USENIX Security Symposium*, 2633–2650. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting

Constitución de la República del Ecuador. (2008). *Registro Oficial No. 449*. Asamblea Nacional Constituyente del Ecuador. https://www.oas.org/juridico/pdfs/mesicic4_ecu_const.pdf

Hill, K. (2023, mayo 10). Meta to pay $650 million to settle facial recognition lawsuit. *The New York Times*. https://www.nytimes.com/2023/05/10/technology/meta-facebook-privacy-settlement.html

Introna, L. D., & Wood, D. (2004). Picturing algorithmic surveillance: The politics of facial recognition systems. *Surveillance & Society*, 2(2/3), 177–198. https://doi.org/10.24908/ss.v2i2/3.3373

Ley Orgánica de Protección de Datos Personales. (2021). *Registro Oficial Suplemento No. 459*. Asamblea Nacional de la República del Ecuador. https://www.finanzaspopulares.gob.ec/wp-content/uploads/2021/07/ley_organica_de_proteccion_de_datos_personales.pdf

O'Neil, C. (2016). *Weapons of math destruction: How big data increases inequality and threatens democracy*. Crown Publishers.

OpenAI. (2024). *Privacy policy*. OpenAI. https://openai.com/policies/privacy-policy

Rosenblatt, J. (2024, marzo 15). Meta agrees to $1.4 billion privacy settlement with Texas. *Bloomberg Law*. https://news.bloomberglaw.com/privacy-and-data-security/meta-agrees-to-1-4-billion-privacy-settlement-with-texas

---
