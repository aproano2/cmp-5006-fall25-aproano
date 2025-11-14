# Homework 2 – Information Security
**Student:** Paulo Cantos 326682 13/11/2025

---

## 1. Standard Digital Signature Protocol Review


## 1.1 Mechanism 1 – Critique  
(Firma usando clave simétrica y verificación devolviendo la firma al firmante)

Este mecanismo reemplaza la criptografía de clave pública por una clave simétrica compartida. El firmante genera una supuesta “firma” cifrando el hash del mensaje con esa clave, pero el receptor no puede verificarla por sí mismo y debe reenviarla al firmante para pedir confirmación. En términos simples... ambos se quedan con la misma llave secreta y luego esperan que esa llave pruebe quién la usó, algo imposible. Este mecanismo se ve tentador pero realmente rompe no repudio.

### Propiedades de seguridad que se rompen

**No repudio:**  
Como ambos conocen la misma clave simétrica, cualquiera puede generar la “firma”. El receptor también podría inventarla. Además, como la verificación depende del firmante, este puede negar haber confirmado la firma o decir que su clave fue comprometida. No existe ninguna evidencia verificable por un tercero.

**Verificación independiente:**  
En una firma digital real, cualquier persona con la clave pública puede verificar la firma sin interactuar con el firmante. Aquí solo el firmante puede validarla, convirtiéndose en un oráculo de verificación.

**Transferibilidad de la prueba:**  
Una firma debe poder presentarse ante un auditor o una autoridad para demostrar autenticidad. Este mecanismo no permite hacerlo porque ningún tercero puede verificar nada sin el firmante.

**Separación de roles:**  
Como todos los que conocen la clave pueden generar “firmas”, no existe diferencia entre firmante y verificador. Esto no es una firma digital sino un MAC mal aplicado.

### Por qué no es una firma digital verdadera
Este mecanismo parece lógico al inicio, pero... se desarma en cuanto recordamos cómo funcionan las firmas digitales de verdad.
Una firma digital debe usar claves asimétricas, permitir verificación sin interacción con el firmante y ofrecer no repudio. La idea básica es esta y la repito porque es fácil olvidarlo en medio de tanta teoría: si ambos comparten la misma clave, el concepto de firma se derrite. El mecanismo falla en los tres puntos: usa clave simétrica, requiere interacción y no garantiza no repudio.

### Ataques posibles
- El firmante puede negar haber validado la firma.  
- El receptor puede fabricar firmas falsas.  
- Se puede abusar al firmante como oráculo de desencriptado y reciclar las confirmaciones sin control, encadenando varios ataques a la vez.

---

## 1.2 Mechanism 2 – Critique  
(Cifrar el mensaje completo con la clave privada como “firma”)

En este mecanismo el firmante cifra el mensaje completo con su clave privada y el receptor usa la clave pública para descifrarlo y asumir autenticidad al mismo tiempo. Esto lo vemos bastante en clases cuando se habla de firmas digitales introductorias, porque suena tentador "cifrar con la privada" sin notar las consecuencias.

### Por qué el mecanismo es incorrecto

**Confunde cifrado con firma:**  
Cifrar con la clave privada no da confidencialidad, porque cualquiera puede descifrar con la clave pública. Las firmas digitales no cifran el mensaje completo; firman el hash del mensaje.

**Incompatible con algoritmos modernos:**  
RSA, ECDSA y otros esquemas no firman cifrando el mensaje entero. Siempre firman el hash. Además, RSA no permite cifrar mensajes grandes directamente.

**Ineficiente y poco práctico:**  
El cifrado asimétrico no está diseñado para manejar grandes volúmenes de datos. Intentar “firmar” cifrando todo el mensaje rompe límites de tamaño y vuelve el proceso lento e inseguro.

### Propiedades que se rompen
- No hay confidencialidad: cualquiera con la clave pública puede leer todo el mensaje.  
- La integridad y la compatibilidad quedan en el aire porque no se usa hashing ni se respetan los formatos estándar.  
- Se mezclan autenticación y entrega de contenido en una sola operación, así que ningún rol queda realmente separado.

### Vulnerabilidades introducidas
- Mensajes grandes no caben en RSA.  
- Riesgo de ataques de padding conocidos.  
- Mayor exposición de la clave privada al usarse para cifrar demasiado.  
- La verificación depende de interpretar contenido, lo cual puede ser peligroso.  
- Además, se amplía la superficie para ataques de side-channel porque la clave privada procesa entradas arbitrarias enviadas por quien verifica.

