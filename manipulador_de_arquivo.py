import csv

BANCO_DE_DADOS = {
    "alunos": [],
    "dengue": [],
    "onibus": [],
}

BANCO_DE_DADOS_IDS = {
    "universo": set(),
    "alunos": set(),
    "dengue": set(),
    "onibus": set(),
}

def montar_id(nome):
    id = f"{nome}"
    return id.replace(" ", "").lower()

def ler_arquivo_csv(nome_do_arquivo, conjunto):
    data = []
    ids_adicionados = []
    with open(nome_do_arquivo, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv, delimiter=';')
        linha = 0
        for row in reader:
            if linha == 0:
                linha += 1
            else:
                row[0] = montar_id(row[1])
                id_pessoa =  row[0]
                if id_pessoa not in ids_adicionados:
                    ids_adicionados.append(id_pessoa)
                    data.append(row)

                    BANCO_DE_DADOS_IDS[conjunto].add(id_pessoa)
                    BANCO_DE_DADOS_IDS["universo"].add(id_pessoa)

    return data

def escrever_no_arquivo_csv(
    nome_do_arquivo,
    dados = {
        "questao": "",
        "dados": [],
        "colunas": "",
    }
):
    f = open(f"{nome_do_arquivo}.csv", 'w', newline='', encoding='utf-8')
    w = csv.writer(f, delimiter=';')

    w.writerow(dados["colunas"])
    for row in dados["dados"]:
        w.writerow(row)
    f.close()

    # f = open(f"resultados.csv", 'a', newline='', encoding='utf-8')
    # w = csv.writer(f, delimiter=';')
    # resultado = dados["questao"], len(dados["dados"])
    # w.writerow(resultado)
    # f.close()

def pegar_dados():
    arquivos = {
        "alunos": "./Base de Alunos5.csv",
        "dengue": "./Base de Dengue5.csv",
        "onibus": "./Base de Onibus5.csv"
    }

    BANCO_DE_DADOS["alunos"] = ler_arquivo_csv(arquivos["alunos"], "alunos")
    BANCO_DE_DADOS["dengue"] = ler_arquivo_csv(arquivos["dengue"], "dengue")
    BANCO_DE_DADOS["onibus"] = ler_arquivo_csv(arquivos["onibus"], "onibus")

    return (BANCO_DE_DADOS, BANCO_DE_DADOS_IDS)


def buscar_dados(ids, nome_do_banco_de_dados):
    dados = []
    pessoas = BANCO_DE_DADOS[nome_do_banco_de_dados]
    for pessoa in pessoas:
        id = pessoa[0]
        if id in ids:
            dados.append(pessoa)

    return dados
