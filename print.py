def alinha(a, i, j, s, t):
    if i == 0 or j == 0:
        return "_"
    if (a[i][j] == a[i-1][j-1] + (s[i] != t[j])):
        alinha(a, i-1, j-1, s, t)
        print(s[i])
        print("_")

    if (a[i][j] == a[i-1][j] + 1):
        alinha(a, i-1, j, s, t)
        print(s[i])
        print(t[j])

    if (a[i][j] == a[i][j-1] + 1):
        alinha(a, i, j-1, s, t)
        print("_")
        print(t[j])