### Por qué se debe firmar el hash
Firmar el hash hace el proceso eficiente, seguro y compatible con los estándares. El hash cambia completamente si se altera un solo bit del mensaje y tiene tamaño fijo, permitiendo firmar archivos de cualquier tamaño. Creo que lo más importante aquí es entender que no firmamos el documento por completo, sino una huella pequeña que representa exactamente lo mismo.

---

## Conclusión general
Los dos mecanismos fallan porque no siguen el principio básico de las firmas digitales: usar criptografía asimétrica y firmar únicamente el hash del mensaje. Ambos rompen propiedades esenciales y no cumplen con los requisitos mínimos de una firma digital real.

---

## 2. Vulnerability to Attack Vectors


## 2.1 Scenario 1 – Alteración del mensaje

Alice firma el mensaje “Transferir $1000 a Mark” y envía el par (x, auth(x)) a Bob. Oscar intercepta la transmisión y cambia el contenido a “Transferir $1000 a Oscar”, intentando usar la misma firma.

### ¿Bob detecta la alteración?

Sí, la detecta. En este caso lo que pasa es que... la firma digital está ligada matemáticamente al hash exacto del mensaje original. El proceso real de firma es:

σ = Sign_sk(H(x))

Cuando Bob recibe el mensaje modificado:

1. Calcula el hash del mensaje recibido H(x_recibido).  
2. Verifica la firma con la clave pública de Alice: Verify_pk(σ, H(x_recibido)).

Como el contenido cambió, el hash cambia por completo y la firma deja de coincidir. La verificación falla.



### Propiedades que protegen este escenario

**Integridad:** cualquier modificación invalida la firma.  
**Autenticidad:** solo la clave privada de Alice puede generar una firma válida.  
**No repudio:** Alice no puede negar haber firmado el mensaje original.

### Vulnerabilidad que Oscar intenta explotar

Oscar intenta un ataque de manipulación del mensaje: cambiar el contenido y reutilizar la firma original. Con un esquema moderno de firma + hash, esto no funciona.

### Cómo el esquema hash + firma evita este ataque

- El hash produce una huella digital única.  
- Un solo bit cambiado genera un hash totalmente diferente.  
- Oscar no puede encontrar otra entrada con el mismo hash ni generar una nueva firma sin la clave privada.

### Cuándo podría fallar este sistema

Este ataque solo podría funcionar si el sistema estuviera mal diseñado:

- Si se firma el mensaje sin aplicar un hash.  
- Si se usa un hash inseguro (MD5, SHA-1).  
- Si solo se firma parte del mensaje.  
- Si se usa RSA sin padding adecuado (RSA "puro").

Nota al margen: en un laboratorio todo luce impecable, pero basta olvidarse de firmar un metadato o de validar la versión para que este escenario vuelva a ser vulnerable.

---

## 2.2 Scenario 2 – Ataque de Repetición (Replay Attack)

Oscar intercepta el par válido (x, auth(x)) —por ejemplo “Transferir $1000 a Mark”— y lo reenvía sin modificar nada muchas veces a Bob.

### ¿La firma verifica cada vez?

Sí. Si Oscar envía exactamente el mismo par, la firma seguirá siendo válida. Las firmas digitales aseguran integridad y autenticidad, pero no aseguran frescura ni unicidad del mensaje. Este ataque pasa todo el tiempo si no se usan nonces.

### Nombre del ataque

Replay Attack (ataque de repetición).

### Por qué es un problema si Bob procesa todo

Si Bob ejecuta cada reenvío, estaría procesando varias veces la misma transacción firmada. En la práctica, lo que ocurriría es que Bob terminaría debitando múltiples veces la misma orden antes de notar el patrón. Alice estaría autorizando múltiples transferencias sin querer. Esto no es un fallo de la firma, sino del protocolo que usa la firma.

### Por qué la firma digital no evita este ataque sola

La firma garantiza:

- que el mensaje viene de Alice,  
- y que no fue modificado.

Pero NO garantiza:

- que el mensaje sea reciente,  
- que no se haya enviado antes,  
- que deba procesarse una sola vez,  
- que no esté siendo reutilizado en otra sesion.

