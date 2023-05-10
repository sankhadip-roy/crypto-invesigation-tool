import re
import base58check
import hashlib

def is_valid_tether_address(address):
    pattern = "^1[1-9A-HJ-NP-Za-km-z]{33}$"
    if not re.match(pattern, address):
        return False
    try:
        print("Pattern matched as tether")
        decoded = base58check.b58decode(address)
        if decoded[0] != 0x00:
            return False
        checksum = decoded[-4:]
        hash160 = decoded[1:-4]
        computed_checksum = hashlib.sha256(hashlib.sha256(decoded[:-4]).digest()).digest()[:4]
        if checksum != computed_checksum:
            return False
    except:
        return False
    return True