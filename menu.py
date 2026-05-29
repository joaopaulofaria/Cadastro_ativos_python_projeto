import json
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

def validacao_entrada_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            tipo_ativo = int(input(mensagem))
            if minimo is not None and tipo_ativo < minimo:
                print(f"Erro: digite um valor maior ou igual a {minimo}.")
            elif maximo is not None and tipo_ativo > maximo:
                print(f"Erro: digite um valor menor ou igual a {maximo}.")
            else:
                return tipo_ativo
        except ValueError:
            print("Erro, digite um numero valido.")

def criacao_id(id_ativo):
    if not id_ativo:
        return 1
    return max(id_ativo.keys()) + 1

def salvar_ativos_json(ativos):
    filename = "ativos.json"
    with open(filename, "w") as f_obj:
        json.dump(ativos, f_obj)

def entrada_cadastro_ativo(ativos):
    """Função para entrada de cadastro dos ativos"""

    limite = validacao_entrada_inteiro("Digite quantos ativos vai cadastrar: ")
    print("Digite os dados abaixo: ")

    for ativo in range(limite):
        id_ativo = criacao_id(ativos)

        hostname = input("Hostname: ") 
        responsavel = input("Responsavel: ")
        setor = input("setor: ")
        exibir_tipos()
        tipo_ativo = validacao_entrada_inteiro("Escolha o tipo do ativo (pelo id): ", minimo=1, maximo=8)

        ativos[id_ativo] = {
            "id": id_ativo,
            "hostname": hostname,
            "responsavel": responsavel,
            "setor": setor,
            "tipo_ativo": TipoAtivo(tipo_ativo).name
        }
    salvar_ativos_json(ativos)



