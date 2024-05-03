import os
from enum import Enum

from pandas import DataFrame

from configuracao import DIRETORIO_RAIZ_PROJETO

CLIMAS_DADOS_POR_PERIODO = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos_temp"
DIRETORIO_REGISTRO_CLIMATICOS = f"{DIRETORIO_RAIZ_PROJETO}\\arquivos_entrada\\registros_climaticos"
DIRETORIO_ARQUIVO_REGISTRO_ACIDENTES = f"{DIRETORIO_RAIZ_PROJETO}\\arquivos_entrada\\registros_acidentes\\base_de_acidentes.xlsx"


class DiretorioLerArquivo(Enum):
    REGISTRO_ACIDENTES_2010_2021 = DIRETORIO_ARQUIVO_REGISTRO_ACIDENTES
    REGISTRO_CLIMATICOS_2010_2012 = f"{DIRETORIO_REGISTRO_CLIMATICOS}\\2010_2012"
    REGISTRO_CLIMATICOS_2013_2015 = f"{DIRETORIO_REGISTRO_CLIMATICOS}\\2013_2015"
    REGISTRO_CLIMATICOS_2016_2018 = f"{DIRETORIO_REGISTRO_CLIMATICOS}\\2016_2018"
    REGISTRO_CLIMATICOS_2019_2021 = f"{DIRETORIO_REGISTRO_CLIMATICOS}\\2019_2021"


class TipoArquivo(Enum):
    MEDIA_DADOS_2010_2021_CSV = 'media_dados_2010_2021.csv'
    DESVIO_PADRAO_DADOS_2010_2021_CSV = 'desvio_padrao_dados_2010_2021.csv'
    MEDIANA_DADOS_2010_2021_CSV = 'mediana_dados_2010_2021.csv'
    VARIANCIA_DADOS_2010_2021_CSV = 'variancia_dados_2010_2021.csv'
    ANALISE_ESTATISTICA_DADOS_CLIMA_2010_2021_CSV = 'analise_estatistica_dados_clima_2010_2021.csv'
    CONTAGEM_REGISTROS_ACIDENTES_2010_2021_CSV = 'contagem_registros_acidentes_2010_2021.csv'


class DiretorioGeraArquivo(Enum):
    ANALISE_ESTATISTICA_ARQUIVOS = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos"
    ANALISE_ESTATISTICA_ARQUIVOS_TEMP = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos_temp"
    ARQUIVOS_CLIMA_PERIODO_TEMP = f"{DIRETORIO_RAIZ_PROJETO}\\scripts\\analise_estatistica\\arquivos_clima_periodo_temp"


class TipoArquivoPeriodo(Enum):
    DADOS_2010_2012_CSV = 'dados_2010_2012.csv'
    DADOS_2013_2015_CSV = 'dados_2013_2015.csv'
    DADOS_2016_2018_CSV = 'dados_2016_2018.csv'
    DADOS_2019_2021_CSV = 'dados_2019_2021.csv'


class DiretorioArquivoPeriodo(Enum):
    MEDIA = f"{CLIMAS_DADOS_POR_PERIODO}\\media"
    MEDIANA = f"{CLIMAS_DADOS_POR_PERIODO}\\mediana"
    VARIANCIA = f"{CLIMAS_DADOS_POR_PERIODO}\\variancia"
    DESVIO_PADRAO = f"{CLIMAS_DADOS_POR_PERIODO}\\desvio_padrao"


def gerar_diretorio(diretorio: DiretorioArquivoPeriodo | DiretorioGeraArquivo):
    os.makedirs(f"{diretorio.value}", exist_ok=True)


class GeradorArquivo:

    @staticmethod
    def gerar_csv_periodo(dados: DataFrame, tipo_arquivo: TipoArquivoPeriodo, diretorio: DiretorioArquivoPeriodo):
        gerar_diretorio(diretorio)
        dados.to_csv(f"{diretorio.value}\\{tipo_arquivo.value}", index=False, decimal=',', sep=';', encoding='utf-8')

    @staticmethod
    def gerar_csv(dados: DataFrame, tipo_arquivo: TipoArquivo, diretorio: DiretorioGeraArquivo):
        gerar_diretorio(diretorio)
        dados.to_csv(f"{diretorio.value}\\{tipo_arquivo.value}", index=False, decimal=',', sep=';', encoding='utf-8')
