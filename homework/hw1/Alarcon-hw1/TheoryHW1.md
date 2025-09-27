# Homework Assignment: Classical Cryptography
**Course:** Information Security

---

## Part I: Research Component

### Task: Historical Cryptographic Algorithms Survey

## Substitution Ciphers

### Caesar Cipher

**Brief historical context and inventor/origin**

El cifrado César fue creado por Julio César, quien lo utilizó como método para comunicarse con sus generales durante las batallas. Aunque su diseño era simple, resultó eficaz en su época, ya que muchas personas no sabían leer, lo que aumentaba la seguridad del mensaje (Duarte et al., 2023). Este método es considerado una de las primeras aplicaciones documentadas de la criptografía.

**Description of the encryption/decryption process**

El proceso de cifrado consiste en desplazar cada letra del mensaje original un número fijo de posiciones, representado por la clave *k*. Por ejemplo, con *k = 3*, la letra **A** se convierte en D, la B en E, la C en F, y así sucesivamente. Al llegar al final del alfabeto, el conteo continúa desde el inicio aplicando el operador módulo 26, correspondiente al número de letras en el alfabeto latino.

El descifrado se realiza aplicando el desplazamiento en sentido contrario: cada letra cifrada se reemplaza por la que se encuentra *k* posiciones atrás en el alfabeto (Fernández, 2004).

**Key space size**

El espacio de claves posibles es de 25, ya que un desplazamiento de 0 no produce cifrado.

**Known vulnerabilities and cryptanalysis methods**

El cifrado César es muy débil y puede romperse fácilmente mediante fuerza bruta o análisis de frecuencia. Este último aprovecha la frecuencia característica de aparición de ciertas letras en un idioma, lo que permite deducir la clave con rapidez (Gómez et al., 2012).

**Real-world usage examples (if any)**

Se usaba en las batallas para comunicarse con los generales. En la actualidad, debido a sus vulnerabilidades, su uso se limita principalmente a fines educativos, ejercicios de práctica y acertijos simples.

---

### Affine Cipher

**Brief historical context and inventor/origin**

El cifrado Afín (Affine cipher) es un método de sustitución que amplía el clásico cifrado César, utilizado por Julio César para proteger mensajes militares. Mientras que el cifrado César se basa en desplazar cada letra un número fijo de posiciones, el Afín incorpora un paso adicional que lo hace más seguro. Funciona asignando un valor numérico a cada letra y aplicando una transformación matemática para codificar y luego recuperar el texto original. Aunque originalmente estaba limitado a las 26 letras del alfabeto inglés, con el tiempo se ha adaptado para incluir caracteres ASCII y se ha fortalecido mediante técnicas como la Transformación de Dígrafos o su integración con herramientas modernas como la Criptografía de Curvas Elípticas. (Kazemi et al., 2011).

**Description of the encryption/decryption process**

Cada letra se representa mediante un valor numérico y se cifra con la fórmula:

$$E(x) = (ax + b) \bmod 26$$

donde *a* y *b* son las claves, y debe cumplirse que $\gcd(a,26) = 1$ para garantizar la existencia de un inverso multiplicativo.

El descifrado requiere calcular dicho inverso de *a* módulo 26 y aplicar la fórmula:

$$D(y) = a^{-1}(y - b) \bmod 26$$

(Mokhtari & Naraghi, 2012).

**Key space size**

Existen 12 posibles valores de *a* que son coprimos con 26, y 26 posibles valores de *b*. Por lo tanto, el espacio de claves es de $12 \times 26 = 312$.

**Known vulnerabilities and cryptanalysis methods**

A pesar de ser más seguro que el César, el cifrado Afín sigue siendo un cifrado de sustitución monoalfabética, lo que lo hace vulnerable a ataques de análisis de frecuencia. Además, al ser un esquema simétrico, conocer la función de cifrado permite deducir la de descifrado (Mokhtari & Naraghi, 2012).

**Real-world usage examples (if any)**

Actualmente no tiene aplicaciones prácticas en seguridad real y se utiliza sobre todo con fines académicos, como ejemplos introductorios en la enseñanza de criptografía.

---

### Monoalphabetic Substitution

**Brief historical context and inventor/origin**

