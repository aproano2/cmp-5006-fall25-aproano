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

Mechanism 1 may look workable at first glance, but once you think through what makes a digital signature useful, it starts breaking down. The biggest issue is that nothing can be verified independently. Only the signer can decrypt the “signature”, which forces the recipient to hand it back to them just to check if it’s real. That already feels like a red flag, because now the signer controls the entire verification process.

There is also a deeper problem that is easy to overlook: since both parties share the same key, either one could generate a signature and later claim the other did it. A system that allows that kind of ambiguity is unlikely to offer non repudiation in any meaningful sense. In a real signature scheme, you want anyone, even a third party, to verify authenticity without involving the signer at all. This mechanism simply doesn’t get there, and it opens the door to forgery, denial, and disputes that would be impossible to resolve.

### Mechanism 2:

Mechanism 2 goes in a different direction, but it still departs from how signature schemes are supposed to work. Encrypting the entire message with the private key may appear to “prove” authorship, but it turns the signature operation into an expensive and somewhat awkward process. Signature algorithms are designed to handle a small digest, not full documents, and using them as general purpose encryptors introduces unnecessary cost and possibly new attack surfaces.

Another detail that stands out is that confidentiality disappears entirely. Anyone with the public key can decrypt the message, so whatever sense of privacy one might expect simply isn’t there. Even though the mechanism technically validates integrity, it does so in a way that feels brittle and out of line with the intended design of asymmetric signature systems.

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

Whether Bob catches Oscar’s modification depends on how carefully the system was built. If the signature truly covers the full message and Bob actually checks it, the altered instruction would fail verification immediately. The hash Bob computes from the modified message wouldn’t match the hash extracted from the signature, so the change is caught right away.

Still, practical systems sometimes cut corners, intentionally or not. If the signature only protects part of the message, or Bob skips verification because he trusts the source or the channel, Oscar’s tampering might slip by unnoticed. That kind of oversight appears simple but is likely to lead to serious problems. The safest approach is to always sign the entire transaction and enforce signature verification before taking any action on the message.

### Scenario 2:

In this scenario Oscar isn’t altering anything; he is replaying a valid signed message over and over. If the system only checks that the signature is mathematically correct, it might treat each replay as a fresh instruction. This is a classic replay attack and shows up in systems that don’t track the freshness or uniqueness of messages.

Preventing this doesn’t require anything exotic. Including timestamps, nonces, or transaction IDs that the server remembers is usually enough to block repeated submissions. If those elements are part of what gets signed, Oscar can’t forge them or reuse them without being detected. Without these checks, though, the system is likely to accept duplicates without realizing they’re old copies.

## 3. Research: Transport Layer Security (TLS 1.3)

Provide a detailed analysis of the TLS 1.3 protocol. Focus on the following areas:
- The architecture of TLS, and its evolution over the last few years
- Cryptographic primitives that are being used
- How the core goals of confidentiality, integrity, and authentication are being satisfied
- Explain the modern applications in which TLS is being used

## Response to question 3.

**Architecture and evolution:** TLS 1.3 is the most recent iteration of the Transport Layer Security protocol, but it didn’t appear out of nowhere. It grew out of years of patchwork in earlier versions, which had accumulated a mix of optional features, legacy ciphers, and frankly a few mechanisms that felt more like historical leftovers than security tools. Those older designs often made connections slower and, at times, a bit shaky from a security perspective. TLS 1.3 trims much of that baggage. By cutting outdated components, shrinking the handshake down to fewer messages, and encrypting most of the negotiation itself, the protocol feels noticeably cleaner. Connections tend to load faster, and the whole system appears easier to reason about, even for someone who’s not deep into protocol analysis.

**Cryptographic primitives:** Instead of the long menu of cryptographic options from its predecessors, TLS 1.3 sticks to a smaller, more modern toolkit. Key exchange relies on ephemeral Diffie Hellman, which essentially means every session gets its own fresh keys rather than reusing long-term secrets. It may seem like a small tweak, but it sharply improves forward secrecy. For encryption, the protocol leans on AEAD algorithms such as AES GCM and ChaCha20 Poly1305. Both are designed to keep data confidential while simultaneously making sure that any tampering is obvious. The protocol also uses strong hashing functions like SHA 256 for key material, and server authentication typically involves RSA PSS or ECDSA, depending on the certificate. The whole setup feels like a deliberate move toward simplicity and hardening.

**Confidentiality, integrity, and authentication:** TLS 1.3 handles confidentiality by encrypting everything that travels between the client and server using ephemeral session keys, so each connection remains isolated from the next. Integrity comes from the built in authentication features of AEAD encryption, which detect even subtle bit flips during transmission. Authentication still relies on digital certificates, and while the certificate ecosystem isn’t perfect, it allows the client to check that it’s speaking to the server it actually intended to reach. When all of these pieces work together, they make passive eavesdropping, silent message edits, and basic impersonation attacks much harder to pull off.

**Modern applications:** At this point, TLS 1.3 sits quietly behind most of what we do on the internet. Anytime you open a banking site, submit a payment on an e commerce platform, or even load social media over HTTPS, there’s a good chance this protocol is running in the background. Mobile apps also depend on it heavily, especially those that constantly exchange data with cloud APIs. And with the rise of HTTP 2, HTTP 3, and QUIC, TLS 1.3 has essentially become part of the transport layer itself. Nearly all secure traffic these days either uses it directly or is built on something that does, even if most users never notice it’s there.


## 4. Design Problem

Design an architecture for a system that requires strong, verifiable, and legally enforceable non-repudiation, utilizing cryptographic principles alongside robust protocol design.

### Scenario: 

The application is a Secure Electronic Contract Signing System (SECS). Two parties, Alice (Service Provider) and Bob (Client), must execute a critical digital contract (e.g., an intellectual property license). The system must guarantee Non-Repudiation of Origin (neither party can deny signing the contract) and Non-Repudiation of Submission/Receipt (neither party can deny receiving the final signed contract). This is vital for maintaining the trustworthiness and legal enforceability of the digital transaction.

## Response to question 4.

A system like SECS needs to do more than attach signatures to a file; it has to provide evidence that will hold up in a legal or contractual setting. Using a Public Key Infrastructure is a natural foundation since certificates bind each party’s identity to their public key in a way that can be independently verified.

When the contract is ready, the system freezes its contents and computes a hash of that final version. Alice signs this hash with her private key. Bob then receives the document and, before doing anything else, verifies Alice’s signature to ensure nothing was changed along the way. Once he confirms the document is intact, he signs the same hash using his own private key. At this point, both signatures refer to the exact same content.

Adding a trusted timestamp may feel like a small detail, but it becomes important when proving when the signatures occurred. The system can also issue digitally signed receipts whenever a document changes hands, creating a trail that later helps resolve disputes. Bob’s acknowledgment of Alice’s signature becomes part of this trail, and the system stores everything in an append only audit log that no one can alter without being detected.

All communication runs through TLS 1.3, which protects the whole process from interception or tampering. By storing contracts, signatures, timestamps, and receipts together, the system provides strong evidence that neither party can realistically deny signing or receiving the final version.