# devolve uma matriz com a[i][j] = d(s[1...i),t[1..j])

s = input()
t = input()

m = len(s)
n = len(t)

# criando matriz de alinhamento
a = []

for i in range(m+1):
    a.append([])
    for j in range(n+1):
        a[i].append(0)

for j in range(1, n+1): a[0][j] = a[0][j-1] + 1 # c(_, t[j])

for i in range(1, m+1): a[i][0] = a[i-1][0] + 1 # c(s[i], _)

print(a[0])

for i in range(1, m+1):
    for j in range(1, n+1):
        x = a[i-1][j] + 1 # c(s[i], _)
        y = a[i][j-1] + 1 # c(_, t[j])
        z = a[i-1][j-1] + (s[i-1] != t[j-1]) # se for diferente é 1 (levenshtein)

        a[i][j] = min(x, y, z)

    print(a[i])


""" for i in range(1, m+1):
    for j in range(1, n+1):
        a[i][j] = a[i-1][j] + 1 # c(s[i], _)

        if (a[i][j] > a[i-1][j-1] + (s[i-1]) != t[j-1]): # c(s[i], t[j])
            a[i][j] = a[i-1][j-1] + 1 

        if (a[i][j] > a[i][j-1] + 1): # c(_, t[j])
            a[i][j] = a[i][j-1] + 1 """
