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

def inicia_jogo(nj,pecas):
    jogo = {}
    jogadores = {}
    i = 0
    while i < nj:
        dist = []
        j = 0
        while len(dist) < 7:
            dist.append(pecas[j])
            del pecas[j]
            j += 1
        jogadores[i] = dist
        i += 1
    jogo["jogadores"] = jogadores
    jogo["monte"] = pecas
    jogo["mesa"] = []
    return jogo

def verifica_ganhador(dic):
    jogadores = dic.keys()
    nj = len(jogadores)
    i = 0
    while i < nj:
        if len(dic[i]) == 0:
            return i
        i += 1
    return -1

def soma_pecas(l):
    i = 0
    somatotal = 0
    while i < len(l):
        s = l[i][0] + l[i][1]
        somatotal += s
        i += 1
    return somatotal

def posicoes_possiveis(mesa,pecas):
    i = 0
    sol = []
    if len(mesa) == 0:
        i = 0
        while i < len(pecas):
            sol.append(i)
            i += 1
    else:
        while i < len(pecas):
            if mesa[0][0] in pecas[i]:
                sol.append(i)
            elif mesa[-1][1] in pecas[i]:
                sol.append(i)
            i += 1
    return sol

def adiciona_na_mesa(peca,mesa):
    if len(mesa) == 0:
        mesa.append(peca)
    else:
        if peca[1] == mesa[0][0]:
            mesa.insert(0,peca)
        elif peca[0] == mesa[0][0]:
            k = peca[1]
            del peca[1]
            peca.insert(0,k)
            mesa.insert(0,peca)
        elif peca[0] == mesa[-1][1]:
            mesa.append(peca)
        elif peca[1] == mesa[-1][1]:
            k = peca[1]
            del peca[1]
            peca.insert(0,k)
            mesa.append(peca)
    return mesa

