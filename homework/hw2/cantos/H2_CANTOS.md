# Homework 2 -- Information Security

**Student:** Paulo Cantos 326682 13/11/2025

------------------------------------------------------------------------

## 1. Standard Digital Signature Protocol Review

## 1.1 Mechanism 1 -- Critique

(Signing using a symmetric key and verification by returning the
signature to the signer)

This mechanism replaces public‑key cryptography with a shared symmetric
key. The signer generates a supposed "signature" by encrypting the hash
of the message with that key, but the receiver cannot verify it
independently and must send it back to the signer for confirmation. In
simple terms... both parties share the same secret key and then expect
that key to prove who used it, which is impossible. This mechanism looks
tempting but fundamentally breaks non‑repudiation.

### Security properties that break

**Non‑repudiation:**\
Since both parties know the symmetric key, either one can generate the
"signature." The receiver could fabricate it as well. Furthermore,
because verification depends on the signer, the signer may deny having
confirmed the signature or claim that their key was compromised. There
is no evidence verifiable by a third party.

**Independent verification:**\
In a real digital signature, anyone with the public key can verify the
signature without interacting with the signer. Here, only the signer can
validate it, turning them into a verification oracle.

**Transferability of proof:**\
A signature must be presentable to an auditor or authority to prove
authenticity. This mechanism does not allow that because no third party
can verify anything without the signer.

**Separation of roles:**\
Since all parties who know the key can generate "signatures," there is
no distinction between signer and verifier. This is not a digital
signature but a misapplied MAC.

### Why this is not a real digital signature

This mechanism seems logical at first, but... it collapses as soon as we
remember how real digital signatures work. A digital signature must use
asymmetric keys, allow verification without interaction with the signer,
and offer non‑repudiation. The basic idea---and I repeat it because it's
easy to forget in the middle of so much theory---is this: if both
parties share the same key, the concept of a signature dissolves. This
mechanism fails on all three points: it uses a symmetric key, requires
interaction, and does not guarantee non‑repudiation.

### Possible attacks

-   The signer can deny having validated the signature.\
-   The receiver can forge signatures.\
-   The signer can be abused as a decryption oracle, recycling
    confirmations without control, chaining multiple attacks together.

------------------------------------------------------------------------

## 1.2 Mechanism 2 -- Critique

(Encrypting the entire message with the private key as a "signature")

In this mechanism, the signer encrypts the entire message with their
private key and the receiver uses the public key to decrypt it and
assume authenticity at the same time. We see this a lot in introductory
digital‑signature discussions because "encrypt with the private key"
sounds tempting without noticing the consequences.

### Why the mechanism is incorrect

**Confuses encryption with signing:**\
Encrypting with the private key does not provide confidentiality because
anyone can decrypt with the public key. Digital signatures do not
encrypt the full message; they sign the hash of the message.

**Incompatible with modern algorithms:**\
RSA, ECDSA, and other schemes do not sign by encrypting the entire
message. They always sign the hash. Also, RSA cannot encrypt large
messages directly.

**Inefficient and impractical:**\
Asymmetric encryption is not designed for large amounts of data.
Attempting to "sign" by encrypting the whole message breaks size limits
and makes the process slow and insecure.

### Properties that break

-   No confidentiality: anyone with the public key can read the entire
    message.\
-   Integrity and compatibility are weakened because no hashing is used
    and no standard formats are followed.\
-   Authentication and content delivery merge into one operation, so no
    roles remain clearly separated.

### Vulnerabilities introduced

-   Large messages don't fit in RSA.\
-   Risk of known padding attacks.\
-   Greater exposure of the private key by using it to encrypt too much
    data.\
-   Verification depends on interpreting content, which can be
    dangerous.\
-   Increased exposure to side‑channel attacks because the private key
    processes arbitrary inputs sent by whoever performs verification.

### Why the hash must be signed

Signing the hash makes the process efficient, secure, and compatible
with standards. The hash completely changes if a single bit of the
message is altered and has fixed size, allowing signatures of
arbitrarily large files. The key idea here is that we do not sign the
entire document, but a small fingerprint that exactly represents it.

------------------------------------------------------------------------

## General Conclusion

Both mechanisms fail because they do not follow the fundamental
principle of digital signatures: using asymmetric cryptography and
signing only the hash of the message. Both break essential properties
and do not meet the minimal requirements of a real digital signature.

------------------------------------------------------------------------

## 2. Vulnerability to Attack Vectors

## 2.1 Scenario 1 -- Message alteration

Alice signs the message "Transfer \$1000 to Mark" and sends the pair (x,
auth(x)) to Bob. Oscar intercepts the transmission and changes the
content to "Transfer \$1000 to Oscar," attempting to reuse the same
signature.

### Does Bob detect the alteration?

Yes, he does. What happens is that the digital signature is
mathematically bound to the exact hash of the original message. The real
signature process is:

σ = Sign_sk(H(x))

When Bob receives the modified message:

1.  He computes the hash of the received message H(x_received).\
2.  He verifies the signature with Alice's public key: Verify_pk(σ,
    H(x_received)).

Since the content changed, the hash changes completely, and the
signature no longer matches. Verification fails.

### Properties protecting this scenario

