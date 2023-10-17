## indigenous-crypto-currency-investigation-tool

> idea:

1. at first we compare the public key with the pattern of different cryptocurrency.
2. after that we are decoding the given public key.
3. in the decoded form we are checking the 0th index pattern
4. we are getting the checksum from the decoded form and we are storing the rest in an array as
   hash160.
5. we are computing the checksum again from hash160 by encrypting it.
6. then we are checking the computed and the previous checksum is similar or not .
7. then we will verify if the public key is present in the blockchain of that currency or not, using
   different APIs.

> technology stack:

1. programming language: Python
2. front-end: Html, CSS, Bootstrap
3. back-end web framework: Django
4. database: SQLite
5. library: regular expression, base58check, hashlib etc
6. APIs: API from blockchain.com, coinapi, btc.com, coingecko etc
7. deployment: render / homeserver

> use cases:

1. checking a public key is valid or not.
2. show transaction details. Like final balance , number of
   transaction, total received etc.
3. currency value converter (ex. INR to BTC).
4. detail investigation of cryptocurrency’s blockchain.
5. tracking current value of any cryptocurrency.

> dependencies:

1. provided public key.
2. APIs from where we are fetching.
3. some libraries such that –
   re [regular expression]
   base58check
   hashlib

> show stopper:

1. we are bound on the 6 currencies that has been
   provided in the problem statement. Beyond that
   if any public key is provided our tool is not able
   to detect that.

> flowchart

![image](https://github.com/user-attachments/assets/148fb8ba-a655-4567-889d-c69fd08c5ee4)

- **[presentation](https://youtu.be/nRpRPiPnX-I?si=HpQjt-PlPXMDGeU1)**
