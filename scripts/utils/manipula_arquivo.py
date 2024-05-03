import os
import shutil
from enum import Enum

from pandas import DataFrame

from configuracao import DIRETORIO_RAIZ_PROJETO

DIRETORIO_REGISTRO_CLIMATICOS_ENTRADA = f"{DIRETORIO_RAIZ_PROJETO}\\arquivos_entrada\\registros_climaticos"
CLIMAS_DADOS_POR_PERIODO = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos_temp\\periodo"
DIRETORIO_ARQUIVO_REGISTRO_ACIDENTES = f"{DIRETORIO_RAIZ_PROJETO}\\arquivos_entrada\\registros_acidentes\\base_de_acidentes.xlsx"


class DiretorioArquivoEntrada(Enum):
    REGISTRO_ACIDENTES_2010_2021 = DIRETORIO_ARQUIVO_REGISTRO_ACIDENTES
    REGISTRO_CLIMATICOS_2010_2012 = f"{DIRETORIO_REGISTRO_CLIMATICOS_ENTRADA}\\2010_2012"
    REGISTRO_CLIMATICOS_2013_2015 = f"{DIRETORIO_REGISTRO_CLIMATICOS_ENTRADA}\\2013_2015"
    REGISTRO_CLIMATICOS_2016_2018 = f"{DIRETORIO_REGISTRO_CLIMATICOS_ENTRADA}\\2016_2018"
    REGISTRO_CLIMATICOS_2019_2021 = f"{DIRETORIO_REGISTRO_CLIMATICOS_ENTRADA}\\2019_2021"


class ClimaAnaliseEstatisticaArquivo(Enum):
    MEDIA_CLIMAS_2010_2021_CSV = 'media_climas_2010_2021.csv'
    MEDIANA_CLIMAS_2010_2021_CSV = 'mediana_climas_2010_2021.csv'
    VARIANCIA_CLIMAS_2010_2021_CSV = 'variancia_climas_2010_2021.csv'
    DESVIO_PADRAO_CLIMAS_2010_2021_CSV = 'desvio_padrao_climas_2010_2021.csv'
    # Junção de media, mediana, variancia e desvio padrao
    ANALISE_ESTATISTICA_CLIMAS_2010_2021_CSV = 'analise_estatistica_climas_2010_2021.csv'


class DiretorioGeraArquivo(Enum):
    ANALISE_ESTATISTICA_ARQUIVOS = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos"
    ANALISE_ESTATISTICA_ARQUIVOS_TEMP = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos_temp"


class ClimaArquivoPeriodo(Enum):
    CLIMAS_2010_2012_CSV = 'climas_2010_2012.csv'
    CLIMAS_2013_2015_CSV = 'climas_2013_2015.csv'
    CLIMAS_2016_2018_CSV = 'climas_2016_2018.csv'
    CLIMAS_2019_2021_CSV = 'climas_2019_2021.csv'


class ClimaDiretorioPeriodo(Enum):
    MEDIA = f"{CLIMAS_DADOS_POR_PERIODO}\\media"
    MEDIANA = f"{CLIMAS_DADOS_POR_PERIODO}\\mediana"
    VARIANCIA = f"{CLIMAS_DADOS_POR_PERIODO}\\variancia"
    DESVIO_PADRAO = f"{CLIMAS_DADOS_POR_PERIODO}\\desvio_padrao"


def gerar_diretorio(diretorio: ClimaDiretorioPeriodo | DiretorioGeraArquivo):
    os.makedirs(f"{diretorio.value}", exist_ok=True)


class GeradorArquivo:

    @staticmethod
    def gerar_csv_periodo(dados: DataFrame, tipo_arquivo: ClimaArquivoPeriodo, diretorio: ClimaDiretorioPeriodo):
        gerar_diretorio(diretorio)
        dados.to_csv(f"{diretorio.value}\\{tipo_arquivo.value}", index=False, decimal=',', sep=';', encoding='utf-8')

    @staticmethod
    def gerar_csv(dados: DataFrame, tipo_arquivo: ClimaAnaliseEstatisticaArquivo, diretorio: DiretorioGeraArquivo):
        gerar_diretorio(diretorio)
        dados.to_csv(f"{diretorio.value}\\{tipo_arquivo.value}", index=False, decimal=',', sep=';', encoding='utf-8')

    @staticmethod
    def remover_diretorio_arquivos(diretorio):
        shutil.rmtree(diretorio)
