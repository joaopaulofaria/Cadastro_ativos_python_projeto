from menu import vulnerabilidade_inicial
from menu import validacao_entrada_inteiro
from menu import salvar_ativos_json

def cadastro_vulnerabilidade(ativos):
    """Cadastrar vulnerabilidade apos o ativo ja esta na base de dados"""
    print ("Cadastro de vulnerabilidades")
    id_consulta = validacao_entrada_inteiro("Digite o id de um ativo: ")
    ativo = ativos[id_consulta]

    try:
        ativo = ativos[id_consulta]
    except KeyError:
        print("Ativo não encontrado.")
        return

    vulnerabilidade_inicial(ativo)
    salvar_ativos_json(ativos)
    print("Vulnerabilidade cadastrada")