from menu import validacao_entrada_inteiro
from busca import printar_ativo
from menu import TipoAtivo
from menu import exibir_tipos
from menu import salvar_ativos_json


def atualizar_ativo(ativos):
    print("\n--- Atualização de Ativo ---")
    id_busca = validacao_entrada_inteiro("Digite o ID do ativo: ")

    try:
        ativo = ativos[id_busca]
    except KeyError:
        print("Ativo não encontrado.")
        return

    printar_ativo(ativo)         

    print("\nQual campo deseja atualizar?")
    print("1 - Hostname")
    print("2 - Responsável")
    print("3 - Setor")
    print("4 - Tipo de ativo")
    print("0 - Cancelar")

    opcao_ativo = validacao_entrada_inteiro("Escolha: ", minimo=0, maximo=4)

    match opcao_ativo:
        case 1:
            ativo["hostname"]    = input("Novo hostname: ")
        case 2:
            ativo["responsavel"] = input("Novo responsável: ")
        case 3:
            ativo["setor"]       = input("Novo setor: ")
        case 4:
            exibir_tipos()
            tipo = validacao_entrada_inteiro("Novo tipo: ", minimo=1, maximo=8)
            ativo["tipo_ativo"]  = TipoAtivo(tipo).name
        case 0:
            print("Atualização cancelada.")
            return

    ativos[id_busca] = ativo   
    salvar_ativos_json(ativos)    # salva no JSON
    print("Ativo atualizado com sucesso.")
    printar_ativo(ativo)          