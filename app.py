from manipulador_de_arquivo import buscar_dados, escrever_no_arquivo_csv, pegar_dados

print(0)
BANCO_DE_DADOS, BANCO_DE_DADOS_IDS = pegar_dados()


def pegar_relatorio_educacao():
    # 1 - cidadãos de XPTO que frequentaram a escola, menos os cidadãos que tiveram dengue.
    resultado_ids = BANCO_DE_DADOS_IDS["alunos"] - BANCO_DE_DADOS_IDS["dengue"]

    dados = buscar_dados(resultado_ids, "alunos")
    escrever_no_arquivo_csv("relatorio_educacao", dados)


pegar_relatorio_educacao()


def pegar_relatorio_saude():
    # 2 - cidadãos de XPTO que tiveram dengue, menos os cidadãos que não utilizam ônibus.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] - BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_saude", dados)


pegar_relatorio_saude()


def pegar_relatorio_mobilidade():
    # 3 - cidadãos de XPTO que utilizaram o transporte público e não tiveram dengue.
    resultado_ids = BANCO_DE_DADOS_IDS["onibus"] - BANCO_DE_DADOS_IDS["dengue"]

    dados = buscar_dados(resultado_ids, "onibus")
    escrever_no_arquivo_csv("relatorio_mobilidade", dados)


pegar_relatorio_mobilidade()


def pegar_relatorio_educacao_e_saude():
    # 4 - cidadãos de XPTO que tiveram dengue e frequentaram a escola.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["alunos"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_educacao_e_saude", dados)


pegar_relatorio_educacao_e_saude()


def pegar_relatorio_educacao_e_mobilidade():
    # 5 - linhas de ônibus dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["alunos"] & BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "alunos")
    escrever_no_arquivo_csv("relatorio_educacao_e_mobilidade", dados)


pegar_relatorio_educacao_e_mobilidade()


def pegar_relatorio_saude_e_mobilidade():
    # 6 - linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_saude_e_mobilidade", dados)


pegar_relatorio_saude_e_mobilidade()


def pegar_relatorio_saude_mobilidade_e_educacao():
    # 7 - cidadãos de XPTO que frequentaram o posto de saúde, utilizaram transporte público e frequentaram a escola.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"] & BANCO_DE_DADOS_IDS["alunos"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_saude_mobilidade_e_educacao", dados)


pegar_relatorio_saude_mobilidade_e_educacao()


def pegar_relatorio_saude_n_mobilidade():
    # 8 - cidadãos de XPTO que frequentaram o posto de saúde, mas não utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] - BANCO_DE_DADOS_IDS["onibus"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_saude_n_mobilidade", dados)


pegar_relatorio_saude_n_mobilidade()


def pegar_relatorio_saude_n_educacao():
    # 9 - cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"] & BANCO_DE_DADOS_IDS["alunos"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_saude_n_educacao", dados)


pegar_relatorio_saude_n_educacao()


def pegar_relatorio_saude_n_educacao_n_mobilidade():
    # 10 - cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola, nem utilizaram transporte público.
    resultado_ids = BANCO_DE_DADOS_IDS["dengue"] & BANCO_DE_DADOS_IDS["onibus"] & BANCO_DE_DADOS_IDS["alunos"]

    dados = buscar_dados(resultado_ids, "dengue")
    escrever_no_arquivo_csv("relatorio_saude_n_educacao_n_mobilidade", dados)


pegar_relatorio_saude_n_educacao_n_mobilidade()