**Integrity:** any modification invalidates the signature.\
**Authenticity:** only Alice's private key can generate a valid
signature.\
**Non‑repudiation:** Alice cannot deny having signed the original
message.

### Vulnerability Oscar attempts to exploit

Oscar attempts a message‑manipulation attack: changing the content and
reusing the signature. With a modern hash + signature scheme, this does
not work.

### How the hash + signature scheme prevents this

-   The hash produces a unique fingerprint.\
-   A single changed bit results in a totally different hash.\
-   Oscar cannot find another input with the same hash or generate a new
    signature without the private key.

### When this system could fail

This attack could work only if the system were poorly designed:

-   If the message is signed without hashing.\
-   If an insecure hash (MD5, SHA‑1) is used.\
-   If only part of the message is signed.\
-   If RSA is used without proper padding ("raw RSA").

A side note: in a lab everything looks perfect, but forgetting to sign a
metadata field or version number is enough to make this scenario
vulnerable again.

------------------------------------------------------------------------

## 2.2 Scenario 2 -- Replay Attack

Oscar intercepts the valid pair (x, auth(x))---for example, "Transfer
\$1000 to Mark"---and resends it without modification multiple times to
Bob.

### Does the signature verify each time?

Yes. If Oscar sends exactly the same pair, the signature remains valid.
Digital signatures ensure integrity and authenticity but not freshness
or uniqueness. This attack happens constantly if no nonces are used.

### Name of the attack

Replay Attack.

### Why this is a problem if Bob processes everything

If Bob processes each replay, he would execute the same signed
transaction multiple times. In practice, Bob would end up debiting
multiple transfers before noticing. Alice would be "authorizing"
multiple transfers unintentionally. This is not a failure of the
signature but of the protocol using the signature.

### Why the digital signature alone does not prevent this

The signature guarantees:

-   the message comes from Alice,\
-   it was not modified.

But it does **not** guarantee:

-   the message is recent,\
-   it was not sent before,\
-   it should be processed only once,\
-   it is not being reused in another session.

A message signed today is still valid tomorrow unless the protocol adds
anti‑replay mechanisms.

### Mechanisms to prevent replay attacks

Real systems combine signatures with freshness mechanisms:

-   Nonces (unique random numbers per session).\
-   Timestamps.\
-   Sequence numbers.\
-   Unique transaction IDs.\
-   A list of processed transactions to reject duplicates.

### Example of anti‑replay flow

Alice generates:

-   Message x\
-   Unique ID: txn_id\
-   Signature: σ = Sign_sk(H(x ∥ txn_id))

Sends to Bob: (x, txn_id, σ).

Bob verifies:

1.  The signature.\
2.  That txn_id has not been used before.

If Oscar replays the message:

-   The signature is valid.\
-   But the ID already exists → Bob rejects it.

It sounds repetitive, but Bob must check twice: first the signature,
then whether the identifier already exists.

------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Research: Transport Layer Security (TLS 1.3)

## 3.1 TLS architecture and evolution

TLS (Transport Layer Security) is a cryptographic protocol operating
above reliable transport (such as TCP) and below application‑layer
protocols (HTTP, SMTP, etc.). Its purpose is to provide an encrypted
channel that prevents eavesdropping, message manipulation, and
impersonation.

It does not fit neatly into the OSI model; it is typically described as
between the transport and application layers. I think the key idea is
understanding that "intermediate layer," because TLS is often sold as
black‑box magic when it really just wraps application traffic. We had
some difficulty deciding how much history to include, so if it sounds
repetitive, it's because we didn't want the reader to get lost among so
many layers and acronyms.

Internally, it is enough to remember that the Record Protocol carries
everything and that the Handshake negotiates algorithms and
authentication (alerts still exist, but listing them no longer adds much
value).

Historically, TLS evolved from SSL 2.0/3.0 (now insecure). TLS 1.0, 1.1,
and 1.2 added incremental improvements, but TLS 1.3 (RFC 8446, 2018)
represents a full redesign:

-   Reduces the handshake to 1 RTT and supports 0‑RTT for resumption.\
-   Eliminates insecure algorithms (static RSA, CBC, RC4, TLS
    compression, weak hashes).\
-   Requires forward secrecy with ephemeral (EC)DHE.\
-   Adopts HKDF for key derivation.

The result is a simpler, faster, and more secure protocol than TLS 1.2.
The idea is basically that TLS 1.3 kept the good parts and swept away
everything else.

------------------------------------------------------------------------

## 3.2 Cryptographic primitives in TLS 1.3

TLS 1.3 uses a more limited but modern set of primitives:

### Key exchange -- ephemeral (EC)DHE

The shared secret is generated using ephemeral Diffie--Hellman,
generally over elliptic curves (X25519, P‑256, etc.). Each connection
uses new keys, providing forward secrecy.

### Symmetric encryption -- AEAD

Only authenticated encryption with associated data (AEAD) is allowed:

-   AES‑GCM (128/256)\
-   ChaCha20‑Poly1305

These ciphers provide confidentiality and integrity in a single
operation using nonces and AAD. There is no room for vintage algorithms.

### Key derivation -- HKDF

TLS 1.3 uses HKDF to derive all keys from the (EC)DHE secret and the
transcript; no need to detal
