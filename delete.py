from menu import validacao_entrada_inteiro, salvar_ativos_json
from busca import printar_ativo

def delete_ativo(ativos):
    """Deleta um ativo e as vulnerabilidades dele"""
    print("\n--- Deletar Ativo ---")
    id_consulta = validacao_entrada_inteiro("Digite o id de um ativo: ")

    try:
        ativo = ativos[id_consulta]
    except KeyError:
        print ("Digite um id valido, tente novamente.")
        return
    
    printar_ativo(ativo)

    validacao = input ("Tem certeza dessa ação: (S/N): ")
    if validacao != "S":
        print ("Operação Cancelada")
        return

    del ativos[id_consulta]
    salvar_ativos_json(ativos)
    print ("Ativo Deletado")
    