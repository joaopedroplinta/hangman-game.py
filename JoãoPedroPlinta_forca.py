import random
import os
import unicodedata
from colorama import Fore, Style

art_forca = [Fore.MAGENTA + """
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """ + Style.RESET_ALL,
Fore.MAGENTA + """
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """ + Style.RESET_ALL,
Fore.MAGENTA + """
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """ + Style.RESET_ALL,
Fore.MAGENTA + """
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """ + Style.RESET_ALL,
Fore.MAGENTA + """
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """ + Style.RESET_ALL,
Fore.MAGENTA + """
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """ + Style.RESET_ALL,
Fore.MAGENTA + """
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """ + Style.RESET_ALL]

jogadas = vitorias = 0
usuario = ' '

#    Função Principal do programa
def main():
    global art_forca, jogadas, vitorias, usuario  # Chamando variaveis para a função
    print(Fore.LIGHTWHITE_EX + '🎮 BEM VINDO AO JOGO DA FORCA 🎮' + Style.RESET_ALL)
    usuario = input(Fore.LIGHTGREEN_EX + 'Para começar digite seu nome de usuario: ' + Style.RESET_ALL)  # Lendo nome do usuario
    dificuldade = input(Fore.LIGHTGREEN_EX + 'Digite a dificuldade (Normal/Tormento/Inferno/Nightmare): ' + Style.RESET_ALL) # Lendo a dificuldade do usuario 
    max_erros = define_max_erros(dificuldade)
    jogadas += 1  # Atribuindo jogada
    letras_erradas = ''  # variavel para letras erradas
    letras_acertadas = ''  # variavel para letras acertadas
    secreta = gera_secreta().upper()  # Chamando funcao para gerar aleatoriamente uma palavra
    secreta_sem_acento = remove_acentos(secreta) # Chamando a função para facilitar a verificação de acertos
    jogando = True  # Atribuindo True para controle

    while jogando:  # enquanto estiver jogando,
        impressao_jogo(letras_erradas, letras_acertadas, secreta, secreta_sem_acento)  # Chamando funcao para impressão do jogo
        palpite = atribuicao_palpite(letras_erradas + letras_acertadas)  # Atribuicao de palpite conforme função

        if palpite in secreta:  # Se palpite estiver na palavra secreta
            letras_acertadas += palpite  # Incrementar o acerto nas letras acertadas

            if checa_vitoria(secreta, letras_acertadas):  # Verificação se o jogo foi vencido
                print(Fore.WHITE + f'Parabens❗ 🎉 A palavra secreta era {secreta} | ❗ Voce ganhou 👏❗' + Style.RESET_ALL)  # Impressao da palavra + mensagem de vitoria
                vitorias += 1  # Incrementando vitoria em 1
                jogando = False  # Nao esta mais jogando
        else:
                letras_erradas += palpite  # Incrementar o erro nas letras erradas

        if len(letras_erradas) == max_erros:
            os.system('clear')
            letras_erradas += palpite
            print(art_forca[len(letras_erradas) - 1])  # imprime a imagem da forca correspondente
            print(Fore.WHITE + f'Voce perdeu❗😂 A palavra secreta era {secreta}.' + Style.RESET_ALL)
            jogando = False

        if not jogando:  # Se nao estiver jogando,
            if repetir_jogo():  # Pergunta se quer jogar novamente, se sim:
                if trocar_dificuldade(): # Pergunta se quer trocar 
                    dificuldade = input(Fore.LIGHTGREEN_EX + 'Digite a dificuldade (Normal/Tormento/Inferno/Nightmare): ' + Style.RESET_ALL) # Lendo a dificuldade do usuario 
                jogadas += 1  # Atribuicao de jogadas para controle futuro
                letras_erradas = ''  # Reiniciando variavel de erros
                letras_acertadas = ''  # Reiniciando variavel de acertos
                jogando = True  # Usuario volta a jogar
                secreta = gera_secreta().upper()  # Gera nova palavra
            else:  # Caso nao queira mais jogar,
                print(f'{usuario}, voce jogou {jogadas} vezes e ganhou {vitorias} delas.')  # Impressao de resultados finais

def gera_secreta():
    with open('forca.txt', 'r', encoding="utf8") as arquivo: # Abrindo arquivo com as palavras
        palavras = arquivo.readlines() # Lendo todas as palavras do arquivo
        secreta = random.choice(palavras).strip() # Escolhendo aleatoriamente uma palavra e removendo espacos em branco
        return secreta

def remove_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto) # Aplica a normalização NFKD (compatibilidade de decomposição) no texto para separar os caracteres acentuados em suas partes
    sem_acentos = u"".join([c for c in nfkd if not unicodedata.combining(c)]) # Cria uma nova string sem acentos, juntando os caracteres do texto normalizado que não são caracteres combinados (acentos)
    return sem_acentos # Retorna a string sem acentos

def impressao_espaco(palavra):  # Funcao para impressao com espacos
    for letra in palavra: # Para cada caractere (letra) na string "palavra"
        print(letra, end = ' ') # Imprime a letra seguida de um espaço (sem quebrar a linha)

    print()  # Deixa uma linha vazia

