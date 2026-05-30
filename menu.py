import json
from enum import Enum

def menu_crud():
    print ("--------------------------------------------------")
    print ("\tCadastro de Ativos")
    print ("--------------------------------------------------")
    print ("\tEscolha qual operação deseja realizar: ")
    print ("--------------------------------------------------")
    print ("\t1 - Cadastro")
    print ("\t2 - Consulta")
    print ("\t3 - Atualização")
    print ("\t4 - Deletar")
    print ("\t5 - Cadastrar vulnerabilidades")
    print ("\t0 - Sair")
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

class Severidade(Enum):
    BAIXA    = 1
    MEDIA    = 2
    ALTA     = 3
    CRITICA  = 4

class StatusVuln(Enum):
    ABERTA          = 1
    EM_TRATAMENTO   = 2
    CORRIGIDA       = 3
    ACEITA_RISCO    = 4

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
            "tipo_ativo": TipoAtivo(tipo_ativo).name,
            "vulnerabilidades": []
        }
        adicionar_vulnerabilidade = input("Deseja cadastrar vulnerabilidades? (S/N): ")
        if adicionar_vulnerabilidade == "S":
            vulnerabilidade_inicial(ativos[id_ativo])
        
    salvar_ativos_json(ativos)


def carregar_dados():
    filename = "ativos.json"
    try:
        with open(filename, "r") as f_obj:
            dados = json.load(f_obj)
            return {int(chave): valor for chave, valor in dados.items()}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    
def vulnerabilidade_inicial(ativo):
    while True:
        descricao  = input("Descrição: ")
        categoria  = input("Categoria: ")
        severidade = validacao_entrada_inteiro("Severidade (1-Baixa 2-Média 3-Alta 4-Crítica): ", minimo=1, maximo=4)
        status     = validacao_entrada_inteiro("Status (1-Aberta 2-Em tratamento 3-Corrigida 4-Aceita risco): ", minimo=1, maximo=4)

        ativo["vulnerabilidades"].append({
            "descricao" : descricao,
            "categoria" : categoria,
            "severidade": Severidade(severidade).name,
            "status"    : StatusVuln(status).name
        })

        adicionar_vulnerabilidade = input("Adicionar outra vulnerabilidade? (S/N): ").strip().upper()
        if adicionar_vulnerabilidade != "S":
            break