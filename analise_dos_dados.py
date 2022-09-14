from banco_de_dados import pegar_dados, salvar_dados_em_um_novo_arquivo

CONJUNTOS_DOS_IDS, BANCO_DE_DADOS = pegar_dados()

def pegar_dados_da_pessoas(nome_do_conjunto, ids, colunas=[]):
    dados = []
    for id in ids:
        elemento = {}

        for pessoa in BANCO_DE_DADOS[nome_do_conjunto]:
            if pessoa["ID"] == id:
                if len(colunas):
                    elemento
                    for coluna in colunas:
                        elemento[coluna] = pessoa[coluna]
                else:
                    elemento = pessoa

        dados.append(elemento)
    return dados


def pegar_relatorio_educacao():
    # 1) Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO que
    # frequentaram a escola, menos os cidadãos que tiveram dengue.
    colunas_solicitadas = ["ID", "Nome", "Data de Nascimento"]

    resultado_ids = CONJUNTOS_DOS_IDS["alunos"] - CONJUNTOS_DOS_IDS["dengue"]
    dados = pegar_dados_da_pessoas("universo", resultado_ids, colunas_solicitadas)

    salvar_dados_em_um_novo_arquivo(
        "relatorio_educacao",
        colunas_solicitadas,
        dados
    )

    return len(dados)

def pegar_relatorio_saude_mobilidade_e_educacao():
    # 7) Relatório Saúde, Mobilidade e Educação: Informar nome, data de nascimento, data que
    # tiveram dengue e linhas de ônibus  dos cidadãos de XPTO que frequentaram o posto de saúde,
    # utilizaram transporte público e frequentaram a escola.
    # colunas_solicitadas = ["ID", "Nome", "Data de Nascimento", "Data da Dengue", "onibus"]
    colunas_solicitadas = ["ID", "Nome", "Data de Nascimento", "Data da Dengue", "Ônibus"]

    resultado_ids = CONJUNTOS_DOS_IDS["dengue"] & CONJUNTOS_DOS_IDS["onibus"] & CONJUNTOS_DOS_IDS["alunos"]
    dados = pegar_dados_da_pessoas("universo", resultado_ids, colunas_solicitadas)
    salvar_dados_em_um_novo_arquivo(
        "relatorio_saude_mobilidade_e_educacao",
        colunas_solicitadas,
        dados
    )

pegar_relatorio_educacao()
pegar_relatorio_saude_mobilidade_e_educacao()