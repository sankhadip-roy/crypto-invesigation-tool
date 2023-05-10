import re

def is_valid_ethereum_address(address):
    pattern = "^0x[a-fA-F0-9]{40}$"
    if not re.match(pattern, address):
        return False
    try:
        print("Pattern matched as ethereum")
        decoded = bytes.fromhex(address[2:])
        if len(decoded) != 20:
            return False
    except:
        return False
    return True

#Base58 encoding is not used for Ethereum addresses because Ethereum uses a different algorithm to generate its addresses. Ethereum uses the Keccak-256 hash function to generate a 256-bit hash from a public key, and then takes the last 20 bytes (40 hexadecimal characters) of the hash to generate the address.
#The resulting address is in hexadecimal format and does not require any further encoding. Therefore, base58 encoding is not necessary for Ethereum addresses.