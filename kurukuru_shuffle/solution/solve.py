encrypted = open("encrypted").read().strip()
L = len(encrypted)

for a in range(L):
    for b in range(L):
        for k in range(1, L):
            flag = list(encrypted)
            i = 0
            for _ in range(L):
                s = (i + a) % L
                t = (i + b) % L
                flag[s], flag[t] = flag[t], flag[s]
                i = (i - k) % L
            flag = "".join(flag)
            if flag.startswith("KosenCTF{"):
                print(flag)
