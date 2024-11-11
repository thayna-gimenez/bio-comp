# devolve uma matriz com a[i][j] = d(s[i+1..m], t[j+1..n])

s = input()
t = input()

m = len(s)
n = len(t)

# inicializando matriz
a = []

for i in range(m+1):
    a.append([])
    for j in range(n+1):
        a[i].append(0)

for j in range(n-1, -1, -1): a[m][j] = a[m][j+1] + 1 # c(_, t[j+1])

for i in range(m-1, -1, -1): 
    a[i][n] = a[i+1][n] + 1 # c(s[i+1], _)

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        x = 1 + a[i][j+1] # c(_, t[j+1])
        y = (s[i] != t[j]) + a[i+1][j+1]
        z = 1 + a[i+1][j] # c(s[i+1], _)

        a[i][j] = min(x, y, z)

for i in range(m+1):
    print(a[i])

