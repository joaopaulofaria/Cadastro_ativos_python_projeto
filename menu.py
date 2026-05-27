from enum import Enum

def menu_crud():
    print ("--------------------------------------------------")
    print ("\tCadastro de Ativos")
    print ("--------------------------------------------------")
    print ("\tEscolha qual operação deseja realizar: ")
    print ("--------------------------------------------------")
    print ("\t0 - Cadastro")
    print ("\t1 - Consulta")
    print ("\t2 - Atualização")
    print ("\t3 - Deletar")
    print ("\t4 - Cadastrar vulnerabilidades")
    print ("\t5 - Sair")
    print ("--------------------------------------------------")

class TipoAtivo(Enum):
    NOTEBOOK          = 1
    SERVIDOR          = 2
    ROTEADOR          = 3
    SOFTWARE          = 4
    APLICACAO_WEB     = 5
    BANCO_DE_DADOS    = 6
    IMPRESSORA        = 7
    ESTACAO_TRABALHO  = 8

def exibir_tipos():
    """Mostra os tipos disponíveis com seus códigos."""
    print("Tipos de ativo disponíveis:")
    for tipo in TipoAtivo:
        print(str(tipo.value) + " - " + str(tipo.name))

def validacao_entrada(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro, digite um numero valido")
