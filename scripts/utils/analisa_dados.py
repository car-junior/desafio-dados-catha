from pandas import DataFrame

from scripts.utils.nome_colunas import Coluna
from scripts.utils.formata_dados import FormataDados


class AnalisaDados:

    @staticmethod
    def calcular_media(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        dados = dados.groupby(
            [Coluna.NOME_COLUNA_DATA.value, Coluna.NOME_COLUNA_ESTADO.value],
            as_index=False
        )[colunas_numericas].mean()
        FormataDados.adicionar_prefixo_em_colunas(dados, "MEDIA", colunas_numericas)
        return dados

    @staticmethod
    def calcular_desvio_padrao(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz o desvio padrao
        return dados.groupby(dados[Coluna.NOME_COLUNA_DATA.value], as_index=False).std()

    @staticmethod
    def calcular_mediana(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz a mediana
        return dados.groupby(dados[Coluna.NOME_COLUNA_DATA.value], as_index=False).median()

    @staticmethod
    def calcular_variancia(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz a variancia
        return dados.groupby(dados[Coluna.NOME_COLUNA_DATA.value], as_index=False).var()
