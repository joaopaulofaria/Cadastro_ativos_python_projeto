from menu import validacao_entrada_inteiro
from busca import printar_ativo
from menu import salvar_ativos_json

def delete_ativo(ativos):
    print ("Deletar ativo")
    id_consulta = validacao_entrada_inteiro("Digite o id de um ativo: ")

    try:
        ativo = ativos[id_consulta]
    except KeyError:
        print ("Digite um id valido, tente novamente.")
        return
    
    printar_ativo(ativo)

    validacao = input ("Tem certeza dessa ação: (S/N)")
    if validacao != "S":
        print ("Operação Cancelada")

    del ativos[id_consulta]
    salvar_ativos_json(ativos)
    print ("Ativo Deletado")
    