Un mensaje firmado hoy sigue siendo válido mañana si el protocolo no agrega mecanismos anti-replay.

### Mecanismos para evitar ataques de repetición

Los sistemas reales combinan firmas con mecanismos de frescura:

- Nonces (números aleatorios únicos por sesión).  
- Timestamps (marcas de tiempo).  
- Sequence numbers (números de secuencia crecientes).  
- Transaction IDs únicos.  
- Lista de transacciones ya procesadas para descartar duplicados.

### Ejemplo de flujo anti-replay

Alice genera:

- Mensaje x  
- ID único: txn_id  
- Firma: σ = Sign_sk(H(x ∥ txn_id))

Envía a Bob: (x, txn_id, σ).

Bob verifica:

1. La firma.  
2. Que txn_id no haya sido usado antes.

Si Oscar reenvía el mensaje:

- La firma es válida.  
- Pero el ID ya existe → Bob lo rechaza.

Bueno, suena repetitivo, pero la única forma de que Bob esté tranquilo es revisar dos veces: primero la firma y luego que el identificador no haya salido ya en la bitácora.

---


---

## 3. Research: Transport Layer Security (TLS 1.3)

## 3.1 Arquitectura y evolución de TLS

TLS (Transport Layer Security) es un protocolo criptográfico que funciona por encima de un transporte fiable como TCP y por debajo de los protocolos de aplicación (HTTP, SMTP, etc.). Su fin es ofrecer un canal cifrado que evite escuchas, manipulación de mensajes y suplantación de identidad.

No calza exactamente con el modelo OSI; suele explicarse como un nivel intermedio entre la capa de transporte y la de aplicación.
Creo que la parte clave es entender ese “nivel intermedio”, porque siempre nos venden TLS como magia negra cuando en realidad solo envuelve el tráfico de la app.
En esta parte tuvimos un poco de dificultad para decidir cuánta historia incluir y cuánta omitir, así que si suena repetitivo es porque de verdad queríamos que el lector no se pierda entre tantas capas y siglas.

Internamente basta con recordar que el Record Protocol transporta todo y que el Handshake se encarga de negociar algoritmos y autenticaciones (las alertas siguen existiendo, pero ya no vale la pena describirlas una por una).

Históricamente, TLS viene de SSL 2.0/3.0 (inseguros hoy). TLS 1.0, 1.1 y 1.2 añadieron mejoras progresivas, pero TLS 1.3 (RFC 8446, 2018) representa un rediseño completo:

- Reduce el handshake a 1 RTT y permite 0-RTT en reanudaciones.
- Elimina algoritmos inseguros (RSA estático, CBC, RC4, compresión TLS, hashes débiles).
- Obliga a usar forward secrecy con (EC)DHE efímero.
- Adopta HKDF como derivador de claves.

El resultado es un protocolo mas simple, rapido y seguro que TLS 1.2. La idea es basicamente que TLS 1.3 se queda con lo salido y barria lo demas; fue una limpieza completa de lo viejo.

---

## 3.2 Primitivas criptográficas en TLS 1.3

TLS 1.3 utiliza un conjunto más limitado pero moderno de primitivas:

### Intercambio de claves – (EC)DHE efímero
El secreto compartido se genera con Diffie–Hellman efímero, generalmente sobre curvas elípticas (X25519, P-256, etc.). Cada conexión usa claves nuevas, lo que da forward secrecy.

### Cifrado simétrico – AEAD
Solo permite cifrados autenticados AEAD:

- AES-GCM (128/256)
- ChaCha20-Poly1305

Estos cifrados aportan confidencialidad e integridad en una sola operación, usando nonces y AAD. No hay espacio para algoritmos vintage aqui.

### Derivación de claves - HKDF
TLS 1.3 usa HKDF, que es la función moderna de derivación, para sacar todas las llaves a partir del secreto (EC)DHE y del transcript; no detallo cada secret porque basta saber que se generan claves distintas para handshake y tráfico de aplicación y que comprometer una no rompe las demás.

### Funciones hash
TLS 1.3 depende de SHA-256 y SHA-384 para alimentar HKDF, para calcular el hash de todo el intercambio hasta ese punto y para firmar ese mismo intercambio durante la autenticación.

MD5 y SHA-1 ya no se permiten.

