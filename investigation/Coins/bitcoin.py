import re
import base58check
import hashlib


def is_valid_bitcoin_address(address):
    pattern = "^(1|3)[a-km-zA-HJ-NP-Z1-9]{25,34}$"
    if not re.match(pattern, address):
        return False
    try:
        # print("Pattern matched as bitcoin")
        decoded = base58check.b58decode(address)
        if decoded[0] not in [0x00, 0x05]:
            return False
        checksum = decoded[-4:]
        hash160 = decoded[1:-4]
        computed_checksum = hashlib.sha256(
            hashlib.sha256(decoded[:-4]).digest()).digest()[:4]
        if checksum != computed_checksum:
            return False
    except:
        return False
    return True
