import random

def cria_pecas():
    p = []
    i = 0
    while i <= 6:
        j = 0
        while j <= i:
            e = [j,i]
            p.append(e)
            j += 1
        i += 1
    random.shuffle(p)
    return p

pecas = cria_pecas()
print (pecas)