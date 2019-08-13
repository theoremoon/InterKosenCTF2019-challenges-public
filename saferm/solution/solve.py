with open("document.zip", "rb") as f:
    buf = f.read()

key = b"\x2e\x57\xad\x2e\xff\xc8\xca\x49"
output = b''
for i in range(0, len(buf) - 8, 8):
    for j in range(8):
        output += bytes([buf[i + j] ^ key[j]])

with open("output.zip", "wb") as f:
    f.write(output + buf[-4:])
