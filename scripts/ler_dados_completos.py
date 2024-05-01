import pandas

from scripts.utils.nome_colunas import RegistroClimatico

media_dados = pandas.read_csv("C:/Users/carlo/Downloads/dados_completos/media_dados_2010_2021.csv", sep=';',
                              decimal=',')
desvio_padrao_dados = pandas.read_csv("C:/Users/carlo/Downloads/dados_completos/desvio_padrao_dados_2010_2021.csv",
                                      sep=';', decimal=',')
mediana_dados = pandas.read_csv("C:/Users/carlo/Downloads/dados_completos/mediana_dados_2010_2021.csv", sep=';',
                                decimal=',')
variancia_dados = pandas.read_csv("C:/Users/carlo/Downloads/dados_completos/variancia_dados_2010_2021.csv", sep=';',
                                  decimal=',')

colunas_juncao = [RegistroClimatico.COLUNA_DATA.value, RegistroClimatico.COLUNA_ESTADO.value]
juncao_dados = pandas.merge(media_dados, desvio_padrao_dados, on=colunas_juncao)
juncao_dados2 = pandas.merge(mediana_dados, variancia_dados, on=colunas_juncao)
juncao = pandas.merge(juncao_dados, juncao_dados2, on=colunas_juncao)
juncao.to_csv("analise_estatistica_basica_registro_climatico_2010_2021.csv", sep=';', decimal=',')
