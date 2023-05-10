import re
import base58check
import hashlib

def is_valid_dogecoin_address(address):
    pattern = "^(D|9|A|Q|R)[1-9A-HJ-NP-Za-km-z]{32,40}$"
    if not re.match(pattern, address):
        return False
    try:
        print("Pattern matched as dogecoin")
        decoded = base58check.b58decode(address)
        if decoded[0] not in [0x1e, 0x30, 0x00, 0x05, 0x06]:
            return False
        checksum = decoded[-4:]
        hash160 = decoded[1:-4]
        computed_checksum = hashlib.sha256(hashlib.sha256(decoded[:-4]).digest()).digest()[:4]
        if checksum != computed_checksum:
            return False
    except:
        return False
    return True