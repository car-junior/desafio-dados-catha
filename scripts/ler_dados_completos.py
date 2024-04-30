import pandas

from scripts.utils.nome_colunas import RegistroClimatico

media_dados = pandas.read_csv("../dados_completos/media_dados_2010_2021.csv", sep=';', decimal=',')
desvio_padrao_dados = pandas.read_csv("../dados_completos/desvio_padrao_dados_2010_2021.csv", sep=';', decimal=',')

colunas_juncao = [RegistroClimatico.COLUNA_DATA.value, RegistroClimatico.COLUNA_ESTADO.value]
juncao_dados = pandas.merge(media_dados, desvio_padrao_dados, on=colunas_juncao)
juncao_dados.to_csv("media_desvio_padrao_registro_climatico_2010_2021.csv", sep=';', decimal=',')