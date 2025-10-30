# Homework 2

### Course: Information Security

### General Instructions: 

- If you need to write a numerical analysis or a mathematical proof, take advantage of the Latex support that markdown (md) offers. 
- Do not include photos or scans of your work done with pen and paper.
- Submit your assignment as a pull request to the class repository, in the "/homework/hw2" directory. Please create a folder that includes your last name to identify your submission

## 1. Standard Digital Signature Protocol Review

The standard, cryptographically robust protocol for creating a digital signature uses asymmetric cryptography combined with secure hashing to provide assurance of both origin authentication and integrity.
The process follows four steps:
- Digest Computation: A cryptographic hash function computes a short digest $H(M)$ of the original message $M$.
- Signing: The sender encrypts the hash value $H(M)$ using their own Private Key ($SK_{Signer}$). This encrypted hash is the signature ($Sig$).
- Transmission: The sender transmits the original message and the signature: $\{M, Sig\}$.
- Verification: The receiver decrypts $Sig$ using the sender's publicly available Public Key ($PK_{Signer}$) to recover the original hash value $H(M)$. The receiver then independently computes a hash $H(M')$ on the received message $M'$ and verifies that $H(M') = H(M)$. If they match, integrity and authentication are confirmed.
 

### Critique of Flawed Alternatives

Students must analyze two proposed alternative signature schemes that deviate from the standard protocol and detail which desirable properties are violated.


### Mechanism 1: 

This scheme proposes using a symmetric key scheme instead of Public Key Cryptography (PKC). To verify the signature, the recipient must give the signature back to the signer, who decrypts and checks it.

### Mechanism 2:

The signer encrypts the entire object $M$ with their private key, and the reader decrypts the entire resulting ciphertext using the signer's public key to both read and verify the content.

## 2. Vulnerability to Attack Vectors

In the following scenarion, Oscar is an adversary. Provide a detail analysis of the potential problems with each of them, the vulnerabilities that Oscar is exploiting, and the cryptographic solutions that can be used to address them. 


### Scenario 1:

Alice sends to Bob:
-  x = "Transfer \$1000 to Mark" 
- the corresponding digital signature $auth(x)$

Oscar intercepts the transmission and replaces the recipient, modifying the message to:
- x =  "Transfer \$1000 to Oscar". 

Will Bob detect this alteration?


### Scenario 2:

Oscar observes a valid transaction message $x$ ("Transfer \$1000 to Mark") and its authentic signature $auth(x)$. Oscar intercepts and retransmits this exact message and signature 100 times to Bob.

## 3. Research: Transport Layer Security (TLS 1.3)

Provide a detailed analysis of the TLS 1.3 protocol. Focus on the following areas:
- The architecture of TLS, and its evolution over the last few years
- Cryptographic primitives that are being used
- How the core goals of confidentiality, integrity, and authentication are being satisfied
- Explain the modern applications in which TLS is being used

## 4. Design Problem

Design an architecture for a system that requires strong, verifiable, and legally enforceable non-repudiation, utilizing cryptographic principles alongside robust protocol design.

### Scenario: 

The application is a Secure Electronic Contract Signing System (SECS). Two parties, Alice (Service Provider) and Bob (Client), must execute a critical digital contract (e.g., an intellectual property license). The system must guarantee Non-Repudiation of Origin (neither party can deny signing the contract) and Non-Repudiation of Submission/Receipt (neither party can deny receiving the final signed contract). This is vital for maintaining the trustworthiness and legal enforceability of the digital transaction.

