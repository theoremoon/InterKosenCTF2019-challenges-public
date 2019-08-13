import numpy as np

# KosenCTF{fl4ggy_p0lyn0m}
flag = b"KosenCTF"
flag = b"{fl4ggy_"
flag = b"p0lyn0m}"

# f(x) =  a0 + a1*x + a2*x^2 + ... + al-1 * x^{l-1}

Y = [[c] for c in flag]
Y = np.array(Y)

A = [
    [pow(j, i) for i in range(len(flag))]
    for j in range(len(flag))
]

A = np.array(A)
Ai = np.linalg.inv(A)

X = np.dot(Ai, Y)
print(X)

output = b""
for i in range(len(flag)):
    y = 0
    for j in range(len(flag)):
        y += X[j][0] * pow(i, j)
    output += bytes([int(round(y))])

assert output == flag
