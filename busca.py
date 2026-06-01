from menu import validacao_entrada_inteiro

def consulta_ativo(ativos):
    """Consulta um ativo que esta na base de dados"""
    print("\n--- Consulta de Ativo ---")
    id_consulta = validacao_entrada_inteiro("Digite o numero do ativo: ")
    try:
        ativo = ativos[id_consulta]
        printar_ativo(ativo)
    except KeyError:
        print("Ativo não encontrado.")

def printar_ativo(ativo):
    """Printa o ativo e as vulnerabilidades dele"""
    print("\n------------------------------------------")
    print ("ID: " + str(ativo['id']))
    print ("Hostname: " + ativo['hostname'])
    print ("Responsável: " + ativo['responsavel'])
    print ("Setor: " + ativo['setor'])
    print ("Tipo: " + ativo['tipo_ativo'])

    if ativo["vulnerabilidades"]:
        print("  Vulnerabilidades:")
        for i, vuln in enumerate(ativo["vulnerabilidades"], start=1):
            print (i)
            print ("Descricao: " + vuln['descricao'])
            print ("Categoria: "  + vuln['categoria'])
            print ("Severidade:" + vuln['severidade'])
            print ("Status: " + vuln['status'])
    else:
        print("Sem vulnerabilidades registradas.")

    print("------------------------------------------")