En comparación con TLS 1.2, desaparecen RSA estático, CBC y compresión. El conjunto se reduce a algoritmos actuales y seguros.



---

## 3.3 Confidencialidad, integridad y autenticación en TLS 1.3

### Confidencialidad
En TLS 1.3 casi todo va cifrado. Despu?s del ServerHello, la mayor parte del handshake ya viaja cifrada y el tr?fico de aplicaci?n usa una clave distinta. Las etapas de derivaci?n (0-RTT, handshake y aplicaci?n) existen, pero no hace falta recitarlas; lo importante es que, al usar (EC)DHE ef?mero, aunque alguien robe la clave privada del servidor m?s adelante no podr? descifrar sesiones pasadas.

### Integridad
La integridad proviene de AEAD. Cada registro tiene:

- un nonce único  
- un tag de autenticación  

Si los datos cambian mínimamente, la verificación falla y la conexión se cierra. Ya no existe un MAC separado como en versiones antiguas.

### Autenticaci?n
Se basa en certificados X.509: el servidor manda su cadena, firma el transcript (CertificateVerify) y remata con un Finished. El cliente valida todo eso y aqu? ya se puede verificar que el servidor posee la clave privada del certificado y que nadie alter? el handshake. La autenticaci?n mutua es opcional y, si se pide, repite la misma idea para el cliente.

---


## 3.4 Aplicaciones modernas de TLS 1.3

TLS 1.3 está presente en la mayoría de escenarios donde se requiere un canal seguro. Yo lo suelo agrupar así:

- **HTTPS en la web:** Navegadores y servidores modernos ya usan TLS 1.3 por defecto; reduce latencia y mejora seguridad.
- **APIs REST y microservicios:** Es común en arquitecturas distribuidas para comunicaciones seguras entre servicios.
- **Aplicaciones móviles y clientes ligeros:** TLS 1.3 junto con ChaCha20-Poly1305 es eficiente en dispositivos sin aceleración AES (la batería lo agradece).

En el extremo de las capas superiores, HTTP/2 y HTTP/3 dependen de TLS 1.3 para su arranque, mientras que muchas VPN basadas en TLS y pasarelas financieras lo adoptaron simplemente porque evitaron reinventar la rueda de la seguridad.
Me pareció útil hacer esta separación entre “web/microservicios” y “capa superior” porque, bueno, son los escenarios que más  en proyectos pequeños.

---

---

## 4. Design Problem: Secure Electronic Contract Signing System (SECS)

### 4.1 Objetivo y requisitos de seguridad

El sistema SECS (Secure Electronic Contract Signing System) permite que dos partes, Alice (proveedor de servicios) y Bob (cliente), firmen electrónicamente un contrato digital (por ejemplo, una licencia de propiedad intelectual) de forma segura. La idea es que el sistema garantice, basicamente, lo mismo que haríamos con papel y pluma, solo que con mejores logs:

- Autenticación fuerte de las partes.  
- Integridad del contrato y de sus versiones.  
- No repudio de origen: nadie puede negar haber firmado una versión concreta del contrato.  
- No repudio de envío y recepción: nadie puede negar haber recibido la copia final firmada.  
- Trazabilidad completa del proceso y evidencia verificable a largo plazo.

Hay muchas formas de diseñar este sistema; yo elegi esta porque me parece la mas clara para explicar el flujo . Este sprint sera el mas pesado porque mezcla analisis de requisitos, arquitectura y pruebas de no repudio en un solo paquete.

Suposiciones básicas:

- Cada parte tiene un par de claves asimétricas (sk_X, pk_X) y un certificado X.509 emitido por una CA confiable.  
- Todas las comunicaciones van sobre TLS 1.3.  
- El tiempo de los sistemas (SECS y la TSA) está bien sincronizado.

---

### 4.2 Arquitectura general de SECS

A nivel lógico, SECS se compone de varios bloques:

#### Frontends (Alice y Bob)
Aplicaciones web o móviles donde los usuarios:

- Se autentican (idealmente con MFA).  
- Crean, revisan y firman contratos.  
- Consultan el historial y descargan la versión final firmada.

#### Backend / Servidor de aplicación SECS

- Expone APIs (REST/GraphQL) para manejar contratos, sesiones de firma y evidencias.  
- Aplica reglas de negocio (quién firma, en qué orden, estados del contrato, etc.).  
- Coordina la interacción con PKI, TSA y el módulo de auditoría.

