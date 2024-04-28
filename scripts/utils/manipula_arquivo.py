import os
from enum import Enum

from pandas import DataFrame

DADOS_POR_PERIODO = 'dados_por_periodo'
DIRETORIO_RAIZ_PROJETO = os.path.dirname(os.getcwd())


class DiretorioLerArquivo(Enum):
    REGISTRO_CLIMATICOS_2010_2012 = f"{DIRETORIO_RAIZ_PROJETO}\\registros_climaticos\\2010_2012"
    REGISTRO_CLIMATICOS_2013_2015 = f"{DIRETORIO_RAIZ_PROJETO}\\registros_climaticos\\2013_2015"
    REGISTRO_CLIMATICOS_2016_2018 = f"{DIRETORIO_RAIZ_PROJETO}\\registros_climaticos\\2016_2018"
    REGISTRO_CLIMATICOS_2019_2021 = f"{DIRETORIO_RAIZ_PROJETO}\\registros_climaticos\\2019_2021"


class TipoArquivo(Enum):
    DADOS_MEDIA_2010_2021_CSV = 'dados_media_2010_2021.csv'


class DiretorioGeraArquivo(Enum):
    DADOS_COMPLETOS = f"{DIRETORIO_RAIZ_PROJETO}\\dados_completos"


class TipoArquivoPeriodo(Enum):
    DADOS_2010_2012_CSV = 'dados_2010_2014.csv'
    DADOS_2013_2015_CSV = 'dados_2013_2015.csv'
    DADOS_2016_2018_CSV = 'dados_2016_2018.csv'
    DADOS_2019_2021_CSV = 'dados_2019_2021.csv'


class DiretorioArquivoPeriodo(Enum):
    MEDIA = f"{DIRETORIO_RAIZ_PROJETO}\\{DADOS_POR_PERIODO}\\media"
    MEDIANA = f"{DIRETORIO_RAIZ_PROJETO}\\{DADOS_POR_PERIODO}\\mediana"
    DESVIO_PADRAO = f"{DIRETORIO_RAIZ_PROJETO}\\{DADOS_POR_PERIODO}\\desvio_padrao"


def gerar_diretorio(diretorio: DiretorioArquivoPeriodo | DiretorioGeraArquivo):
    os.makedirs(f"{diretorio.value}", exist_ok=True)


class GeradorArquivo:

    @staticmethod
    def gerar_csv_periodo(dados: DataFrame, tipo_arquivo: TipoArquivoPeriodo, diretorio: DiretorioArquivoPeriodo):
        gerar_diretorio(diretorio)
        dados.to_csv(f"{diretorio.value}\\{tipo_arquivo.value}", index=False, decimal=',', sep=';')

    @staticmethod
    def gerar_csv(dados: DataFrame, tipo_arquivo: TipoArquivo, diretorio: DiretorioGeraArquivo):
        gerar_diretorio(diretorio)
        dados.to_csv(f"{diretorio.value}\\{tipo_arquivo.value}", index=False, decimal=',', sep=';')