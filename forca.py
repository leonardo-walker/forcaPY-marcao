from funcoes import limpar_tela, menu_apresentacao, ganhou, perdeu,printar_historico
import time
from datetime import datetime

limpar_tela()
menu_apresentacao()
time.sleep(3)
limpar_tela()

nome_desafiante = input("Quem vai desafiar? ")
nome_desafiado = input("Quem vai ser desafiado? ")

limpar_tela()

print("As seguintes informações devem ser completadas pelo DESAFIANTE: ")
palavra_chave = input("\nDigite a PALAVRA CHAVE: ").lower().strip()
dica1 = input("\nDigite a DICA 1: ")
dica2 = input("\nDigite a DICA 2: ")
dica3 = input("\nDigite a DICA 3: ")

letras_digitadas = []
erros = 0
letras_certas = []
limpar_tela()

print("Bem VindoX", nome_desafiado)
print("-----------------------------------")

while True:
    key = ''
    for letra in palavra_chave:
        key += letra if letra in letras_certas else "_ "
    print("Acerte a palavra:",key)       
    if key == palavra_chave:
        ganhou()
        break
    print ('''\nDigite "0" para receber dicas''')
    tentativa = input("\nDigite uma letra:").lower().strip()
    limpar_tela()
    if tentativa == '0':
        escolher_dica = input ('''
(1) Para a dica 1.
(2) Para a dica 2.
(3) Para a dica 3.

Selecione uma opção: ''' )
        if escolher_dica == "1":
            print('\nDica 1: ',dica1)
            time.sleep(3)
            limpar_tela()
        elif escolher_dica == '2':
            print('\nDica 2: ',dica2)
            time.sleep(3)
            limpar_tela()
        elif escolher_dica == '3':
            print('\nDica 3: ',dica3)
            time.sleep(3)
            limpar_tela()
        else:
            print("Opção inválida!\n")
            time.sleep(3)
            limpar_tela()
    try: 
        letras_digitadas
    except:
        print("Caracter inválido!\n")

    if tentativa in letras_digitadas:
        print("Você já tentou essa letra!\n")
        erros = erros
        
    else:
         letras_digitadas += tentativa
    
    if tentativa in palavra_chave or tentativa == '0':
        letras_certas += tentativa
    else:
        erros += 1
        print ("Essa letra não está na palavra!\n")

    if erros >= 6:
        print('''
I==:==
I  :
I  O         ENFORCADO!        
I \|/          
I / \ 
===========
    ''')
        time.sleep(2)
        break

    print("I==:==\nI  :   ") 
    print("I  O   " if erros >= 1 else "I")
    linha2 = ""
    if erros == 2:
            linha2 = "  |   "
    elif erros == 3:
            linha2 = " \|   "
    elif erros >= 4:
            linha2 = " \|/ "
    print("I%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 = " /     "
    elif erros >= 6:
        linha3 = " / \ "
    print("I%s" % linha3)
    print("I\n===========")
   
limpar_tela()
if key == palavra_chave:
    ganhou()
    time.sleep(3)
    limpar_tela()
else:
    perdeu()
    time.sleep(3)
    limpar_tela()

print("A palavra chave era:",palavra_chave)
registro = open("registro.txt","w")

if key == palavra_chave:
    registro.write("O(a) vencedor(a) foi %s" % nome_desafiado)
else:
    registro.write("O(a) vencedor(a) foi %s" % nome_desafiante)
    
registro = open("registro.txt","r")
conteudo = registro.read()
print(conteudo)

input("\nPressione ENTER para continuar...")
limpar_tela()

historico=[]
data_atual = datetime.today().strftime('%d/%m/%Y - %H:%M')

arquivo = open("historico.txt","a")
historico.append (data_atual+" -> "+ nome_desafiante+ " VS " + nome_desafiado+" -> "+ conteudo+" -> "+"Palavra: "+palavra_chave+"\n" )
arquivo.write(''.join(historico))
arquivo.close()


print ('''(1) Para ver o histórico.
(2) Para deletar o histórico.
(0) Para sair.''')

ver_historico = input("\nDigite uma opção:")
if ver_historico == "1":
    printar_historico()
    quit()
elif ver_historico == "2":
    del historico
    arquivo = open("historico.txt","w")
    arquivo.close()
    limpar_tela()
    print("Histórico deletado com sucesso!")
    time.sleep (2)
    quit()
elif ver_historico == "0":
        limpar_tela()
        quit()
