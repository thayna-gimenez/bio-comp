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

    if (a[m][n] == a[m-1][n] + 2): # c(s[i], _)
        return alinha