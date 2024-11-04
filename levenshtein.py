# adiciona espaço no final da menor sequência
def add_espaco(seq, diferenca):
    for i in range(diferenca):
            seq += "_"

    return seq

s = input()
t = input()

m = len(s)
n = len(t)

if (m <= n):
    s = add_espaco(s, n-m)
        
else:
    t = add_espaco(t, m-n)

linha_zero = [0] * len(s)
c = [linha_zero] * len(t)

for i in range(len(s)):
     for j in range(len(t)):

        if s[i] == t[j]:
            c[i][j] = 1

print(c)