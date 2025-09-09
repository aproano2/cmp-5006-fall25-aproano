# Homework Assignment: Classical Cryptography
**Course:** Information Security 

**General Instructions:** If you need to write a numerical analysis or a mathematical proof, take advantage of the Latex support that markdown (md) offers. Do not include photos or scans of your work done with pen and paper. 

## Part I: Research Component

### Task: Historical Cryptographic Algorithms Survey

Research and write a comprehensive reportcovering the most important classical cryptographic algorithms. Your report should include:

**Required Algorithms to Cover:**
1. **Substitution Ciphers**
   - Caesar Cipher (review from class)
   - Affine Cipher
   - Monoalphabetic Substitution
   - Polyalphabetic Substitution (Vigenère Cipher)

2. **Transposition Ciphers**
   - Columnar Transposition
   - Rail Fence Cipher

3. **Advanced Classical Systems**
   - Hill Cipher
   - One-Time Pad

**For Each Algorithm, Include:**
- Brief historical context and inventor/origin
- Description of the encryption/decryption process
- Key space size
- Known vulnerabilities and cryptanalysis methods
- Real-world usage examples (if any)


## Part II: Practical Exercises

### Exercise 1: Caesar Cipher Analysis

Given the following ciphertext encrypted with a Caesar cipher:
```
Al osk lzw twkl gx laewk, al osk lzw ogjkl gx laewk, al osk lzw syw gx oakvge, 
al osk lzw syw gx xggdakzfwkk, al osk lzw whguz gx twdawx, al osk lzw whguz gx 
afujwvmdalq, al osk lzw kwskgf gx Dayzl, al osk lzw kwskgf gx Vsjcfwkk, al osk 
lzw khjafy gx zghw, al osk lzw oaflwj gx vwkhsaj, ow zsv wnwjqlzafy twxgjw mk, 
ow zsv fglzafy twxgjw mk, ow owjw sdd ygafy vajwul lg Zwsnwf, ow owjw sdd ygafy 
vajwul lzw glzwj osq...
```

**Tasks:**
a) Decrypt the message using frequency analysis (show your work)
b) What is the key used?

### Exercise 2: Affine Cipher Implementation

The Affine cipher uses the formula: E(x) = (ax + b) mod 26

**Given:** Plaintext = "CRYPTOGRAPHY", a = 5, b = 8

**Tasks:**
a) Encrypt the plaintext (show calculations for first 3 letters)
b) Find the decryption key values (multiplicative inverse of a)
c) Verify your encryption by decrypting the first 3 letters
d) How many valid keys exist for the Affine cipher? Explain your reasoning.

### Exercise 3: Perfect Secrecy Analysis

Consider a simple cipher that operates on single bits where:
- Key space: {0, 1}
- Plaintext space: {0, 1}  
- Encryption: C = P ⊕ K (XOR operation)
- Each key is chosen with probability 1/2

**Tasks:**
a) Create the complete encryption matrix showing all possible (plaintext, key, ciphertext) combinations
b) Calculate P(C=0) and P(C=1)
c) Calculate P(P=0|C=0) and P(P=1|C=0)
d) Does this cipher achieve perfect secrecy? Prove your answer using Shannon's definition
e) What happens to perfect secrecy if we reuse the key for multiple bits?

### Exercise 4: Entropy and Key Analysis

Consider the following scenarios:

**Scenario A:** A password system where:
- Passwords are exactly 4 characters long
- Each character is chosen uniformly from {A, B, C, D}

**Scenario B:** A Vigenère cipher with:
- Key length = 3
- Each key character chosen uniformly from 26-letter alphabet

**Tasks:**
a) Calculate the entropy (in bits) for Scenario A
b) Calculate the entropy (in bits) for Scenario B  
c) If an attacker can test 1000 keys per second, how long would it take to break each system in the worst case?
d) Calculate the "unicity distance" concept: If English text has entropy ≈ 1.5 bits per character, how much ciphertext would theoretically be needed to uniquely determine a 3-character Vigenère key?


## Part III: Pico CTF

Five problems have been posted in the Pico CTF platform. For each problem, find the flags using two different methods. For each method:
- Provide an explanation on what technique was used to solve it
- Provide any code you used. If you need to apply brute-force, please write your own Python code to do so. Do not use online platforms.
- Provide screenshots showing that the platform accepted your flag.