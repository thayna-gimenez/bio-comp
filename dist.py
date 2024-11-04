# devolve uma matriz com a[i][j] = d(s[1...i),t[1..j])

s = input()
t = input()

m = len(s)
n = len(t)

# criando matriz de alinhamento
linha_zero = [0] * len(s)
a = [linha_zero] * len(t)

for j in range(1, n):
    a[0][j] = a[0][j-1] + 1 # c(_, t[j])

for i in range(1, m):
    a[i][0] = a[i-1][0] + 2 # c(s[i], _)

    for j in range(1, n):
        a[i][j] = a[i-1][j] + 2 # c(s[i], _)

        if (a[i][j] > a[i-1][j-1] + 3): # c(s[i], t[j])
            a[i][j] = a[i-1][j-1] + 3

        if (a[i][j] > a[i][j-1] + 1): # c(_, t[j])
            a[i][j] = a[i][j-1] + 1


print(a)
