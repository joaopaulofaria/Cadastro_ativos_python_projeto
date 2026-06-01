from menu import menu_crud, validacao_entrada_inteiro, entrada_cadastro_ativo, carregar_dados
from busca import consulta_ativo
from atualizar import atualizar_ativo
from delete import delete_ativo
from vulnerabilidade import cadastro_vulnerabilidade

ativos = carregar_dados()

while True:
    menu_crud()
    operacao = validacao_entrada_inteiro("Digite um numero: ")

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
            break                          
        case _:
            print ("Opção invalida, tente novamente!")