El cifrado por sustitución monoalfabética (Monoalphabetic Substitution) es uno de los métodos de encriptación más antiguos y sencillos y consistente en reemplazar cada letra de algun texto original por otra siguiendo un esquema fijo. Se utilizó desde la antigüedad en civilizaciones como la griega, romana y árabe, y no se conoce su inventor especifico. Durante el Renacimiento este sistema se extendió en Europa, y en el mundo arabe luego nacio el análisis de frecuencias, usada para descifrar este tipo de códigos. (Dooley, 2018; Pelosi & Selleri, 2021)

**Description of the encryption/decryption process**

Para cifrar, cada letra del texto se sustituye por la letra que ocupa la misma posición en el alfabeto permutado. Para descifrar, se utiliza la tabla inversa, recuperando el texto original al reemplazar las letras cifradas por sus equivalentes en el alfabeto normal (Kang & Lee, 2024).

**Key space size**

El espacio de claves corresponde al número de permutaciones posibles del alfabeto. En el caso del alfabeto latino, existen $26!$ posibilidades, lo que equivale a aproximadamente $4 \times 10^{26}$ claves (Kang & Lee, 2024).

**Known vulnerabilities and cryptanalysis methods**

Aunque el número de claves es enorme, el cifrado es vulnerable al análisis de frecuencia, ya que algunas letras aparecen con mayor frecuencia que otras en un idioma. De igual forma, patrones lingüísticos comunes como artículos o conjunciones facilitan su ruptura. Incluso con fuerza bruta, este método puede descifrarse en textos suficientemente largos (Kang & Lee, 2024).

**Real-world usage examples (if any)**

Actualmente no se utiliza con fines de seguridad debido a su debilidad, pero sigue siendo empleado en la enseñanza de criptografía, en juegos y acertijos. Además, su estudio fue fundamental para el desarrollo de métodos más avanzados como los cifrados por bloques (Kang & Lee, 2024).

---

### Polyalphabetic Substitution (Vigenère Cipher)

**Brief historical context and inventor/origin**

El cifrado Vigenère recibe su nombre de Blaise de Vigenère, diplomático y criptógrafo de la corte de Enrique III de Francia en el siglo XVI. Durante varios siglos fue considerado "indescifrable", hasta que en 1917 Friedrich Kasiski y William Friedman desarrollaron técnicas efectivas para romperlo (Aliyu & Olaniyan, 2016).

**Description of the encryption/decryption process**

El método utiliza una palabra clave (*keyword*) que se repite hasta igualar la longitud del texto a cifrar. Cada letra del texto se combina con la letra correspondiente de la clave sumando sus posiciones en el alfabeto, según la fórmula:

$$C_i = (P_i + K_i) \bmod 26$$

Para descifrar, se aplica la fórmula inversa:

$$P_i = (C_i - K_i) \bmod 26$$

(Aliyu & Olaniyan, 2016).

**Key space size**

Si la clave tiene una longitud $m$, entonces existen $26^m$ posibles combinaciones (Aliyu & Olaniyan, 2016).

**Known vulnerabilities and cryptanalysis methods**

El punto débil del cifrado radica en la repetición de la clave, lo que permite aplicar análisis de frecuencia en segmentos del texto. Una vez identificada la longitud de la clave, el problema se reduce a resolver varios cifrados César. Esto fue la base del ataque de Kasiski y del índice de coincidencia, técnicas que hicieron posible su ruptura (Aliyu & Olaniyan, 2016).

**Real-world usage examples (if any)**

Aunque ya no se emplea en seguridad moderna por sus vulnerabilidades, el cifrado Vigenère sigue teniendo un valor educativo y recreativo, siendo un clásico en cursos de criptografía y en acertijos históricos.

---

## Transposition Ciphers

### Columnar Transposition

**Brief historical context and inventor/origin**

El cifrado por transposición columnar (Columnar Transposition) fue un método popular creado y utilizado entre mediados del siglo XIX y la primera mitad del siglo XX para proteger mensajes. Su mecanismo consistía en escribir el texto en filas dentro de una cuadrícula con un número determinado de columnas y luego leerlo por columnas siguiendo un orden establecido por una clave, lo que cambiaba la posición original de las letras.

A partir de este sistema se desarrollaron variantes más complejas, como el cifrado ADFGVX y la doble transposición, que ampliaron su seguridad. Con el tiempo, los avances en criptografía redujeron su uso; sin embargo, su concepto básico sigue siendo estudiado en la criptografía moderna (Lasry et al., 2016; Dooley, 2018).

**Description of the encryption/decryption process**

El proceso de encriptación se basa en escoger una *keyword* o palabra clave, a la cual se asigna un número a cada letra dependiendo de su orden alfabético.

