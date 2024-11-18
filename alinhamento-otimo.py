def dist(s, t):
  # devolve uma matriz com a[i][j] = d(s[1...i),t[1..j])
  m = len(s)
  n = len(t)

  # criando matriz de alinhamento
  # no final, irá ser preenchida com as pontuações de alinhamentos ótimos de
  # prefixos de s com prefixos de t
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

  return a


# devolve um alinhamento ótimo mínimo entre s e t
# baseado no algoritmo para o problema da LCS
def alinha(a, i, j, s, t):
    if i == 0 or j == 0:
        return "_", "_"
        
    if (a[i][j] == a[i-1][j-1] + (s[i-1] != t[j-1])): # veio de uma substuição ou dos caracteres serem iguais (diagonal)
        s_alinhado, t_alinhado = alinha(a, i-1, j-1, s, t)
        s_alinhado += s[i-1] # como a matriz a "começa" no 1 mas a sequência não, precisa diminuir um do índice na hora de acessar a sequência
        t_alinhado += t[j-1]
        return s_alinhado, t_alinhado

    if (a[i][j] == a[i-1][j] + 1): # veio de cima (s alinhado a espaço)
        s_alinhado, t_alinhado = alinha(a, i-1, j, s, t)
        s_alinhado += s[i-1]
        t_alinhado += "_"
        return s_alinhado, t_alinhado

    if (a[i][j] == a[i][j-1] + 1): # veio da esquerda (t alinhado a espaço)
        s_alinhado, t_alinhado = alinha(a, i, j-1, s, t)
        s_alinhado += "_"
        t_alinhado += t[j-1]
        return s_alinhado, t_alinhado


s = input()
t = input()

a = dist(s, t)
s_alinhado, t_alinhado = alinha(a, len(s), len(t), s, t)
print(s_alinhado)
print(t_alinhado)