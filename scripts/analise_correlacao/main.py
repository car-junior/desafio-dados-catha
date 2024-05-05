import pandas
import seaborn as sn
import matplotlib.pyplot as plt
from scipy.stats import kendalltau

from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.manipula_arquivo import AnaliseCorrelacaoDiretorio, DiretorioArquivoEntrada
from scripts.utils.monta_dados import MontaDados
from scripts.utils.nome_colunas import RegistroAcidente, RegistroClimatico

media_climas_2013_2021 = MontaDados.via_arquivos_csv_gerados(diretorio=AnaliseCorrelacaoDiretorio.MEDIAS_POR_PERIODO)
acidentes_2013_2022 = MontaDados.via_arquivo_excel_acidentes(
    DiretorioArquivoEntrada.REGISTRO_ACIDENTES_2013_2022,
    RegistroAcidente.colunas_para_ler()
)
media_climas_2013_2021['DATA'] = pandas.to_datetime(media_climas_2013_2021['DATA']).dt.date

# acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] = pandas.to_datetime(
#     acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value]
# )
# acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] = acidentes_2013_2022[
#     RegistroAcidente.COLUNA_OCORRENCIA_DIA.value].dt.date

# remove linhas onde o ano é 2022
acidentes_2013_2021 = acidentes_2013_2022[
    acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value].dt.year != 2022
    ]

acidentes = AnalisaDados.calcular_quantidade_acidentes(acidentes_2013_2021)
acidentes[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] = pandas.to_datetime(
    acidentes[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value]).dt.date
acidentes = acidentes.rename(
    columns={
        RegistroAcidente.COLUNA_OCORRENCIA_DIA.value: 'DATA',
        RegistroAcidente.COLUNA_ESTADO.value: 'ESTADO'
    }
)
# remove coluna string ocorrencia
acidentes = acidentes.drop(f"{RegistroAcidente.COLUNA_OCORRENCIA_CLASSIFICACAO.value}", axis=1)

# faz merge
merge_colunas_base = [RegistroClimatico.COLUNA_DATA.value, RegistroClimatico.COLUNA_ESTADO.value]
merge_climas_acidentes = pandas.merge(media_climas_2013_2021, acidentes, on=merge_colunas_base, how='left')

# zera onde nao tem valor
merge_climas_acidentes.fillna(0, inplace=True)
merge_climas_acidentes = merge_climas_acidentes[merge_climas_acidentes['quantidades'] != 0]
merge_climas_acidentes['quantidades'] = merge_climas_acidentes['quantidades'].astype(int)
merge_climas_acidentes.to_csv("climas_qtd_acidentes_2013_2021.csv", index=False, sep=';', decimal=",", encoding='utf-8')

# REMOVE COLUNAS NAO NUMERICAS
# merge_climas_acidentes = merge_climas_acidentes.drop("ESTADO", axis=1)
# merge_climas_acidentes = merge_climas_acidentes.drop("DATA", axis=1)
#
# correlacao = merge_climas_acidentes.corr("spearman")
# sn.heatmap(correlacao, annot=True, fmt=".1f", linewidths=2.0)
# plt.show()
