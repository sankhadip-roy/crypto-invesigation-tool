import re
import base58check
import hashlib

def is_valid_monero_address(address):
    pattern = "^(4|8)[0-9A-HJ-NP-Za-km-z]{94}$"
    if not re.match(pattern, address):
        return False
    try:
        print("Pattern matched as monero")
        decoded = base58check.b58decode(address)
        if decoded[0] != 0x12:
            return False
        checksum = decoded[-4:]
        hash256 = hashlib.sha256(hashlib.sha256(decoded[:-4]).digest()).digest()
        computed_checksum = hash256[:4]
        if checksum != computed_checksum:
            return False
    except:
        return False
    return True