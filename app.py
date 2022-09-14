from manipulador_de_arquivo import buscar_dados, escrever_no_arquivo_csv, pegar_dados

BANCO_DE_DADOS, BANCO_DE_DADOS_IDS = pegar_dados()


def show(con, con_2=[]):
    print(len(con))
    if con_2:
        print(len(con_2))


def pegar_relatorio_educacao():
    # 1) Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO que frequentaram a escola, menos os cidadãos que tiveram dengue.
    resultado_ids = BANCO_DE_DADOS_IDS["alunos"] - BANCO_DE_DADOS_IDS["dengue"]

    dados = buscar_dados(resultado_ids, "alunos")
    # escrever_no_arquivo_csv("relatorio_educacao", {
    #     "questao": "1) Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO que frequentaram a escola, menos os cidadãos que tiveram dengue.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_educacao()


def pegar_relatorio_saude():
    # 2) Relatório Saúde: Informar nome, data de nascimento e data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, menos os cidadãos que não utilizam ônibus.
    resultado_ids = BANCO_DE_DADOS_IDS["universo"] & BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "dengue")
    # escrever_no_arquivo_csv("relatorio_saude", {
    #     "questao": "2) Relatório Saúde: Informar nome, data de nascimento e data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, menos os cidadãos que não utilizam ônibus.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_saude()


def pegar_relatorio_mobilidade():
    # 3) Relatório Mobilidade: Informar nome, data de nascimento e linhas de ônibus dos cidadãos de XPTO que utilizaram o transporte público e não tiveram dengue.
    resultado_ids = BANCO_DE_DADOS_IDS["onibus"] - BANCO_DE_DADOS_IDS["dengue"]

    dados = buscar_dados(resultado_ids, "onibus")
    # escrever_no_arquivo_csv("relatorio_mobilidade", {
    #     "questao": "3) Relatório Mobilidade: Informar nome, data de nascimento e linhas de ônibus dos cidadãos de XPTO que utilizaram o transporte público e não tiveram dengue.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_mobilidade()


def pegar_relatorio_educacao_e_saude():
    # 4) Relatório Educação e Saúde: Informar nome, data de nascimento, id e data que tiveram dengue dos cidadãos de XPTO que frequentaram a escola e tiveram dengue.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["alunos"]

    dados = buscar_dados(resultado_ids, "dengue")
    # escrever_no_arquivo_csv("relatorio_educacao_e_saude", {
    #     "questao": "4) Relatório Educação e Saúde: Informar nome, data de nascimento, id e data que tiveram dengue dos cidadãos de XPTO que frequentaram a escola e tiveram dengue.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_educacao_e_saude()


def pegar_relatorio_educacao_e_mobilidade():
    # 5) Relatório Educação e Mobilidade: Informar nome, data de nascimento, id e linhas de ônibus dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["alunos"] & BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "alunos")
    # escrever_no_arquivo_csv("relatorio_educacao_e_mobilidade", {
    #     "questao": "5) Relatório Educação e Mobilidade: Informar nome, data de nascimento, id e linhas de ônibus dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_educacao_e_mobilidade()


def pegar_relatorio_saude_e_mobilidade():
    # 6) Relatório Saúde e Mobilidade: Informar nome, data de nascimento, data que tiveram dengue e linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "dengue")
    # escrever_no_arquivo_csv("relatorio_saude_e_mobilidade", {
    #     "questao": "6) Relatório Saúde e Mobilidade: Informar nome, data de nascimento, data que tiveram dengue e linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_saude_e_mobilidade()

def juntar_dados(lista_principal, lista_secundaria, colunas = []):
    dados = []

    for principal in lista_principal:
        id_principal = principal[0]

        dados_da_pessoa: list = principal

        for secundaria in lista_secundaria:
            id_secundaria = secundaria[0]

            if id_principal == id_secundaria:
                for coluna in colunas:
                    dados_da_pessoa.append(secundaria[coluna])

        dados.append(dados_da_pessoa)

    return dados

def pegar_relatorio_saude_mobilidade_e_educacao():
    # 7) Relatório Saúde, Mobilidade e Educação: Informar nome, data de nascimento, data que tiveram dengue e linhas de ônibus  dos cidadãos de XPTO que frequentaram o posto de saúde, utilizaram transporte público e frequentaram a escola.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"] & BANCO_DE_DADOS_IDS["alunos"]

    dados_dengue = buscar_dados(resultado_ids, "dengue")
    dados_onibus = buscar_dados(resultado_ids, "onibus")

    colunas = ["ID", "Nome", "Nome da Mae", "Nome do Pai", "Sexo", "Data de Nascimento", "onibus"]
    escrever_no_arquivo_csv("relatorio_saude_mobilidade_e_educacao", {
        "questao": "7) Relatório Saúde, Mobilidade e Educação: Informar nome, data de nascimento, data que tiveram dengue e linhas de ônibus  dos cidadãos de XPTO que frequentaram o posto de saúde, utilizaram transporte público e frequentaram a escola.",
        "dados": juntar_dados(dados_dengue, dados_onibus, [6]),
        "colunas": colunas,
    })


pegar_relatorio_saude_mobilidade_e_educacao()


def pegar_relatorio_saude_n_mobilidade():
    # 8) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] - BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "dengue")
    # escrever_no_arquivo_csv("relatorio_saude_n_mobilidade", {
    #     "questao": "8) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não utilizaram transporte público.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_saude_n_mobilidade()


def pegar_relatorio_saude_n_educacao():
    # 9) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola.
    resultado_ids = (BANCO_DE_DADOS_IDS["universo"] &
                     BANCO_DE_DADOS_IDS["dengue"]) - BANCO_DE_DADOS_IDS["alunos"]

    dados = buscar_dados(resultado_ids, "dengue")
    # escrever_no_arquivo_csv("relatorio_saude_n_educacao", {
    #     "questao": "9) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola.",
    #     "dados": dados
    # })

    show(dados)


pegar_relatorio_saude_n_educacao()


def pegar_relatorio_saude_n_educacao_n_mobilidade():
    # 10) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde,
    # mas não frequentaram a escola, nem utilizaram transporte público.
    resultado_ids = ((BANCO_DE_DADOS_IDS["dengue"] - BANCO_DE_DADOS_IDS["alunos"]) - BANCO_DE_DADOS_IDS["onibus"])
    dados = buscar_dados(resultado_ids, "dengue")

    colunas = ["ID", "Nome", "Nome da Mae", "Nome do Pai", "Sexo", "Data de Nascimento"]
    escrever_no_arquivo_csv("relatorio_saude_n_educacao_n_mobilidade", {
        "questao": "10) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola, nem utilizaram transporte público.",
        "dados": dados,
        "colunas": colunas
    })

    show(dados)

pegar_relatorio_saude_n_educacao_n_mobilidade()
