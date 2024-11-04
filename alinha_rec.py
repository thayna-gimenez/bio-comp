def espaco(seq):
    espacos = ""
    
    for c in seq:
        espacos += "_"
    
    print(espacos)

def alinha_rec(seq_1, seq_2):
    m = len(seq_1)
    n = len(seq_2)
    
    if (m == 0):
        print(seq_2)
        espaco(seq_2)
        
    if (n == 0):
        print(seq_1)
        espaco(seq_1)

seq_1 = input()
seq_2 = input()

alinha_rec(seq_1, seq_2)