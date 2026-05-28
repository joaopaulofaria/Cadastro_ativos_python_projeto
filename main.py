#criação de menu para projeto
from menu import menu_crud
from menu import exibir_tipos
from menu import validacao_entrada_inteiro
from menu import entrada_cadastro_ativo

menu_crud()
ativos = {} 

#escrever funcao que valida entrada de usuarios (se é int ou nao etc) e mover pro outro arquivo
operacao = validacao_entrada_inteiro("Digite um numero: ")

#colocar essa operacao em um while com talvez uma variavel de ativacao

match operacao:
    case 0:
        entrada_cadastro_ativo(ativos)
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


