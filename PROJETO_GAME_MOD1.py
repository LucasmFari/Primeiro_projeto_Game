def main():
    print(f"{'THE WALKING DEAD':^80}")
    print('='*80)
    print(f"{'Você é um homem que acorda na cama de um hospital, sem mémoria, E agora?':^40}")
    print('\n ao se deparar com o quarto sujo de sangue e um silêncio no mesmo,')
    print('\n percebe que em sua volta só há sangue e desordem...')
    print('  e lhe faz um questionamento, cadê todos ?')
    print(f"{'Quando quiser começar, digite a palavra JOGAR:':^80}")
    print('')
    print(f"{'Senão, digite qualquer tecla...':^80}")
    print('')
    comeco = (input(f"{'JOGAR??:':^80}")).lower().strip().split()[0]
    if comeco == 'jogar':
        print('_' * 30)
        print('Veja qual personagem você pode chamar:')
        print('_' * 30)
    if selecao_personagem():
        endgame()

def endgame():
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        main()
    if resposta != 'j':
        endgame()

def selecao_personagem():
    user_in = int(input("Selecione seu personagem:\n 1 - will o estrategista\n 2 - jovem acelerado\n 3 - xerife abusado \nDigite 1, 2 ou 3:"))
    if user_in == 1:
        print('Você escolheu a will o estrategista.')
        game_01()
    elif user_in == 2:
        print('Você escolheu o jovem acelerado.')
        game_02()
    elif user_in == 3:
        print('Você escolheu o xerife abusado.')
        game_03()
    else:
        print("Digite uma opção válida !")
        selecao_personagem()



# Caso o jogador morra PERSOANAGEM1
def jogador_morreu():
    print("\033[31mum zumbi, morde sua perna, vai sangrar até morrer, lastimável!.\033[0;0m")
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        endgame()
    if resposta != 'j':
        endgame()
# Caso o jogador morra PERSOANAGEM1
def jogador_morre():
    print("\033[31mGAME OVER!\033[0;0m")
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        endgame()
    if resposta != 'j':
        endgame()

# Caso o jogador morra PERSOANAGEM1
def jogador_morreu_sniper():
    print("\033[31mO Sniper é certeiro, lhe acerta na cabeça, morte feia demais!!!!!\033[0;0m")
    resposta = (input("\033[31mGame Over!\033[0;0m\n\nDigite j para jogar denovo! :")).lower()
    while resposta == 'j':
        endgame()
    if resposta != 'j':
        endgame()
# Caso o jogador morra PERSOANAGEM1
def jogador_morreu_torre():
    print("\033[31msuas pernas quebram, e também vai sangrar até morrer, lastimável!.\033[0;0m")
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        endgame()
    if resposta != 'j':
        endgame()
#------------------------------------------------------------------------------------------------------
#comentario para o jogador voltar a jogar !!!!!!
#exemplo

#def jogador_morreu03():  
#   print("\033[31mé Xerife, não foi dessa vez!!\033[0;0m")
#  resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
# while resposta == 'j':
#    main()
#if resposta != 'j':
#    endgame()
#-------------------------------------------------------------------------------------------------------



# História personagem1

def game_01() -> object:
    print('=' * 200)
    resposta = input("você está andando muito atento pela cidade, "
                     "\ne escuta gritos esqusitos não muito longe de você,"
                     "\ne agora ?\n A - pega sua arma\n B - corre para outra direção \nDigite A ou B:").upper()
    print("=" * 200)
    if resposta == 'A':
        print("\033[31mvocê ao pegar sua arma não reparou que tinha um zumbi rastejando aos seus pés.\033[0;0m")
        jogador_morreu()
    elif resposta == 'B':
        print("ao correr para outra direção se livra.")
        jogador_cabana1()
    else:
        print("Por favor, digite uma opção válida !")
        game_01()

def jogador_cabana1():
    resposta = input(" E encontra um esconderijo, mas percebe que tem alguém te observando, um sniper rival.,"
                     "\no que você faz ?\n A - da meia volta\n B - atira para ganhar tempo e sair do galpão \nDigite A ou B:").upper()
    print("=" * 200)
    if resposta == 'A':
        print("De fato tinha um sniper mas quem te pega é.")
        jogador_morreu()
    elif resposta == 'B':
        print("você atira pra direção onde viu algo, isso faz com que consiga se livrar da mira do sniper")
        jogador_verifica_porta()
    else:
        print("Digite uma opção válida!")
        jogador_cabana1()
print("=" * 150)

