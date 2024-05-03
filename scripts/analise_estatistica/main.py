from scripts.utils.manipula_arquivo import GeradorArquivo, DiretorioGeraArquivo, DiretorioArquivoPeriodo
from scripts.utils.manipula_arquivo import TipoArquivo
from scripts.utils.monta_dados import MontaDados

# Executa analise estatistica gerando media, mediana, desvio padrao e variancia para os dados de clima por periodo
# Foi feito dividido em periodos porque a quantidade de dados para analisar é imensa, dividindo ficou mais leve trabalhar
# com os dados em memoria

print("Criando dados do registros climáticos a partir de 2010 a 2012")
exec(open("analise_climas_2010_2012.py").read())

print("Criando dados do registros climáticos a partir de 2013 a 2015")
exec(open("analise_climas_2013_2015.py").read())

print("Criando dados do registros climáticos a partir de 2016 a 2018")
exec(open("analise_climas_2016_2018.py").read())

print("Criando dados do registros climáticos a partir de 2019 a 2021")
exec(open("analise_climas_2019_2021.py").read())

# Nesta etapa é feito a junção da analise estatistica por periodo em apenas um intervalo de 2010 a 2021
# para media, mediana, desvio padrao e variancia

media_dados_2010_2021 = MontaDados.via_arquivos_csv_gerados(caminho_raiz=DiretorioArquivoPeriodo.MEDIA)
GeradorArquivo.gerar_csv(media_dados_2010_2021,
                         TipoArquivo.MEDIA_DADOS_2010_2021_CSV,
                         DiretorioGeraArquivo.ANALISE_ESTATISTICA_ARQUIVOS_TEMP)
del media_dados_2010_2021

desvio_padrao_dados_2010_2021 = MontaDados.via_arquivos_csv_gerados(caminho_raiz=DiretorioArquivoPeriodo.DESVIO_PADRAO)
GeradorArquivo.gerar_csv(desvio_padrao_dados_2010_2021,
                         TipoArquivo.DESVIO_PADRAO_DADOS_2010_2021_CSV,
                         DiretorioGeraArquivo.ANALISE_ESTATISTICA_ARQUIVOS_TEMP)
del desvio_padrao_dados_2010_2021

mediana_dados_2010_2021 = MontaDados.via_arquivos_csv_gerados(caminho_raiz=DiretorioArquivoPeriodo.MEDIANA)
GeradorArquivo.gerar_csv(mediana_dados_2010_2021,
                         TipoArquivo.MEDIANA_DADOS_2010_2021_CSV,
                         DiretorioGeraArquivo.ANALISE_ESTATISTICA_ARQUIVOS_TEMP)
del mediana_dados_2010_2021

variancia_dados_2010_2021 = MontaDados.via_arquivos_csv_gerados(caminho_raiz=DiretorioArquivoPeriodo.VARIANCIA)
GeradorArquivo.gerar_csv(variancia_dados_2010_2021,
                         TipoArquivo.VARIANCIA_DADOS_2010_2021_CSV,
                         DiretorioGeraArquivo.ANALISE_ESTATISTICA_ARQUIVOS_TEMP)
del variancia_dados_2010_2021

# Nesta etapa é feito um merge de todas analises estatisticas(media, mediana, desvio padrao e variancia de 2010 a 2021)
# em apenas um unico arquivo csv de 2010 a 2021

# TODO:
# Deletar os arquivos_temp temporarios por periodos
# Deletar os temporarios por analise estatistica de 2010 a 2021

print("Gerando analise estatistica dos dados analisados(media, mediana, desviao padrao e variancia 2010 a 2021)")
# Faz juncao das analises estatisticas em um unico dataframe
merge_analise_estatistica = MontaDados.merge_analise_estatistica_clima()
GeradorArquivo.gerar_csv(
    merge_analise_estatistica,
    TipoArquivo.ANALISE_ESTATISTICA_DADOS_CLIMA_2010_2021_CSV,
    DiretorioGeraArquivo.ANALISE_ESTATISTICA_ARQUIVOS
)


