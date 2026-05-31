#criação de menu para projeto
from menu import menu_crud
from menu import validacao_entrada_inteiro
from menu import entrada_cadastro_ativo
from menu import carregar_dados
from busca import consulta_ativo
from atualizar import atualizar_ativo
from delete import delete_ativo
from vulnerabilidade import cadastro_vulnerabilidade
#ver uma forma de tirar esse tanto de from (outras formas de chamar o metodo)

menu_crud()
ativos = carregar_dados()

#escrever funcao que valida entrada de usuarios (se é int ou nao etc) e mover pro outro arquivo
operacao = validacao_entrada_inteiro("Digite um numero: ")

#colocar essa operacao em um while com talvez uma variavel de ativacao

match operacao:
    case 1:
        entrada_cadastro_ativo(ativos)
    case 2:
        consulta_ativo(ativos)
    case 3:
        atualizar_ativo(ativos)
    case 4:
        delete_ativo(ativos)
    case 5:
        cadastro_vulnerabilidade(ativos)
    case 0:
        print ("Sair")                           
    case _:
        print ("Opção invalida, tente novamente!")