def define_max_erros(dificuldade): # Define a função define_max_erros com um parâmetro dificuldade.
    dificuldades = {'NORMAL': 6, 'TORMENTO': 4, 'INFERNO': 3, 'NIGHTMARE': 2} # Cria um dicionário dificuldades com chaves de diferentes níveis de dificuldade do jogo e seus respectivos valores que representam o número máximo de erros permitidos
    return dificuldades[dificuldade.upper()] # Retorna o valor associado à chave dificuldade convertida para maiúscula no dicionário dificuldades, ou 6 se a chave não existir no dicionário.

def atribuicao_palpite(letras): # Define a função atribuicao_palpite com um parâmetro letras.
    while True: # Inicia um loop infinito.
        palpite = input(Fore.LIGHTCYAN_EX + 'Digite uma letra: ' + Style.RESET_ALL).upper() # Recebe uma entrada do usuário para palpite, converte a entrada para maiúscula e a atribui à variável palpite.
        if len(palpite) == 1 and palpite.isalpha(): # Verifica se a entrada do usuário tem comprimento 1 e é uma letra.
            if palpite in letras: # Verifica se o palpite já foi escolhido anteriormente.
                print('Voce ja escolheu essa letra. Tente novamente.') # Imprime uma mensagem informando ao usuário que a letra já foi escolhida anteriormente.
            else: # Se o palpite é uma letra e não foi escolhido anteriormente, a execução cai aqui.
                return palpite # Retorna o palpite escolhido pelo usuário. Se o palpite não atender aos critérios, o loop continuará até que um palpite válido seja fornecido.
        else:
            print('Entrada invalida. Tente novamente.')

def impressao_jogo(letras_erradas, letras_acertadas, secreta, secreta_sem_acento):  # Função para impressao do jogo

    global art_forca  # define uma variavel global
    os.system('clear')  # Limpa a tela do terminal 
    print(art_forca[len(letras_erradas)] + '\n')  # Impressao da forca de acordo com erros do usuario
    print(Fore.RED + 'Letras erradas:' + Style.RESET_ALL, end=' ') # Imprime a mensagem "Letras erradas:" com formatação de cor

    # Imprime as letras erradas digitadas pelo usuário
    for letra in letras_erradas:
        print(letra, end=' ')
    print() # Imprime uma linha em branco
    vazio = '_' * len(secreta)  # Cria uma string com underscores (_) para representar as letras não reveladas

    # Substitui os underscores pelas letras acertadas na palavra
    for i in range(len(secreta_sem_acento)):
        if secreta_sem_acento[i] in letras_acertadas:
            vazio = vazio[:i] + secreta[i] + vazio[i + 1:]

    # Imprime a palavra com as letras acertadas e os underscores
    for letra in vazio:
        print(letra, end=' ')
    print() # Imprime uma linha em branco

def atribuicao_palpite(palpite_usuario):
    acentos = {
        'A': 'ÁÀÂÃÄ',
        'E': 'ÉÈÊË',
        'I': 'ÍÌÎÏ',
        'O': 'ÓÒÔÕÖ',
        'U': 'ÚÙÛÜ',
        'C': 'Ç'
    } # Cria um dicionário com as letras base (sem acento) e suas correspondentes acentuadas

    while True:  # Enquanto usuario estiver dando palpites
        palpite = input(Fore.RED + 'Entre com alguma letra. \n' + Style.RESET_ALL).upper()  # Lendo entrada do usuario e convertendo em maisucula
        if len(palpite) != 1:  # Verifica se usuario entrou com apenas uma letra
            print(Fore.LIGHTRED_EX + 'Coloque uma unica letra' + Style.RESET_ALL)
        elif palpite in palpite_usuario:  # Verifica se usuario entrou com palpite repetido
            print(Fore.LIGHTRED_EX + 'Voce ja digitou essa letra, digite de novo!' + Style.RESET_ALL)
        elif not 'A' <= palpite <= 'Z':  # Verifica se esta dentro do alfbeto
            print(Fore.LIGHTRED_EX + 'Digite somente uma letra!' + Style.RESET_ALL)
        else:
            for letra_base, acentuadas in acentos.items(): # Adiciona automaticamente os acentos possíveis ao palpite
                # Se o palpite estiver na lista de acentuadas, substitui pelo equivalente sem acento
                if palpite in acentuadas:
                    palpite = letra_base
                    break
            return palpite # Retorna o palpite sem acento (ou o próprio palpite, caso não haja acento)
        
def repetir_jogo():
    return input(Fore.LIGHTWHITE_EX + "Voce quer jogar novamente? (SIM ou NAO)\n" + Style.RESET_ALL).upper().startswith('S')  # Retorna resposta do usuario

def trocar_dificuldade():
    return input(Fore.LIGHTWHITE_EX + "Você quer trocar a dificuldade? (SIM OU NÃO)\n" + Style.RESET_ALL).upper().startswith('S')  # Retorna resposta do usuario

def checa_vitoria(secreta, letras_acertadas):
    venceu = True
    for letra in secreta:  # Checa cada letra da palavra secreta
        if letra not in letras_acertadas:  # E se nao estiver na palavra secreta,
            venceu = False  #  Venceu torna-se falso
            break  # Quebra da estrutura de repeticao

    return venceu  # retorna True se a letra estiver na secreta e caso contrario, False

main()  # Chama função principal do programa