def jogador_verifica_porta():
    resposta = input("após a troca de tiro, seu objetivo é sair desse lugar! \nA - corro mais rápido. \nB - vou pelo esgoto"
                     " do galpão \nC - Saio pelos fundos correndo. \nDigite A, B OU C:").upper()
    if resposta == 'A':
        print("é uma sig sauer 762, poder letal e alcançe absurdo")
        jogador_morreu_sniper()
    elif resposta == 'B':
        print("se livrou pela tubulação e seguiu adiante.")
        jogador_corre_zumbi()
    elif resposta == 'C':
        print("nos fundos é a saída de emergência !")
        jogador_corre_zumbi()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_verifica_porta()



def jogador_corre_zumbi():
    print("=" * 150)
    resposta = input("caminhando pro leste se depara com milhares de mortos vivos, resolve descarregar o pente ou não "
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print("sua munição acaba :(")
        jogador_morre()
    elif resposta == 'B':
        print("melhor coisa que fez, na sua volta tem um carro com as chaves para chegar até a torre de rádio")
        jogador_tem_uma_brilhante_ideia()
    else:
        print('digite um opção válida')
        jogador_corre_zumbi()


def jogador_tem_uma_brilhante_ideia():
    print("=" * 150)
    resposta = input('visualiza um torre de rádio, e tem a idéia de pedir ajuda através do sinal, você vai até lá ou segue adiante ?'
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print('você acaba dando mole e caí')
        jogador_morreu_torre()
    elif resposta == 'B':
        print("talvez não era tanto uma boa ideia, arriscado demais")
        jogador_foge()
    else:
        print('digite um opção válida')
        jogador_corre_zumbi()


def jogador_foge():
    print("=" * 150)
    resposta = input('\033[1;33m VOCÊ SE LIVROU E GANHOU O JOGO, TEM MEUS PARABÉNS, DESEJA JOGAR NOVAMENTE ?(sim/não)" \033[0;0m').lower()
    if resposta == 'sim':
        main()
    else:
        print('\033[31mATÉ À PRÓXIMA!!!!!!!!!')


#história personagem 2
def endgame():
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        main()
    if resposta != 'j':
        endgame()

def jogador_morreu02():
    print("\033[31mse deu mal meu amigo!!!!!\033[0;0m")
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        endgame()
    if resposta != 'j':
        endgame()


# História personagem2

def game_02() -> object:
    print('=' * 150)
    resposta = input("equipes rivais estão fazendo rondas em torno da cidade!!"
                     "\nhá barulhos de carros e alguns tiros pro alto,"
                     "\ne agora ?\n A - abaixo próximo de um carro\n B - corre para outra direção \nDigite A ou B:").upper()
    print("=" * 150)
    if resposta == 'A':
        print("\033[31mpensou bem garoto, boa escolha!\033[0;0m")
        jogador_ilha()
    elif resposta == 'B':
        print("tinha uma ronda nessa direção.")
        jogador_morreu02()
    else:
        print("Por favor, digite uma opção válida !")
        game_02()

def jogador_ilha():
    resposta = input(" após os rebeldes irem embora, você pensa em se insolar em uma ilha,,"
                     "\no que você faz ?\n A - continua com essa ideia?\n B - talvez seja melhor ir para alguma cidade com mais opções\nDigite A ou B:").upper()
    print("=" * 150)
    if resposta == 'A':
        print("chegou ao caís, mas era perigoso demais! ")
        jogador_morreu02()
    elif resposta == 'B':
        print("boa tática, talvez você encontre mais armas e remedios")
        jogador_cidade()
    else:
        print("Digite uma opção válida!")
        jogador_ilha()
print("=" * 150)

def jogador_cidade():
    resposta = input("você conseguiu chegar na cidade charleston! \nA - vai a casa de um amigo. \nB - encontra uma pessoa para te ajudar"
                     " nessa jornada \nC - lembra do carro dos seus avós. \nDigite A, B OU C:").upper()
    if resposta == 'A':
        print("ele estava trancado na casa, ao você abrir a porta, ele te pega!!")
        jogador_morreu02()
    elif resposta == 'B':
        print("essa pessoa te rouba e ainda te engana!")
        jogador_morreu02()
    elif resposta == 'C':
        print("boa escolha, seus avós estavam em outra cidade e morreram por lá mesmo, \na casa estava vazia, e ainda as chaves do carro estavam no mesmo lugar de sempre!")
        jogador_pega_carro()
    else:
        print("Por favor, digite uma opção válida !")
        game_02()



def jogador_pega_carro():
    print("=" * 150)
    resposta = input("dirijindo para o leste se depara com milhares de mortos vivos, resolve descarregar o pente ou não "
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print("sua munição acaba :(")
        jogador_morreu02()
    elif resposta == 'B':
        print("melhor coisa que fez, melhor ir para algum tipo de abrigo!!")
        jogador_encontra_um_abrigo()
    else:
        print('digite um opção válida')
        jogador_ilha()


def jogador_encontra_um_abrigo():
    print("=" * 150)
    resposta = input('visualiza um galpão, e tem a idéia de descansar um pouco, descansa um pouco ou segue adiante ?'
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print('tinha mortos vivos escondidos')
        jogador_morreu02()
    elif resposta == 'B':
        print("com essa sua escolha, você decide ir para o canadá")
        jogador_vai_para_outro_pais()
    else:
        print('digite um opção válida')
        jogador_encontra_um_abrigo()


def jogador_vai_para_outro_pais():
    print("=" * 150)
    resposta = input('\033[1;33m SERÁ UMA NOVA JORNADA NO CANADÁ, DESEJA JOGAR NOVAMENTE ?(sim/não)" \033[0;0m').lower()
    if resposta == 'sim':
        main()
    else:
        print('\033[31mATÉ À PRÓXIMA!!!!!!!!!')

#história personagem3

def endgame():
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    if resposta == 'j':
        main()
    if resposta != 'j':
        endgame()

def jogador_morreu03():
    print("\033[31mé Xerife, não foi dessa vez!!\033[0;0m")
    resposta = (input('\n\nDigite j para jogar denovo! :')).lower().strip().split()[0]
    while resposta == 'j':
        endgame()
    if resposta != 'j':
        endgame()

def game_03() -> object:
    print('=' * 150)
    resposta = input("ao andar pelo corredores do hospital, tem uma pequena lembrança que era integrante de algo militar!!"
                     "\nas luzes do hospital se apagam,"
                     "\ne agora ?\n A - tentar achar a saída principal\n B - ou pensar em ir para andares mais alto \nDigite A ou B:").upper()
    print("=" * 150)
    if resposta == 'A':
        print("\033[31ma saída principal estava obstruida!\033[0;0m")
        jogador_morreu03()
    elif resposta == 'B':
        print("tinha uma ronda nessa direção.")
        jogador_telhado()
    else:
        print("Por favor, digite uma opção válida !")
        game_03()

def jogador_telhado():
    resposta = input("no telhado havia um helicoptero,"
                     "\no que você faz ?\n A - pensa em tentar pilotar\n B - ou desiste da ideia e desce pela escada de emergência\nDigite A ou B:").upper()
    print("=" * 150)
    if resposta == 'A':
        print("foi uma boa ideia, conseguiu vê do alto o que está se passando!!")
        jogador_rua()
    elif resposta == 'B':
        print("você não se da conta que tem um ferro solto na escada e cai")
        jogador_morreu03()
    else:
        print("Digite uma opção válida!")
        jogador_telhado()
print("=" * 150)

def jogador_rua():
    resposta = input("você conseguiu pousar ! \nA - foi direto em casa. \nB - talvez agora seja melhor pegar um carro,"
                     " para procurar sua esposa!! \nC - um filme passa na sua cabeça, decide ir na delegacia. \nDigite A, B OU C:").upper()
    if resposta == 'A':
        print("foi na emoção e acabou morrendo, tinha um zumbi dentro da casa!!")
        jogador_morreu03()
    elif resposta == 'B':
        print("o carro estava ruim, ficou de costas e um zumbi te agarrou!")
        jogador_morreu03()
    elif resposta == 'C':
        print("boa escolha, lá pegará armas, \n assim conseguirá se defender, todo equipado se sairá melhor!")
        jogador_trocatirros()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_rua()



def jogador_trocatirros():
    print("=" * 150)
    resposta = input("ao sair da delegacia, se depara com uma multidão de zumbis, troca tiros ou sai pelos fundos?"
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print("estava bem preparado! senta a mamona meu filho!!! :)")
        jogador_ganhatempo()
    elif resposta == 'B':
        print("os fundos estavam trancados, perdeu tempo, os zumbis cercaram o local!!")
        jogador_morreu03()
    else:
        print('digite um opção válida')
        jogador_trocatirros()


def jogador_ganhatempo():
    print("=" * 150)
    resposta = input('Após trocar tiros, consegue chamar atenção de sobreviventes que estavam escondidos, se alia ou não?'
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print('era pessoas ruins!!!')
        jogador_morreu03()
    elif resposta == 'B':
        print(" os zumbis vão em direção ao outro grupo, se dá bem, consegue escapar!!")
        jogador_encontra_sua_esposa()
    else:
        print('digite um opção válida')
        jogador_ganhatempo()


def jogador_encontra_sua_esposa():
    print("=" * 150)
    resposta = input('\033[1;33m ENCONTROU SUA ESPOSA E AINDA GANHOU O JOGO, TEM MEUS PARABÉNS, DESEJA JOGAR NOVAMENTE ?(sim/não)" \033[0;0m').lower()
    if resposta == 'sim':
        main()
    else:
        print('\033[31mATÉ À PRÓXIMA!!!!!!!!!')
main()