Por ejemplo, con la palabra "hola":
- a = 1, h = 2, l = 3, o = 4.

Luego, el texto a cifrar se organiza en filas del mismo largo que la *keyword*. Si el texto es más largo, se continúa escribiendo hacia abajo y se rellenan los espacios sobrantes con la letra **x**.

Después, se leen las columnas en el orden determinado por los números de la clave (primero la columna marcada con 1, luego la 2, etc.) hasta completar el criptograma.

Para desencriptar, el texto cifrado se divide en columnas según la longitud de la clave, se colocan en una tabla siguiendo ese orden y finalmente se leen las filas en secuencia para recuperar el mensaje original (Jones, 2016).

**Key space size**

El espacio de claves depende de la longitud de la palabra clave. Si la *keyword* tiene n caracteres, existirán n! formas posibles de ordenar las columnas.

**Known vulnerabilities and cryptanalysis methods**

El cifrado por transposición columnar conserva exactamente las mismas letras del texto original, lo que facilita aplicar:
- análisis de frecuencia,
- análisis de patrones,
- búsqueda de palabras comunes.

Además, puede romperse con ataques de fuerza bruta (Kester, 2013).

**Real-world usage examples**

Fue utilizado como cifra de campo por los ejércitos alemán y estadounidense hasta la Primera Guerra Mundial, y también durante la Segunda Guerra Mundial (Xipell, 2009).

---

### Rail Fence Cipher

**Brief historical context and inventor/origin**

El cifrado Rail Fence (Rail Fence Cipher) es un metodo clásico de transposición que consiste en reorganizar los caracteres de un mensaje original para formar un texto cifrado. Su nombre viene de que el mensaje se lee "como una reja (fence)" Fue uno de los primeros métodos de encriptación utilizados históricamente, por su sencillez y facilidad de aplicación, junto con otros sistemas como el cifrado César o la transposición columnar. Aunque no se conoce bien su origen o inventor, se sabe que ha sido empleado desde tiempos antiguos (incluso grecia antigua), en contextos debido a su simplicidad y el bajo costo computacional del modelo. Se la uso comunmente en guerras, como la guerra civil de Estados Unidos. Ahora es vulnerable a atauqes de criptografia mas avanzados, pero sigue siendo estudiado y se lo ha combinado con otras técnicas para mejorar su seguridad, manteniendolo como modelo clave de la criptografía. (Jagetiya & Krishna, 2020; Siahaan, 2016; Glantz, 2011; Hoobi, 2025)

**Description of the encryption/decryption process**

Este cifrado utiliza una clave k, que representa el número de rieles. El texto se escribe en zigzag: bajando diagonalmente hasta el último riel y luego subiendo.

Ejemplo con k = 3 y el texto "holacomoestas":
- **Riel 1:** h . . . c . . . e . . . s
- **Riel 2:** . o a o o s a
- **Riel 3:** . . l . . . m . . . t

El texto cifrado se obtiene concatenando los rieles en orden: hcesoaoosalmt.

Para desencriptar, se distribuyen las letras cifradas en los rieles siguiendo el mismo patrón en zigzag. Después se leen en orden diagonal, reconstruyendo el mensaje original "holacomoestas".

**Key space size**

En teoría, si se permite cualquier número de rieles hasta la longitud del texto, el espacio de claves es n - 1, para un mensaje de n letras.

**Known vulnerabilities and cryptanalysis methods**

El Rail Fence Cipher es vulnerable a ataques de fuerza bruta debido a su reducido espacio de claves. Puede romperse fácilmente mediante análisis manual o computacional de patrones (Siahaan, 2016).

**Real-world usage examples**

En el contexto de la computación en la nube, el Rail Fence Cipher destaca por su simplicidad y rapidez. Aunque ofrece menor seguridad que algoritmos más robustos como el Hill Cipher, su eficiencia lo convierte en una opción viable para ciertas aplicaciones en entornos de nube (Dalal et al., 2023).

---

## Advanced Classical Systems

### Hill Cipher

**Brief historical context and inventor/origin**

El Hill Cipher fue inventado en 1929 por Lester S. Hill. Es el primer cifrado poligráfico que trabaja con álgebra lineal, ya que utiliza matrices para transformar bloques de letras en otros bloques. Su característica distintiva es que cifra varias letras al mismo tiempo, lo que dificulta la detección de patrones de frecuencia, a diferencia de cifras más simples como César o Vigenère (Hasoun et al., 2021).