#### PKI y Autoridad de Certificación (CA)

- Emite certificados X.509 para Alice, Bob y, si hace falta, para SECS.  
- Mantiene CRL/OCSP para verificar el estado de los certificados.  
- Vincula claves públicas con identidades reales (persona/empresa), lo que es clave para el no repudio.

#### Repositorio de contratos y metadatos

- Guarda los contratos (por ejemplo, PDFs) en un almacenamiento tipo object storage.  
- Registra metadatos como:  
  - contract_id  
  - versión  
  - H(M) (hash del documento)  
  - estado  
  - partes involucradas  
  - marcas de tiempo  
  - referencias a las firmas

Una versión ya firmada no se modifica; si hay cambios, se crea una nueva versión con un nuevo hash.

#### Servidor de sellado de tiempo (TSA)

- Recibe hashes de contratos o firmas.  
- Devuelve Time-Stamp Tokens (TST) firmados que prueban que esos datos existían en una fecha y hora concreta.  
- Añade un tercero de confianza al componente temporal del no repudio.

#### Módulo de auditoría y logs inmutables

- Registra eventos como creación de contrato, visualizaciones, firmas, envíos y descargas del artefacto final.  
- Los logs son append-only y se encadenan con hashes (hash chain o Merkle tree) para detectar manipulaciones.  
- Opcionalmente se publican resúmenes hash en un almacén externo o blockchain privada.

#### HSM / módulos seguros de claves (opcional pero recomendable)

- Protegen claves privadas críticas (CA, TSA, servidor SECS y, en esquemas de firma remota, claves de usuario).  
- Reducen el riesgo de compromiso y refuerzan la idea de control exclusivo sobre las firmas.

En conjunto, esta arquitectura mezcla app, infra criptográfica (PKI, TSA, HSM) y almacenamiento inmutable para construir una cadena de evidencias sólida. Obviamente esta arquitectura es simplificada; en la practica habraa mas modulos satelite y procesos operativos.

---

### 4.3 Mecanismos criptográficos utilizados

#### Hash de documentos y versiones

Para cada versión canónica del contrato M se calcula:

- h_M = H(M)

donde H es un hash seguro (como SHA-256).  
Ese hash identifica de forma inmutable la versión y sirve de base para las firmas.

#### Firmas digitales de Alice y Bob

Antes de firmar, el servidor genera un mensaje canónico que incluye:

- contract_id  
- versión  
- h_M  
- rol de la parte  
- session_id  
- y, en el caso de Bob, referencia a la firma de Alice

Para Alice:

- m_A = (contract_id, versión, h_M, rol = "PROVEEDOR", session_id)  
- h_A = H(m_A)  
- σ_A = Sign_skA(h_A)

Para Bob:

- m_B = (contract_id, versión, h_M, rol = "CLIENTE", session_id, ref_sig_A)  
- h_B = H(m_B)  
- σ_B = Sign_skB(h_B)

Aquí ref_sig_A puede ser, por ejemplo, H(σ_A), lo que hace que Bob firme explícitamente el mismo contrato que ya firmó Alice.
Obviamente en un sistema productivo habría más metadatos (por ejemplo, localidad o políticas internas).

#### Sellado de tiempo (TSA)

Aquí viene la parte delicada... si nadie externo fija un instante temporal, cualquier firma podría cuestionarse años después.

Después de las firmas se construye un hash combinado:

- h_final = H(M ∥ m_A ∥ σ_A ∥ m_B ∥ σ_B)

Este valor se manda a la TSA, que responde con un TST:

- TST = Sign_skTSA(h_final ∥ t ∥ serial ∥ ...)

El TST vincula el contenido y las firmas con un instante temporal concreto.

#### Firma del servidor SECS (Acta de Firma)

El sistema genera un artefacto final F (un “Acta de Firma”) que resume:

- El contrato M  
- Los hashes  
- Las firmas de Alice y Bob  
- Los TST emitidos  
- Un resumen de eventos de auditoría más relevantes

Luego:

- h_F = H(F)  
- σ_SECS = Sign_skSECS(h_F)

Opcionalmente, h_F también se sella en la TSA.  
Este acta firmada por SECS facilita la prueba ante un juez o auditor.

