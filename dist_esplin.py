# devolve um vetor com a[j] = d(s,t[1..j]) para j de 0 até n

s = input()
t = input()

m = len(s)
n = len(t)

# criando vetor
a = []

for j in range(n+1): a.append(0)

for j in range(1, n+1): a[j] = a[j-1] + 1 # c(_, t[j])

for i in range(1, m+1):
    v = a[0] # correspondente à coluna j-1
    a[0] = v + 1 # c(s[i], _)

    for j in range(1, n+1):
        w = a[j] # correspondente à coluna j

        x = a[j-1] + 1 # c(_, t[j])
        y = v + (s[i-1] != t[j-1]) # c(s[i], t[j])
        z = w + 1 # c(s[i], _)

        a[j] = min(x, y, z)
        v = w

print(a) # contém as distâncias entre a sequência s inteira e todos os prefixos de t (inclusive o vazio)