**Description of the encryption/decryption process**

Se utiliza una matriz clave (K) de tamaño *n × n*. Para trabajar con el alfabeto de 26 letras, cada letra se convierte en su valor posicional (A = 0, B = 1, ..., Z = 25).

- Para cifrar, el texto plano se divide en bloques de tamaño *n*, se convierten en vectores/matrices (P) y se aplica:

$$C = K \cdot P \pmod{26}$$

- El proceso se repite por cada bloque, obteniendo así el criptograma.

- Para descifrar, se calcula la inversa modular de K y se aplica:

$$P = K^{-1} \cdot C \pmod{26}$$

(Acharya et al., 2009).

**Key space size**

En el Hill Cipher, la clave debe ser una matriz invertible módulo 26. El espacio de claves depende del número de estas matrices existentes. Por ejemplo, para matrices de tamaño 2×2, existen 157,248 claves válidas. Esto muestra un crecimiento rápido del espacio de claves, aunque la seguridad no depende únicamente de este tamaño debido a la naturaleza lineal del algoritmo.

**Known vulnerabilities and cryptanalysis methods**

El Hill Cipher es vulnerable a ataques de texto conocido debido a su carácter lineal. Aunque la multiplicación matricial no garantiza seguridad por sí sola, sigue siendo útil cuando se combina con operaciones no lineales, ya que estas aportan difusión al proceso de cifrado (Hasoun et al., 2021).

**Real-world usage examples**

Actualmente, el Hill Cipher se emplea principalmente con fines educativos, para ilustrar cómo las matemáticas (matrices, determinantes e inversas) se aplican en la criptografía.

---

### One-Time Pad (OTP)

**Brief historical context and inventor/origin**

El concepto de cifrado con clave de un solo uso tiene raíces tempranas. Aunque a menudo se atribuye a Gilbert Vernam (1917) y Joseph Mauborgne, investigaciones históricas revelan que Frank Miller ya había descrito la idea en 1882 (Bellovin, 2011).

- Vernam propuso un sistema de teletipo que combinaba texto con una cinta de clave.
- Mauborgne estableció que la clave debía ser completamente aleatoria y usada solo una vez.
- Más tarde, Claude Shannon (1949) demostró formalmente que este sistema alcanzaba secreto perfecto desde la teoría de la información.

**Description of the encryption/decryption process**

El OTP requiere que el mensaje y la clave tengan la misma longitud.

- Cifrado:
$$C = P \oplus K$$

- Descifrado:
$$P = C \oplus K$$

Para garantizar seguridad perfecta, la clave debe ser:
1. verdaderamente aleatoria,
2. independiente,
3. tan larga como el mensaje,
4. jamás reutilizada (Ware, 1997).

**Key space size**

Si el mensaje tiene longitud n bits, la clave debe tener también n bits. El espacio de claves es entonces $2^n$.

Ejemplo: para un mensaje de 128 bits, el espacio de claves es $2^{128}$.

**Known vulnerabilities and cryptanalysis methods**

En teoría, el OTP es invulnerable si se cumplen sus condiciones. En la práctica, sus vulnerabilidades provienen de errores de implementación:

- **Reutilización de claves (two-time pad):** permite obtener relaciones entre textos mediante XOR (Mason et al., 2016).
- **Errores en la generación/distribución de claves:** si no son verdaderamente aleatorias o se repiten, la seguridad se pierde (caso histórico: Proyecto Venona, NSA, 1996).
- **Mensajes estructurados:** al reutilizar claves en textos con formatos predecibles, el criptoanálisis puede recuperar gran parte del mensaje (Mason et al., 2016).
- **Extensiones cuánticas:** algunos estudios exploran el reciclaje de claves en criptografía cuántica bajo condiciones específicas, aunque esto no aplica al OTP clásico (Oppenheim et al., 2005).

**Real-world usage examples**

El OTP fue utilizado extensamente en comunicaciones diplomáticas y militares durante la primera mitad del siglo XX.

- Caso histórico: Proyecto Venona, donde se descifraron mensajes soviéticos por errores en la gestión de claves (NSA, 1996).

En la actualidad, su uso generalizado es raro debido a la dificultad de generar, distribuir y almacenar claves largas. Sin embargo, sigue aplicándose en comunicaciones altamente sensibles en contextos diplomáticos o experimentales (Zöllner et al., 1998; Ware, 1997).