_equeña nota sobre los logs encadenados:_ cada entrada L_i se arma tomando el hash del elemento anterior (prev_hash = H(L_{i-1})) y mezcl?ndolo con su propio contenido para obtener self_hash = H(L_i ? prev_hash). Asi cualquier modificacion rompe la cadena y se detecta enseguida; es casi un mini-blockchain sin la parte glamorosa y sin minas de datos escondidas.

---

### 4.4 Flujo del protocolo SECS (alto nivel)



#### 4.4.1 Fase de preparación (creación del contrato)

1. Alice → SECS: envía el borrador del contrato para crear un nuevo contract_id.  
2. SECS:
   - Normaliza el documento a una versión canónica M.  
   - Calcula h_M = H(M).  
   - Almacena M y h_M.  
   - Crea una sesión de firma y registra CONTRACT_CREATED en el log.

#### 4.4.2 Fase de firma de Alice

1. Alice → SECS: envía SignRequest_Alice indicando que quiere firmar.  
2. SECS:
   - Comprueba autenticación y permisos.  
   - Genera m_A y h_A = H(m_A).  
3. Alice:
   - Firma localmente (o vía HSM) y calcula σ_A = Sign_skA(h_A).  
   - Envía σ_A y su certificado a SECS.  
4. SECS:
   - Guarda σ_A y Cert_A.  
   - Registra SIGNED_BY_ALICE en el log.  
   - Opcionalmente pide un TST sobre contrato + firma de Alice y lo almacena.

#### 4.4.3 Fase de firma de Bob

1. SECS → Bob: le avisa de que hay un contrato listo y que Alice ya firmó.  
2. Bob → SECS: pide el contrato. SECS le manda:
   - M  
   - h_M  
   - σ_A  
   - Cert_A  
   - TST correspondiente a la firma de Alice  
3. Bob (o SECS en su nombre) verifica:
   - Que H(M) coincide con h_M.  
   - Que la firma de Alice es válida.  
   - Que certificado y TST son correctos.  
4. Si Bob decide firmar:
   - SECS genera m_B, incluyendo h_M y ref_sig_A.  
   - Bob calcula σ_B = Sign_skB(H(m_B)).  
5. SECS:
   - Guarda σ_B y Cert_B.  
   - Registra SIGNED_BY_BOB.  
   - Solicita a la TSA un TST sobre h_final.

#### 4.4.4 Fase de cierre y no repudio de recepción

1. Creación del artefacto final F:
   - SECS empaqueta contrato, firmas, TSTs y resumen de auditoría en F.  
   - Calcula h_F y firma con σ_SECS.  
2. Entrega a las partes:
   - SECS → Alice: notificación + enlace para descargar F.  
   - SECS → Bob: igual.  
   - Cada descarga/visualización genera eventos FINAL_ARTIFACT_DELIVERED_TO_ALICE y FINAL_ARTIFACT_DELIVERED_TO_BOB en el log.  
3. (Opcional) Acuse de recibo firmado:
   - Alice y Bob pueden firmar un mensaje tipo  
     - ack_A = Sign_skA(H("RECEIVED_FINAL" ∥ contract_id ∥ version ∥ h_F))  
   - Esto refuerza aún más el no repudio de recepción.

---

### 4.5 Cómo se garantiza el no repudio

#### No repudio de origen

- Cada parte firma un hash que:
  - Identifica de forma única el contenido del contrato (h_M).  
- Incluye metadatos como contrato, versión, rol y sesión.  
- Las firmas σ_A y σ_B se validan con certificados X.509 emitidos por una CA confiable.  
- Los TST prueban que las firmas existían en un momento concreto y que los certificados eran válidos.  
- El uso de HSM refuerza la idea de que solo el titular controlaba la clave privada.

Esto ayuda a que Alice o Bob la tengan difícil si intentan negar haber firmado esa versión concreta del contrato.

#### No repudio de envío/recepción

SECS registra en logs inmutables cada entrega del artefacto final, guardando usuario autenticado, timestamp, IP o dispositivo y el hash h_F entregado. Si el caso lo amerita, Alice y Bob emiten un acuse de recibo firmado sobre ese mismo hash (no siempre lo piden, pero deja todo redondo). Los logs siguen la misma cadena de hashes mencionada antes y se pueden sellar periódicamente o incluso anclar a una blockchain privada. 
