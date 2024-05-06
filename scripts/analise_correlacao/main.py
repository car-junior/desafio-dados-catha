# Calcula media de climas 2013 a 2015 e gera csv
import os.path

import pandas
import seaborn as sn
from matplotlib import pyplot as plt

from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import DiretorioArquivoEntrada
from scripts.utils.monta_dados import MontaDados
from scripts.utils.nome_colunas import RegistroAcidente, RegistroClimatico


def remover_utc(valor: str):
    valor = valor.replace(" UTC", "")
    posicao = 2
    return valor[:posicao] + ":" + valor[posicao:]


def arrendodar_hora(valor: str):
    posicao = 2
    return valor[:posicao] + ":00"


# calcula correlacao de variaveis com quantidades de acidentes
if os.path.exists("climas_acidentes_2013_2021.csv"):
    merge_climas_acidentes = pandas.read_csv("climas_acidentes_2013_2021.csv", decimal=",", sep=";")
    merge_climas_acidentes = merge_climas_acidentes.drop("ESTADO", axis=1)
    merge_climas_acidentes = merge_climas_acidentes.drop("DATA", axis=1)
    merge_climas_acidentes = merge_climas_acidentes.drop("HORA", axis=1)

    correlacao = merge_climas_acidentes.corr("pearson")
    sn.heatmap(correlacao, annot=True, fmt=".1f", linewidths=.4)
    plt.figure(figsize=(12, 10))
    plt.show()

# Gera CSV com media de climas por dia/mes/ano e hora e estado
else:
    climas_2013_2015 = MontaDados.via_arquivos_csv_clima(diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2013_2015)
    FormataDados.renomear_colunas_dados_2010_2018(climas_2013_2015)

    climas_2016_2018 = MontaDados.via_arquivos_csv_clima(diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2016_2018)
    FormataDados.renomear_colunas_dados_2010_2018(climas_2016_2018)

    climas_2013_2018 = pandas.concat([climas_2013_2015, climas_2016_2018], ignore_index=True)
    climas_2013_2018[RegistroClimatico.COLUNA_HORA.value] = climas_2013_2018[RegistroClimatico.COLUNA_HORA.value].astype(str)
    climas_2013_2018[RegistroClimatico.COLUNA_DATA.value] = pandas.to_datetime(
        climas_2013_2018[RegistroClimatico.COLUNA_DATA.value]
    )
    FormataDados.substituir_valores(climas_2013_2018)

    climas_2019_2021 = MontaDados.via_arquivos_csv_clima(diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2019_2021)
    FormataDados.renomear_colunas_dados_2019_2021(climas_2019_2021)
    climas_2019_2021['DATA'] = pandas.to_datetime(climas_2019_2021['DATA'])
    climas_2019_2021['HORA'] = climas_2019_2021['HORA'].astype(str)
    climas_2019_2021['HORA'] = climas_2019_2021['HORA'].apply(remover_utc)

    climas_2013_2021 = pandas.concat([climas_2013_2018, climas_2019_2021], ignore_index=True)
    climas_2013_2021.dropna(how='all', inplace=True)
    climas_2013_2021['HORA'] = climas_2013_2021['HORA'].astype(str)
    climas_2013_2021['DATA'] = pandas.to_datetime(climas_2013_2021['DATA']).dt.date

    media_climas_2013_2021 = AnalisaDados.calcular_media_por_data_hora_estado(climas_2013_2021)

    acidentes_2013_2022 = MontaDados.via_arquivo_excel_acidentes(
        DiretorioArquivoEntrada.REGISTRO_ACIDENTES_2013_2022,
        RegistroAcidente.colunas_para_ler()
    )
    acidentes_2013_2021 = acidentes_2013_2022[
        acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value].dt.year != 2022
        ]
    acidentes = AnalisaDados.calcular_quantidade_acidentes(acidentes_2013_2021)
    acidentes[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] = pandas.to_datetime(
        acidentes[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value]).dt.date
    acidentes = acidentes.rename(
        columns={
            RegistroAcidente.COLUNA_ESTADO.value: 'ESTADO',
            RegistroAcidente.COLUNA_OCORRENCIA_DIA.value: 'DATA',
            RegistroAcidente.COLUNA_OCORRENCIA_HORA.value: 'HORA'
        }
    )
    acidentes['HORA'] = acidentes['HORA'].astype(str)
    acidentes['HORA'] = acidentes['HORA'].apply(arrendodar_hora)

    # remove coluna string ocorrencia
    acidentes = acidentes.drop(f"{RegistroAcidente.COLUNA_OCORRENCIA_CLASSIFICACAO.value}", axis=1)
    # remove linhas vazias
    acidentes.dropna(how='all', inplace=True)

    # faz merge
    merge_colunas_base = ['ESTADO', 'DATA', 'HORA']
    merge_climas_acidentes = pandas.merge(media_climas_2013_2021, acidentes, on=merge_colunas_base, how='left')

    # zera onde nao tem valor
    merge_climas_acidentes.fillna(0, inplace=True)
    merge_climas_acidentes = merge_climas_acidentes[merge_climas_acidentes['QTD. ACIDENTES'] != 0]
    merge_climas_acidentes['QTD. ACIDENTES'] = merge_climas_acidentes['QTD. ACIDENTES'].astype(int)

    merge_climas_acidentes.to_csv("climas_acidentes_2013_2021.csv", index=False, sep=';', decimal=",", encoding='utf-8')