---

## Part II: Practical Exercises

### Exercise 1: Caesar Cipher Analysis

**Given ciphertext:**
```
Al osk lzw twkl gx laewk, al osk lzw ogjkl gx laewk, al osk lzw syw gx oakvge, 
al osk lzw syw gx xggdakzfwkk, al osk lzw whguz gx twdawx, al osk lzw whguz gx 
afujwvmdalq, al osk lzw kwskgf gx Dayzl, al osk lzw kwskgf gx Vsjcfwkk, al osk 
lzw khjafy gx zghw, al osk lzw oaflwj gx vwkhsaj, ow zsv wnwjqlzafy twxgjw mk, 
ow zsv fglzafy twxgjw mk, ow owjw sdd ygafy vajwul lg Zwsnwf, ow owjw sdd ygafy 
vajwul lzw glzwj osq...
```

#### Step 1: Frequency Analysis

We start by counting the most frequent letters in the ciphertext. For this, we use the following Python code:

```python
from collections import Counter

def frequency_percentages(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]  # ignore spaces and symbols
    total = len(letters)
    freq = Counter(letters)

    print("=== Frecuencia de letras en % (ordenadas) ===")
    for letter, count in freq.most_common():  # sorted by frequency
        percentage = (count / total) * 100
        print(f"{letter}: {percentage:.2f}%")

ciphertext = """Al osk lzw twkl gx laewk, al osk lzw ogjkl gx laewk, 
al osk lzw syw gx oakvge, al osk lzw syw gx xggdakzfwkk, 
al osk lzw whguz gx twdawx, al osk lzw whguz gx afujwvmdalq, 
al osk lzw kwskgf gx Dayzl, al osk lzw kwskgf gx Vsjcfwkk, 
al osk lzw khjafy gx zghw, al osk lzw oaflwj gx vwkhsaj, 
ow zsv wnvjqlzafy twxgjw mk, ow zsv fglzafy twxgjw mk, 
ow owjw sdd ygafy vajwul lg Zwsnwf, ow owjw sdd ygafy 
vajwul lzw glzwj osq..."""

frequency_percentages(ciphertext)
```

The output shows the frequency distribution (excerpt):
```
w: 14.7%
l: 10.6%
k: 8.7%
g: 8.4%
a: 8.1%
...
```

#### Step 2: Determining the Key

The most frequent ciphertext letter is `w`.
In English, the most frequent letter is `e`.
Therefore we assume:

$$w \rightarrow e$$

Positions in the alphabet:

$$w = 22, \quad e = 4$$

So the key is:

$$22 - 4 = 18$$

#### Step 3: Decryption with Key = 18

We test this shift with the following Python code:

```python
def caesar_decrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new_char = chr((ord(ch) - base - shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(ch)
    return "".join(result)

plaintext = caesar_decrypt(ciphertext, 18)
print("=== Texto descifrado ===")
print(plaintext)
```

#### Result

The decrypted text is:

> *It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way...*

#### Conclusion

**The Caesar cipher key is: 18**

---

### Exercise 2: Affine Cipher Implementation

The Affine cipher uses the formula: $E(x) = (ax + b) \bmod 26$

**Given:** Plaintext = `CRYPTOGRAPHY`, $a = 5$, $b = 8$

#### a) Cifrado (primeras 3 letras)

Usamos $A=0, B=1,\ldots,Z=25$.

$$\begin{aligned}
\textbf{C}:&\ x=2 \quad\Rightarrow\quad y=(5\cdot2+8)=18 \pmod{26} \;\Rightarrow\; \textbf{S}\\[6pt]
\textbf{R}:&\ x=17 \quad\Rightarrow\quad y=(5\cdot17+8)=93 \equiv 15 \pmod{26} \;\Rightarrow\; \textbf{P}\\[6pt]
\textbf{Y}:&\ x=24 \quad\Rightarrow\quad y=(5\cdot24+8)=128 \equiv 24 \pmod{26} \;\Rightarrow\; \textbf{Y}
\end{aligned}$$

El cifrado completo resulta: `SPYFZAMPIFRY`

#### b) Clave de descifrado (Algoritmo de Euclides)

$$\gcd(26,5) = 1$$

$$26 = 5 \cdot 5 + 1$$

$$1 = 26 - 5(5)$$

Por lo tanto:

$$a^{-1} \equiv 21 \pmod{26}$$

**Verificación:** $5\cdot 21 = 105 \equiv 1 \pmod{26}$.

