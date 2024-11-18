# primeira tentativa de alinhamento
# devolve um alinhamento de pontuação mínima de s e t

# imprime espaços de acordo com o tamanho da sequência dada
def espaco(seq):
    espacos = ""
    
    for c in seq:
        espacos += "_"
    
    print(espacos)

s = input()
t = input()

def alinha(a, s, t):
    m = len(s)
    n = len(t)

    if m == 0:
        print(t)
        espaco(t)
            
    if (n == 0):
        print(s)
        espaco(s)

    if (a[m][n] == a[m-1][n] + 1): # c(s[i], _)
        x = alinha(a, s[:m-1], t) 
        return x + s[m]

    if (a[m][n] == a[m-1][n-1] + (s[m] != t[n])):
        y = alinha(a, s[:m-1], t[:n-1])
        return y + s[m]
    