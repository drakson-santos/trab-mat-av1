import csv
from itertools import chain

def montar_id(nome):
    id = f"{nome}"
    return id.replace(" ", "").lower()

def montar_tabela(linhas):
    dados = []
    colunas = []
    ids_adicionados = []

    primeira_linha = 1
    for linha in linhas:

        if primeira_linha:
            colunas = linha

            segunda_linha = 0
            primeira_linha = segunda_linha
        else:
            linha[0] = montar_id(linha[1])
            id_pessoa = linha[0]
            if id_pessoa not in ids_adicionados:

                elemento = {}
                total_de_colunas = len(colunas)
                for posicao_da_coluna in range(total_de_colunas):
                    elemento[colunas[posicao_da_coluna]] = linha[posicao_da_coluna]

                ids_adicionados.append(id_pessoa)
                dados.append(elemento)
    return dados

def pegar_dados_do_arquivo_csv(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r') as arquivo_csv:
        linhas = csv.reader(arquivo_csv, delimiter=';')
        dados = montar_tabela(linhas)
        return dados

def salvar_dados_em_um_novo_arquivo(
    nome_do_arquivo,
    colunas_solicitadas,
    dados
):
    f = open(f"{nome_do_arquivo}.csv", 'w', newline='', encoding='utf-8')
    w = csv.writer(f, delimiter=';')

    w.writerow(colunas_solicitadas)
    for dado in dados:
        w.writerow(dado.values())
    f.close()

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

def montar_conjunto_universo(
    conjunto_alunos,
    conjunto_dengue,
    conjunto_onibus
):
    colunas_de_alunos = conjunto_alunos[0].keys()
    colunas_de_dengue = conjunto_dengue[0].keys()
    colunas_de_onibus = conjunto_onibus[0].keys()
    todas_as_colunas = set()
    for coluna in chain(colunas_de_alunos, colunas_de_dengue, colunas_de_onibus):
        todas_as_colunas.add(coluna)

    ids_adicionados = set()
    conjunto_universo = list()

    for aluno in conjunto_alunos:
        if aluno["ID"] not in ids_adicionados:
            conjunto_universo.append(aluno)
            ids_adicionados.add(aluno["ID"])

    def add_conjunto_universo(conjunto):
        for elemento in conjunto:
            if elemento["ID"] not in ids_adicionados:
                conjunto_universo.append(elemento)
                ids_adicionados.add(elemento["ID"])
            else:
                for adicionado_no_universo in conjunto_universo:
                    if adicionado_no_universo["ID"] == elemento["ID"]:
                        for coluna in todas_as_colunas:
                            if elemento.get(coluna):
                                adicionado_no_universo[coluna] = elemento[coluna]
    add_conjunto_universo(conjunto_onibus)
    add_conjunto_universo(conjunto_dengue)
    return conjunto_universo

def pegar_banco_de_dados():
    arquivos = {
        "alunos": "./Base de Alunos5.csv",
        "dengue": "./Base de Dengue5.csv",
        "onibus": "./Base de Onibus5.csv"
    }

    banco_alunos = pegar_dados_do_arquivo_csv(arquivos["alunos"])
    banco_dengue = pegar_dados_do_arquivo_csv(arquivos["dengue"])
    banco_onibus = pegar_dados_do_arquivo_csv(arquivos["onibus"])
    conjunto_universo = montar_conjunto_universo(banco_alunos, banco_dengue, banco_onibus)

    return {
        "alunos": banco_alunos,
        "dengue": banco_dengue,
        "onibus": banco_onibus,
        "universo": conjunto_universo
    }

def pegar_dados():
    BANCO_DE_DADOS = pegar_banco_de_dados()
    NOME_DOS_BANCOS = ["alunos", "dengue", "onibus"]
    CONJUNTO_DOS_IDS = {
        "alunos": set(),
        "dengue": set(),
        "onibus": set(),
    }

    for nome_do_banco in NOME_DOS_BANCOS:
        dados = BANCO_DE_DADOS[nome_do_banco]
        for pessoa in dados:
            CONJUNTO_DOS_IDS[nome_do_banco].add(pessoa["ID"])

    return CONJUNTO_DOS_IDS, BANCO_DE_DADOS