Entonces:
$$D(y) = 21(y-8) \pmod{26}$$

#### c) Verificación por descifrado (primeras 3 letras)

Aplicamos $D(y)=21(y-8)\pmod{26}$:

$$\begin{aligned}
\textbf{S}:&\ y=18 \Rightarrow D(y)=21(18-8)=210 \equiv 2 \pmod{26} \Rightarrow \textbf{C}\\[6pt]
\textbf{P}:&\ y=15 \Rightarrow D(y)=21(15-8)=147 \equiv 17 \pmod{26} \Rightarrow \textbf{R}\\[6pt]
\textbf{Y}:&\ y=24 \Rightarrow D(y)=21(24-8)=336 \equiv 24 \pmod{26} \Rightarrow \textbf{Y}
\end{aligned}$$

#### d) Número de claves válidas

$a$ debe ser coprimo con $26$ $\Rightarrow$ $a\in\{1,3,5,7,9,11,15,17,19,21,23,25\}$ (12 valores).

$b$ puede ser cualquier valor $0\dots 25$ (26 valores).

$$\boxed{12\times 26 = 312\ \text{claves válidas}}$$

---

### Exercise 3: Perfect Secrecy Analysis

Consider a simple cipher that operates on single bits where:
- Key space: $\{0, 1\}$
- Plaintext space: $\{0, 1\}$
- Encryption: $C = P \oplus K$ (XOR operation)
- Each key is chosen with probability $\frac{1}{2}$

#### a) Matriz de Cifrado Completa

La matriz de cifrado completa mostrando todas las combinaciones posibles de (texto plano, clave, texto cifrado):

| Texto Plano (P) | Clave (K) | Texto Cifrado (C = P ⊕ K) |
|-----------------|-----------|---------------------------|
| 0               | 0         | 0                         |
| 0               | 1         | 1                         |
| 1               | 0         | 1                         |
| 1               | 1         | 0                         |

#### b) Calcular P(C=0) y P(C=1)

Dado que las claves se eligen uniformemente con probabilidad $\frac{1}{2}$ cada una, y asumiendo distribución uniforme de textos planos:

De la matriz de cifrado:
- $C = 0$ ocurre cuando $(P=0, K=0)$ o $(P=1, K=1)$
- $C = 1$ ocurre cuando $(P=0, K=1)$ o $(P=1, K=0)$

Por lo tanto:

$$\begin{aligned}
P(C=0) &= P(P=0) \cdot P(K=0) + P(P=1) \cdot P(K=1) \\
&= \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{2}
\end{aligned}$$

$$\begin{aligned}
P(C=1) &= P(P=0) \cdot P(K=1) + P(P=1) \cdot P(K=0) \\
&= \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{2}
\end{aligned}$$

#### c) Calcular P(P=0|C=0) y P(P=1|C=0)

Usando el teorema de Bayes:

$$P(P=0|C=0) = \frac{P(C=0|P=0) \cdot P(P=0)}{P(C=0)}$$

De la matriz de cifrado, $P(C=0|P=0) = P(K=0) = \frac{1}{2}$

$$P(P=0|C=0) = \frac{\frac{1}{2} \cdot \frac{1}{2}}{\frac{1}{2}} = \frac{1}{2}$$

Similarmente:

$$P(P=1|C=0) = \frac{P(C=0|P=1) \cdot P(P=1)}{P(C=0)} = \frac{\frac{1}{2} \cdot \frac{1}{2}}{\frac{1}{2}} = \frac{1}{2}$$

#### d) Análisis de Secreto Perfecto

Según la definición de Shannon, un cifrado logra secreto perfecto si:

$$P(P=p|C=c) = P(P=p) \text{ para todo } p \in \mathcal{P}, c \in \mathcal{C}$$

De nuestros cálculos:
- $P(P=0|C=0) = \frac{1}{2} = P(P=0)$ ✓
- $P(P=1|C=0) = \frac{1}{2} = P(P=1)$ ✓

Por simetría, lo mismo se cumple para $C=1$:
- $P(P=0|C=1) = \frac{1}{2} = P(P=0)$ ✓
- $P(P=1|C=1) = \frac{1}{2} = P(P=1)$ ✓

**Conclusión:** Sí, este cifrado logra secreto perfecto porque la probabilidad de cualquier texto plano dado cualquier texto cifrado es igual a la probabilidad a priori de ese texto plano.

#### e) Impacto de la Reutilización de Claves

