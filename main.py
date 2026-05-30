#criação de menu para projeto
from menu import menu_crud
from menu import validacao_entrada_inteiro
from menu import entrada_cadastro_ativo
from menu import carregar_dados

menu_crud()
ativos = carregar_dados()

#escrever funcao que valida entrada de usuarios (se é int ou nao etc) e mover pro outro arquivo
operacao = validacao_entrada_inteiro("Digite um numero: ")

#colocar essa operacao em um while com talvez uma variavel de ativacao

match operacao:
    case 1:
        entrada_cadastro_ativo(ativos)
    case 2:
        print ("2 - Consulta")
    case 3:
        print ("3 - Atualizacao")
    case 4:
        print ("4 - Delete")
    case 5:
        print ("vulnerabilidade")
    case 0:
        print ("Sair")                           
    case _:
        print ("Opção invalida, tente novamente!")


