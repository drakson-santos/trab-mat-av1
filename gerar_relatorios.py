from banco_de_dados import salvar_resultados_em_um_novo_arquivo
from analise_dos_dados import pegar_relatorio_educacao,\
pegar_relatorio_saude, \
pegar_relatorio_mobilidade, \
pegar_relatorio_educacao_e_saude, \
pegar_relatorio_educacao_e_mobilidade, \
pegar_relatorio_saude_e_mobilidade, \
pegar_relatorio_saude_mobilidade_e_educacao, \
pegar_relatorio_saude_n_mobilidade, \
pegar_relatorio_saude_n_educacao, \
pegar_relatorio_saude_n_educacao_n_mobilidade

import os
if os.path.isfile("resultados.csv"):
    os.remove("resultados.csv")

questao = "1) Relatório Educação: Informar nome, data de nascimento e id dos cidadãos de XPTO que frequentaram a escola, menos os cidadãos que tiveram dengue."
resultado = pegar_relatorio_educacao()
salvar_resultados_em_um_novo_arquivo(questao, resultado, True)

questao = "2) Relatório Saúde: Informar nome, data de nascimento e data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, menos os cidadãos que não utilizam ônibus."
resultado = pegar_relatorio_saude()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "3) Relatório Mobilidade: Informar nome, data de nascimento e linhas de ônibus dos cidadãos de XPTO que utilizaram o transporte público e não tiveram dengue."
resultado = pegar_relatorio_mobilidade()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "4) Relatório Educação e Saúde: Informar nome, data de nascimento, id e data que tiveram dengue dos cidadãos de XPTO que frequentaram a escola e tiveram dengue."
resultado = pegar_relatorio_educacao_e_saude()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "5) Relatório Educação e Mobilidade: Informar nome, data de nascimento, id e linhas de ônibus dos cidadãos de XPTO que frequentaram a escola e utilizaram transporte público."
resultado = pegar_relatorio_educacao_e_mobilidade()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "6) Relatório Saúde e Mobilidade: Informar nome, data de nascimento, data que tiveram dengue e linhas de ônibus dos cidadãos de XPTO que frequentaram o posto de saúde e utilizaram transporte público."
resultado = pegar_relatorio_saude_e_mobilidade()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "7) Relatório Saúde, Mobilidade e Educação: Informar nome, data de nascimento, data que tiveram dengue e linhas de ônibus  dos cidadãos de XPTO que frequentaram o posto de saúde, utilizaram transporte público e frequentaram a escola"
resultado = pegar_relatorio_saude_mobilidade_e_educacao()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "8) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não utilizaram transporte público."
resultado = pegar_relatorio_saude_n_mobilidade()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "9) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola."
resultado = pegar_relatorio_saude_n_educacao()
salvar_resultados_em_um_novo_arquivo(questao, resultado)

questao = "10) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos de XPTO que frequentaram o posto de saúde, mas não frequentaram a escola, nem utilizaram transporte público."
resultado = pegar_relatorio_saude_n_educacao_n_mobilidade()
salvar_resultados_em_um_novo_arquivo(questao, resultado)