Si reutilizamos la clave para múltiples bits, el secreto perfecto se **pierde**. Esto se debe a:

Considere cifrar dos bits $P_1P_2$ con la misma clave $K$:
- $C_1 = P_1 \oplus K$
- $C_2 = P_2 \oplus K$

Un atacante puede calcular: 

$$C_1 \oplus C_2 = (P_1 \oplus K) \oplus (P_2 \oplus K) = P_1 \oplus P_2$$

Esto revela información sobre la relación entre textos planos, violando el secreto perfecto. El espacio de claves se vuelve efectivamente más pequeño en relación al espacio de mensajes, rompiendo el requisito fundamental de que $|\mathcal{K}| \geq |\mathcal{M}|$ para el secreto perfecto.

---

### Exercise 4: Entropy and Key Analysis

#### Scenario A: Sistema de Contraseñas
- Las contraseñas tienen exactamente 4 caracteres de longitud
- Cada carácter se elige uniformemente de $\{A, B, C, D\}$

#### Scenario B: Cifrado de Vigenère
- Longitud de clave = 3
- Cada carácter de la clave se elige uniformemente del alfabeto de 26 letras

#### a) Entropía para el Escenario A

Número total de contraseñas posibles: $4^4 = 256$

Entropía en bits:

$$\begin{aligned}
H_A &= \log_2(256) = \log_2(4^4) = 4 \log_2(4) = 4 \times 2 = 8 \text{ bits}
\end{aligned}$$

#### b) Entropía para el Escenario B

Número total de claves posibles: $26^3 = 17,576$

Entropía en bits:

$$\begin{aligned}
H_B &= \log_2(17,576) = \log_2(26^3) = 3 \log_2(26) \approx 3 \times 4.7 = 14.1 \text{ bits}
\end{aligned}$$

#### c) Tiempo para Romper Cada Sistema

Tasa de ataque: 1000 claves por segundo

**Escenario A (caso peor):**

$$\text{Tiempo} = \frac{256 \text{ claves}}{1000 \text{ claves/seg}} = 0.256 \text{ segundos}$$

**Escenario B (caso peor):**

$$\text{Tiempo} = \frac{17,576 \text{ claves}}{1000 \text{ claves/seg}} = 17.576 \text{ segundos} \approx 17.6 \text{ segundos}$$

#### d) Cálculo de la Distancia de Unicidad

Dados:
- Entropía del texto en inglés: 1.5 bits por carácter
- Longitud de clave de Vigenère: 3 caracteres
- Entropía de la clave: $3 \log_2(26) \approx 14.1$ bits

La distancia de unicidad $n_0$ es la cantidad de texto cifrado necesaria para determinar únicamente la clave:

$$n_0 = \frac{H(K)}{D} = \frac{\text{Entropía de la clave}}{\text{Redundancia por carácter}}$$

Donde redundancia por carácter = $\log_2(26) - 1.5 = 4.7 - 1.5 = 3.2$ bits/carácter

$$n_0 = \frac{14.1}{3.2} \approx 4.4 \text{ caracteres}$$

**Conclusión:** Teóricamente, se necesitarían aproximadamente 5 caracteres de texto cifrado en inglés para determinar únicamente una clave de Vigenère de 3 caracteres, asumiendo que se conocen las propiedades estadísticas del inglés.

---

## Referencias

Acharya, B., Panigrahy, S. K., Patra, S. K., & Panda, G. (2009). Image encryption using advanced Hill cipher algorithm. *International Journal of Recent Trends in Engineering, 1*(1), 663--667.

Aliyu, A. A. M., & Olaniyan, A. (2016). Vigenere cipher: Trends, review and possible modifications. *International Journal of Computer Applications, 135*(11), 46--50.

Bellovin, S. M. (2011). Frank Miller: Inventor of the one-time pad. *Cryptologia, 35*(3), 203--222. https://doi.org/10.1080/01611194.2011.583711

Dalal, Y. M., Raj, S. N., Supreeth, S., Shruthi, G., Yerriswamy, T., & Biradar, A. (2023). Comparative approach to secure data over cloud computing environment. In *2023 7th International Conference on Computational Systems and Information Technology for Sustainable Solutions (CSITSS)*. IEEE. https://doi.org/10.1109/CSITSS60515.2023.10334187

Dooley, J. F. (2018). Cryptology before 1500 -- A bit of magic. In *History of Cryptography and Cryptanalysis. History of Computing*. Springer, Cham. https://doi.org/10.1007/978-3-319-90443-6_2

