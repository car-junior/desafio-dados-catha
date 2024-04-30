from pandas import DataFrame

from scripts.utils.nome_colunas import Coluna
from scripts.utils.formata_dados import FormataDados


class AnalisaDados:

    @staticmethod
    def calcular_media(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        media_dados = dados.groupby(
            [Coluna.NOME_COLUNA_DATA.value, Coluna.NOME_COLUNA_ESTADO.value],
            as_index=False
        )[colunas_numericas].mean()
        FormataDados.adicionar_prefixo_em_colunas(media_dados, "MEDIA", colunas_numericas)
        return media_dados

    @staticmethod
    def calcular_desvio_padrao(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        desvio_padrao_dados = dados.groupby(
            [Coluna.NOME_COLUNA_DATA.value, Coluna.NOME_COLUNA_ESTADO.value],
            as_index=False
        )[colunas_numericas].std()
        FormataDados.adicionar_prefixo_em_colunas(desvio_padrao_dados, "DESVIO PADRAO", colunas_numericas)
        return desvio_padrao_dados

    @staticmethod
    def calcular_mediana(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz a mediana
        return dados.groupby(dados[Coluna.NOME_COLUNA_DATA.value], as_index=False).median()

    @staticmethod
    def calcular_variancia(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz a variancia
        return dados.groupby(dados[Coluna.NOME_COLUNA_DATA.value], as_index=False).var()
