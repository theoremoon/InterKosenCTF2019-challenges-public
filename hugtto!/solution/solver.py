from PIL import Image
import os

import random

stat = os.stat("./steg_emiru.png")
img = Image.open("./steg_emiru.png")
w, h = img.size

for i in range(-60, 60):
    random.seed(stat.st_mtime + i)
    char = ""
    flag = ""
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            rnd = random.randint(0, 2)
            if rnd == 0:
                char += str(r & 1)
            elif rnd == 1:
                char += str(g & 1)
            elif rnd == 2:
                char += str(b & 1)
            if len(char) == 8:
                flag += chr(int(char[::-1], 2))
                char = ""
        break
    if "KosenCTF" in flag:
        print(flag)
        break
