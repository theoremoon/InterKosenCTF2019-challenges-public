from ptrlib.crypto.padcbc import padding_oracle_encrypt
from binascii import hexlify, unhexlify
import requests
import os
import json

def pad(s, bs):
    l = bs - len(s) % bs
    return s + bytes(l for _ in range(l))

URL = "http://" + os.getenv("CHALLENGE_HOST", "localhost") + ":8000/"

# oracle function
def decrypt(cipher):
    r = requests.get(URL + "result", cookies={"result": hexlify(cipher).decode()})
    return (
        "unicode decode error" in r.text
        or "padding error" not in r.text
        or "json decode error" in r.text
    )

# encrypt a payload by padding oracle
payload = pad(json.dumps({"is_hit": "1", "number": "1"}).encode(), 16)
iv, cipher = padding_oracle_encrypt(decrypt, payload, bs=16, unknown=b"?")

# login and get the flag
import re

r = requests.get(URL + "result", cookies={"result": hexlify(iv + cipher).decode()})
print(re.findall("KosenCTF{.+}", r.text)[0])