Duarte Rizo, J. H., Makis Coleman, R. J., & Tórrez Martínez, J. A. (2023). *Análisis de la eficiencia del algoritmo de César y RSA para encriptar mensajes de texto* (Tesis doctoral).

Fernández, S. (2004). La criptografía clásica. *Sigma, 24*(24), 119--141.

Glantz, E. (2011). Guide to Civil War Intelligence. Journal of U.S Intelligence Studies.

Gómez, S., Arias, J. D., & Agudelo, D. (2012). Cripto-análisis sobre métodos clásicos de cifrado. *Scientia et Technica, 2*(50), 97--102.

Hasoun, R. K., Khlebus, S. F., & Tayyeh, H. K. (2021). A new approach of classical Hill cipher in public key cryptography. *International Journal of Nonlinear Analysis and Applications, 12*(2), 1071--1082.

Hoobi, M. M. (2025, March). Enhanced rail-fence cryptography algorithm using hybrid models. In AIP Conference Proceedings (Vol. 3264, No. 1, p. 030004). AIP Publishing LLC. https://doi.org/10.1063/5.0258471

Jagetiya, A., & Krishna, C. R. (2020). Evolution of Information Security Algorithms. Design and Analysis of Security Protocol for Communication, 29-77. https://doi.org/10.1002/9781119555759.ch2

Jones, J. (2016). A columnar transposition cipher in a contemporary setting. *Cryptology ePrint Archive.*

Kang, D., & Lee, J. (2024). A robust decryption technique using letter frequency analysis for short monoalphabetic substitution ciphers. *Journal of Computing Science and Engineering, 18*(3), 144--151.

Kazemi, M., Naraghi, H., & Golshan, H. M. (2011, November). On the affine ciphers in cryptography. In *International Conference on Informatics Engineering and Information Science* (pp. 185--199). Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-25327-0_17

Kester, Q. A. (2013). A hybrid cryptosystem based on Vigenere cipher and columnar transposition cipher. *arXiv preprint* arXiv:1307.7786.

Lasry, G., Kopal, N., & Wacker, A. (2016). Cryptanalysis of columnar transposition cipher with long keys. *Cryptologia, 40*(4), 374--398. https://doi.org/10.1080/01611194.2015.1087074

Mason, J., Stolfo, S., Stolfo, D., & Stolfo, D. (2016). A natural language approach to automated cryptanalysis of the two-time pad. In *Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (CCS)* (pp. 179--190). https://doi.org/10.1145/2976749.2978394

Mokhtari, M., & Naraghi, H. (2012). Analysis and design of affine and Hill cipher. *Journal of Mathematics Research, 4*(1), 67.

Oppenheim, J., Horodecki, M., & Horodecki, P. (2005). Mutually unbiased bases and recycling of one-time pads in quantum cryptography. *Physical Review A, 72*(4), 042309. https://doi.org/10.1103/PhysRevA.72.042309

Pelosi, G., & Selleri, S. (2021, November). Florence and a leap in cryptography: The Leon Battista Alberti cypher disk. In *2021 7th IEEE History of Electrotechnology Conference (HISTELCON)* (pp. 7--11). IEEE.

Shannon, C. E. (1949). Communication theory of secrecy systems. *Bell System Technical Journal, 28*(4), 656--715. https://doi.org/10.1002/j.1538-7305.1949.tb00928.x

Siahaan, A. P. U. (2016). Rail fence cryptography in securing information. *International Journal of Scientific & Engineering Research, 7*(7), 535--538.

U.S. National Security Agency (NSA). (1996). *The Venona story*. *Cryptologic Spectrum*. National Security Agency Central Security Service.

Ware, W. H. (1997). *Security controls for computer systems: Report of the Defense Science Board Task Force on Computer Security*. RAND Corporation.

Xipell Solans, P. (2009). *Antecedentes y perspectivas de estudio en historia de la criptografía* (Proyecto de fin de carrera, Universidad Carlos III de Madrid). e-Archivo UC3M. https://e-archivo.uc3m.es/handle/10016/7748

Zöllner, J., Federrath, H., Klimant, H., Pfitzmann, A., Westfeld, A., Wicke, P., & Bäuml, G. (1998). Modeling the security of steganographic systems. *Lecture Notes in Computer Science, 1525,* 344--354. https://doi.org/10.1007/3-540-49380-8_25