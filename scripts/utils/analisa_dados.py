from pandas import DataFrame

from scripts.utils.nome_colunas import RegistroClimatico, RegistroAcidente
from scripts.utils.formata_dados import FormataDados


class AnalisaDados:

    @staticmethod
    def calcular_media(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        media_dados = dados.groupby(
            [RegistroClimatico.COLUNA_DATA.value, RegistroClimatico.COLUNA_ESTADO.value],
            as_index=False
        )[colunas_numericas].mean()
        FormataDados.adicionar_prefixo_em_colunas(media_dados, "MEDIA", colunas_numericas)
        return media_dados

    @staticmethod
    def calcular_desvio_padrao(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        desvio_padrao_dados = dados.groupby(
            [RegistroClimatico.COLUNA_DATA.value, RegistroClimatico.COLUNA_ESTADO.value],
            as_index=False
        )[colunas_numericas].std()
        FormataDados.adicionar_prefixo_em_colunas(desvio_padrao_dados, "DESVIO PADRAO", colunas_numericas)
        return desvio_padrao_dados

    @staticmethod
    def calcular_mediana(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz a mediana
        return dados.groupby(dados[RegistroClimatico.COLUNA_DATA.value], as_index=False).median()

    @staticmethod
    def calcular_variancia(dados: DataFrame) -> DataFrame:
        # Agrupa dados por ano e mes e faz a variancia
        return dados.groupby(dados[RegistroClimatico.COLUNA_DATA.value], as_index=False).var()

    @staticmethod
    def calcular_quantidade_acidentes(dados: DataFrame) -> DataFrame:
        return dados.groupby([
            RegistroAcidente.COLUNA_ESTADO.value,
            RegistroAcidente.COLUNA_OCORRENCIA_CLASSIFICACAO.value,
            RegistroAcidente.COLUNA_OCORRENCIA_DIA.value
        ]).size().reset_index(name="quantidades")

# FAZER UM FILTRO
# dados.loc[dados[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] == '23/09/2017']