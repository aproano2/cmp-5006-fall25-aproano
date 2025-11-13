# Homework 2

# Fabián De La Cruz y Roberth Lara

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

## Answers to question 1.

### Mechanism 1:

Mechanism 1 fails as a digital signature scheme because it does not provide public verifiability or non-repudiation. In a proper digital signature system, anyone who receives the message should be able to verify the signature using the signer’s public key. In this symmetric-key proposal, only the signer can verify the signature because only the signer can decrypt it. This means the recipient must return the signature to the signer to confirm it, which defeats the entire purpose of a digital signature. It also allows the recipient to forge signatures, since both parties share the same key. As a result, the signer cannot later prove that they were not the one who signed a message, and the recipient cannot prove to a third party that the signer actually created it. Because of this, the mechanism completely loses the core security properties expected of digital signatures.

### Mechanism 2:

Mechanism 2 also deviates from the standard protocol but in a different way. Instead of signing a hash of the message, the signer encrypts the entire message with their private key, expecting others to decrypt it with the public key. While verification still works, this approach is highly inefficient and provides no confidentiality, since anyone with the public key can read the message. Digital signature algorithms are designed to operate on a short digest, not to encrypt large amounts of data, so using them to transform the entire message is both unnecessary and potentially unsafe. This method wastes computation and violates the intended design of signature schemes, which aim to prove authenticity and integrity without turning the private key into a general purpose encryption tool.

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

## Answers to question 2.

### Scenario 1:

In Scenario 1 Oscar’s tampering exploits a situation where the signature does not cover the full, relevant transaction data or the receiver fails to verify the signature against the received message. If the signature is properly computed over the entire message and Bob actually verifies the signature, Bob will detect the alteration because the recomputed hash of the modified message will not match the decrypted hash from the signature. If, however, the signer only signed part of the data or Bob neglects verification, Oscar’s modification goes unnoticed. Simple cryptographic defenses are: always sign the complete transaction and make signature verification mandatory before executing any action, also, use certificates to bind public keys to identities and transport integrity protections so on-the-wire tampering is harder.

### Scenario 2:

In Scenario 2 Oscar performs a replay attack by resending a previously valid message and signature multiple times. If the system accepts any correctly signed message without checking whether it’s fresh or already processed, Oscar can cause duplicate transactions. Defenses against replay are straightforward and commonly used: include a freshness element in the signed data such as a timestamp plus an allowed time window, a one time nonce or unique transaction identifier, and/or maintain server-side state of processed IDs so duplicates are rejected. Combining these with proper signatures would prevent Oscar from simply replaying an old signed message to cause harm.

## 3. Research: Transport Layer Security (TLS 1.3)

Provide a detailed analysis of the TLS 1.3 protocol. Focus on the following areas:
- The architecture of TLS, and its evolution over the last few years
- Cryptographic primitives that are being used
- How the core goals of confidentiality, integrity, and authentication are being satisfied
- Explain the modern applications in which TLS is being used

## Response to question 3.

**Architecture and evolution:** TLS 1.3 is the newest version of the Transport Layer Security protocol, designed to secure communication between two parties over the internet. Earlier versions of TLS contained many optional features and older cryptographic methods, which made them slower and sometimes vulnerable. TLS 1.3 simplified the architecture by removing outdated mechanisms, reducing the number of messages needed to establish a secure connection, and encrypting most of the handshake. This makes connections faster, easier to analyze, and more secure by default.

**Cryptographic primitives:** TLS 1.3 uses a small, modern set of cryptographic tools. For key exchange, it relies on ephemeral Diffie-Hellman, which creates a fresh key for every session. For encryption, it uses secure “AEAD” algorithms such as AES-GCM or ChaCha20-Poly1305, which protect confidentiality and integrity at the same time. It also uses hash functions such as SHA-256 for creating and managing keys, and digital signatures like RSA-PSS or ECDSA for authenticating servers.

**Confidentiality, integrity, and authentication:** TLS 1.3 protects confidentiality by encrypting all data exchanged between the client and server using keys that are unique to each session. Integrity is maintained because the AEAD algorithms detect any tampering or modification of the data in transit. Authentication is provided through digital certificates, which allow the client to confirm that it is truly communicating with the legitimate server. Together, these features prevent eavesdropping, message manipulation, and impersonation.

**Modern applications:** TLS 1.3 is widely used across today’s internet. It protects HTTPS connections used by websites, online banking, and e-commerce. It secures communication for mobile apps, APIs, cloud services, and many email protocols. It is also used in modern transport technologies like HTTP/2, HTTP/3, and QUIC. Essentially, almost all secure web and application traffic today relies on TLS 1.3 to protect users’ data.


## 4. Design Problem

Design an architecture for a system that requires strong, verifiable, and legally enforceable non-repudiation, utilizing cryptographic principles alongside robust protocol design.

### Scenario: 

The application is a Secure Electronic Contract Signing System (SECS). Two parties, Alice (Service Provider) and Bob (Client), must execute a critical digital contract (e.g., an intellectual property license). The system must guarantee Non-Repudiation of Origin (neither party can deny signing the contract) and Non-Repudiation of Submission/Receipt (neither party can deny receiving the final signed contract). This is vital for maintaining the trustworthiness and legal enforceability of the digital transaction.

## Response to question 4.

SECS relies on a Public Key Infrastructure where both Alice and Bob have legally recognized digital certificates issued by a trusted Certificate Authority. These certificates link their identities to their public keys, allowing their digital signatures to serve as legally enforceable proof of authorship.

The system creates a fixed, final version of the contract and computes a hash of it. Alice signs this hash with her private key, producing a digital signature that proves she is the origin of the signature. Bob receives the exact same contract, verifies Alice’s signature, and then signs the same hash with his own private key. Both signatures are time-stamped by a trusted time-stamping service to prove when the signatures occurred.

Whenever the system delivers a signed document from one party to the other, it generates a signed receipt confirming who received it and when. The system signs these receipts itself, ensuring that each delivery can be proven later. Bob also signs an acknowledgment when he receives Alice’s signature, and the system stores these acknowledgments as evidence.

All messages travel over TLS 1.3 to prevent tampering. The system keeps append-only audit logs and stores all signatures, timestamps, and receipts together with the contract so anyone can verify them later. This ensures both parties cannot deny signing the contract or deny receiving the final signed version.