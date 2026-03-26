# TLS Handshake

## Core Goals (CIA Triad)

- **Confidentiality:** No snooping (Encryption).
- **Integrity:** No tampering (Hashing).
- **Authentication:** No imposters (Certificates).

## The Strategy

- **Asymmetric Encryption (Public/Private Key):** Slow but safe. Used _only_ during the handshake to exchange secrets.
- **Symmetric Encryption (Shared Key):** Fast and efficient. Used for the actual data transfer once the handshake is done.

---

## The Handshake Flow (Step-by-Step)

### Phase 1: The Greeting (Negotiation)

- **ClientHello:** "Here are the TLS versions and Cipher Suites I support. Here is my **Client Random** number."
- **ServerHello:** "I choose _this_ TLS version and _this_ Cipher Suite. Here is my **Server Random** number."

### Phase 2: Authentication (Trust)

- **Certificate Exchange:** Server sends its **Digital Certificate** (ID card).
- **Validation:** Client validates the certificate by checking the digital signature against the **Certificate Authority's (CA)** public key (Chain of Trust).

### Phase 3: Key Exchange (The Secret)

- **The Method:** Uses **ECDHE** (Elliptic Curve Diffie-Hellman Ephemeral).
- **The Process:**
  - Client and Server exchange public parameters ("Paint Buckets").
  - They combine these with their private secrets to calculate the **Pre-Master Secret**.
- The Calculation:
  $$Session Keys = Function(PreMasterSecret + ClientRandom + ServerRandom)$$

### Phase 4: Finishing (Locking it Down)

- **ChangeCipherSpec:** "Switching to encrypted mode now!"
- **Finished:** The first encrypted message. Contains a hash of the entire conversation to prove no one tampered with the handshake.

---

## TLS 1.2 vs. TLS 1.3

- **TLS 1.2:** Requires **2 Round Trips (2-RTT)**. "Hello" -> "Wait" -> "Key Exchange" -> "Wait" -> "Keys".
- **TLS 1.3:** Requires **1 Round Trip (1-RTT)**. The Client _guesses_ the key exchange method and sends its key share immediately in the _ClientHello_. Faster and more secure.
