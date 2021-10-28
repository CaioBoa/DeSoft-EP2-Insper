import random

#cria uma lista com 28 pecas
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

#distribui a lista de pecas entre o numero de jogadores (7 para cada) e coloca o resto no monte além de criar a lista mesa
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

#verifica as pecas de todos os jogadores e caso algum não tenha pecas em mão retorna seu número (caso contrário retorna -1)
def verifica_ganhador(dic):
    jogadores = dic.keys()
    nj = len(jogadores)
    i = 0
    while i < nj:
        if len(dic[i]) == 0:
            return i
        i += 1
    return -1

#soma o valor das peças de um jogador
def soma_pecas(l):
    i = 0
    somatotal = 0
    while i < len(l):
        s = l[i][0] + l[i][1]
        somatotal += s
        i += 1
    return somatotal

#retorna uma lista das peças que podem ser utilizadas dependendo da mesa e das peças do jogador
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

#adiciona a peça na mesa, girando-a caso necessário
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

#cria uma lista baseado no número dos jogadores para estimar uma ordem aleatória
def ordem_jogadores(nj):
    i = 0
    l_ordem = []
    while len(l_ordem) < nj:
        l_ordem.append(i)
        i += 1
    random.shuffle(l_ordem)
    return l_ordem

#recebe a mão do jogador (bot) e a situação da mesa e retorna uma jogada possível para o mesmo realizar, caso não haja jogada retoran False
def jogada_bot(mao,mesa):
    jogadas = posicoes_possiveis(mesa,mao)
    if len(jogadas) == 0:
        return False
    r = random.randint(0,len(mao)-1)
    while r not in jogadas:
        r = random.randint(0,len(mao)-1)
    return r

#pergunta numero de jogadores
numero_jogadores = input("Quantos Jogadores?? (2-4)")
#distribui as peças
jogo = inicia_jogo(numero_jogadores,cria_pecas())
#cria uma ordem para os jogadores
ordem = ordem_jogadores(numero_jogadores)
#início da rodada
while verifica_ganhador(jogo["jogadores"]) == -1:
    print("MESA:{0}".format(jogo["mesa"]))
    #define turnos para os jogadores
    for jogador_atual in ordem:
        #caso seja um bot jogando
        if jogador_atual != 0:
            #para saber se existe jogadas possíveis ao bot ou ele terá que comprar do monte
            k = jogada_bot(jogo["jogadores"][jogador_atual],jogo["mesa"])
            #se tiver que comprar do monte
            if k == -1:
                #se o monte tiver peças suficientes
                if len(jogo["monte"]) > 0:
                    #compra do monte
                    jogo["jogadores"][jogador_atual].append(jogo["monte"][-1])
            #se não tiver que comprar do monte
            else:
                #joga peça possível aleatória na mesa
                jogo["mesa"] = adiciona_na_mesa(jogo["jogadores"][jogador_atual][k],jogo["mesa"])
        #caso seja o usuário jogando
        if jogador_atual == 0:
            #define lista de jogadas possiveis
            possiveis = posicoes_possiveis(jogo["mesa"],jogo["jogadores"][jogador_atual])
            #variavel para repetição do loop caso jogador não escolha uma peça possivel
            P = False
            #se existirem jogadas possiveis
            while len(possiveis) > 0 and P == False:
                #define uma peca para jogar
                peca_escolhida = int(input("Escolha uma peça"))
                #joga a peçaa na mesa caso seja possível
                if peca_escolhida in possiveis:
                    jogo["mesa"] = jogo["mesa"] = adiciona_na_mesa(jogo["jogadores"][jogador_atual][peca_escolhida],jogo["mesa"])
                    P = True
                #pede para jogar outra peça
                if peca_escolhida not in possiveis:
                    print("Escolha outra peça")
            #se não existirem jogadas possíveis ao jogador
            else:
                #se o monte tiver peças disponíveis
                if len(jogo["monte"]) > 0:
                    #compra do monte
                    jogo["jogadores"][jogador_atual].append(jogo["monte"][-1])



        


            
            
