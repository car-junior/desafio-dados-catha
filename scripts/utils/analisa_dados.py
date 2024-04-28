from pandas import DataFrame

from scripts.utils.nome_colunas import Coluna


class AnalisaDados:

    @staticmethod
    def calcular_media(dataset: DataFrame) -> DataFrame:
        # # Agrupa dataset por ano e mes e faz a media
        #
        # return dataset.groupby([Coluna.NOME_COLUNA_DATA.value, Coluna.NOME_COLUNA_ESTADO.value])[
        #     'RADIACAO GLOBAL (KJ/M2)'].mean()
        # dataset.head(2)
        return dataset.groupby(dataset['Estado - Data'], as_index=False).mean()

    @staticmethod
    def calcular_desvio_padrao(dataset: DataFrame) -> DataFrame:
        # Agrupa dataset por ano e mes e faz o desvio padrao
        return dataset.groupby(dataset[Coluna.NOME_COLUNA_DATA.value], as_index=False).std()

    @staticmethod
    def calcular_mediana(dataset: DataFrame) -> DataFrame:
        # Agrupa dataset por ano e mes e faz a mediana
        return dataset.groupby(dataset[Coluna.NOME_COLUNA_DATA.value], as_index=False).median()

    @staticmethod
    def calcular_variancia(dataset: DataFrame) -> DataFrame:
        # Agrupa dataset por ano e mes e faz a variancia
        return dataset.groupby(dataset[Coluna.NOME_COLUNA_DATA.value], as_index=False).var()
