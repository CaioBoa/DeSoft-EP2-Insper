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
    jogo={}
    jogadores={}
    monte=[]
    

    for i in range(0,nj):
        jogadores[i]=[]

    ip=0
    while ip <= len(pecas)-1:
        for j in range(0,nj):
            while len(jogadores[j])<7:
                jogadores[j].append(pecas[ip])
                ip+=1

        if ip<=len(pecas)-1:
            monte.append(pecas[ip])
        ip+=1
    jogo['jogadores']=jogadores
    jogo['monte']=monte
    jogo['mesa']=[]

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
numero_jogadores = int(input("Quantos Jogadores?? (2-4)"))
while numero_jogadores<2 or numero_jogadores>4:
    print("\nNúmero de jogadores inválido!\n")
    numero_jogadores = int(input("Quantos Jogadores?? (2-4)"))
print("")
#distribui as peças
jogo = inicia_jogo(numero_jogadores,cria_pecas())
#cria uma ordem para os jogadores
ordem = ordem_jogadores(numero_jogadores)
#início da rodada
while verifica_ganhador(jogo["jogadores"]) == -1:
    #define turnos para os jogadores
    for jogador_atual in ordem:
        #caso seja um bot jogando
        if jogador_atual != 0:
            print("Turno do jogador {0}".format(jogador_atual))
            print("MESA: {0}\n".format(jogo["mesa"]))
            #para saber se existe jogadas possíveis ao bot ou ele terá que comprar do monte
            k = jogada_bot(jogo["jogadores"][jogador_atual],jogo["mesa"])
            #se tiver que comprar do monte
            if k == -1:
                #se o monte tiver peças suficientes
                if len(jogo["monte"]) > 0:
                    #compra do monte
                    jogo["jogadores"][jogador_atual].append(jogo["monte"][-1])
                    #explica jogada
                    print("Jogador {0} comprou uma peça do monte.\n".format(jogo["monte"][-1]))
                    #remove carta do monte
                    del jogo["monte"][-1]

            #se não tiver que comprar do monte
            else:
                #joga peça possível aleatória na mesa
                jogo["mesa"] = adiciona_na_mesa(jogo["jogadores"][jogador_atual][k],jogo["mesa"])
                #explica a jogada
                print("Jogador {0} colocou na mesa: {1}\n".format(jogador_atual,jogo["jogadores"][jogador_atual][k]))

                del jogo["jogadores"][jogador_atual][k]
                
            print("Nova MESA:{0}\n".format(jogo["mesa"]))
            print("-------------------------\n")
            
        #caso seja o usuário jogando
        if jogador_atual == 0:
            print("Seu turno!\n")
            print("Tamanho do Monte: {0}".format(len(jogo["monte"])))
            print("MESA: {0}\n".format(jogo["mesa"]))
            print("Suas peças: {0}".format(jogo["jogadores"][0]))
            #enumera as pecas
            x=""
            for i in range(len(jogo["jogadores"][0])):
                    x+="{0}       ".format(i+1)
                
                
            print("                {0}\n".format(x))
            #define lista de jogadas possiveis
            possiveis = posicoes_possiveis(jogo["mesa"],jogo["jogadores"][jogador_atual])
            #variavel para repetição do loop caso jogador não escolha uma peça possivel
            P = False
            #se existirem jogadas possiveis
            while len(possiveis) > 0 and P == False:
                #mostra jogadas possiveis
                #enumera as pecas possiveis
                z=[]
                x=""
                for i in possiveis:
                    z.append(jogo["jogadores"][jogador_atual][i])
                    x+="{0}       ".format(i+1)
                print("Você pode jogar as peças: {0}".format(z))
                
                print("                              {0}".format(x))
                #define uma peca para jogar
                peca_escolhida = int(input("Escolha uma peça: "))-1
                print('')
                #joga a peçaa na mesa caso seja possível
                if peca_escolhida in possiveis:
                    jogo["mesa"] = adiciona_na_mesa(jogo["jogadores"][jogador_atual][peca_escolhida],jogo["mesa"])
                    #explcia jogada
                    print("Você colocou na mesa: {0}".format(jogo["jogadores"][jogador_atual][peca_escolhida]))
                    
                    del jogo["jogadores"][jogador_atual][peca_escolhida]
                    print("Nova MESA: {0}\n".format(jogo["mesa"]))
                    print("-------------------------")
                    P = True
                #pede para jogar outra peça
                if peca_escolhida not in possiveis:
                    print("Escolha outra peça!\n")
            #se não existirem jogadas possíveis ao jogador
            if len(possiveis) == 0:
                
                print("Não existem jogadas possíveis nesse turno então vamos comprar do monte para você")
                print("Suas peças: {0}\n".format(jogo["jogadores"][0]))
                #se o monte tiver peças disponíveis
                if len(jogo["monte"]) > 0:
                    #compra do monte
                    jogo["jogadores"][jogador_atual].append(jogo["monte"][-1])
                    #deleta do monte
                    del jogo["monte"][-1]
                    #mostra pro jogador que comprou peca
                    k="zzz"
                    while k!="ok":
                        k=input("Digite 'ok' para continuar: ")
                

if verifica_ganhador(jogo["jogadores"]) == 0:
    print("Você venceu! Parabéns")
if verifica_ganhador(jogo["jogadores"]) > 0:
    print("O jogador {0} venceu! Não foi dessa vez".format(verifica_ganhador(jogo["jogadores"])))




        


            
            
