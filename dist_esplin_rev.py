# devolve um vetor com a[j] = d(s,t[j+1...n]) para j de 0 até n

s = input()
t = input()

m = len(s)
n = len(t)

# criando vetor
b = []

for j in range(n+1): b.append(0)

for j in range(n-1, -1, -1): b[j] = b[j+1] + 1 # c(_, t[j+1])

for i in range(m-1, -1, -1):
    v = b[n]
    b[n] = v + 1 # c(s[i+1], _)

    for j in range(n-1, -1, -1):
        w = b[j]

        x = b[j+1] + 1 # c(_, t[j+1])
        y = v + (s[i] != t[j]) # c(s[i], t[j])
        z = w + 1 # c(s[i+1], _)

        b[j] = min(x, y, z)
        v = w

print(b)