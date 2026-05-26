#criação de menu para projeto
from menu import menu_crud

menu_crud()

operacao = input()
#escrever funcao que valida entrada de usuarios (se é int ou nao etc) e mover pro outro arquivo
try:
    operacao = int(operacao)
except ValueError:
    print("Digite um número válido")

#colocar essa operacao em um while com talvez uma variavel de ativacao
match operacao:
    case 0:
        print ("1 - Cadastro de ativos")
    case 1:
        print ("2 - Consulta")
    case 2:
        print ("3 - Atualizacao")
    case 3:
        print ("4 - Delete")
    case 4:
        print ("vulnerabilidade")
    case 5:
        print ("Sair")                            
    case _:
        print ("Opção invalida, tente novamente!")


