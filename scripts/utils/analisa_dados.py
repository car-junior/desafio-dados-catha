from pandas import DataFrame

from scripts.utils.formata_dados import FormataDados
from scripts.utils.nome_colunas import RegistroClimatico, RegistroAcidente


class AnalisaDados:

    @staticmethod
    def calcular_media(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        media_dados = dados.groupby(RegistroClimatico.agrupa_por(), as_index=False)[colunas_numericas].mean()
        FormataDados.adicionar_prefixo_em_colunas(media_dados, "MEDIA", colunas_numericas)
        return media_dados

    @staticmethod
    def calcular_desvio_padrao(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        desvio_padrao_dados = dados.groupby(RegistroClimatico.agrupa_por(), as_index=False)[colunas_numericas].std()
        FormataDados.adicionar_prefixo_em_colunas(desvio_padrao_dados, "DESVIO PADRAO", colunas_numericas)
        return desvio_padrao_dados

    @staticmethod
    def calcular_mediana(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        mediana_dados = dados.groupby(RegistroClimatico.agrupa_por(), as_index=False)[colunas_numericas].median()
        FormataDados.adicionar_prefixo_em_colunas(mediana_dados, "MEDIANA", colunas_numericas)
        return mediana_dados

    @staticmethod
    def calcular_variancia(dados: DataFrame) -> DataFrame:
        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        variancia_dados = dados.groupby(RegistroClimatico.agrupa_por(), as_index=False)[colunas_numericas].var()
        FormataDados.adicionar_prefixo_em_colunas(variancia_dados, "VARIANCIA", colunas_numericas)
        return variancia_dados

    @staticmethod
    def calcular_quantidade_acidentes(dados: DataFrame) -> DataFrame:
        return dados.groupby(RegistroAcidente.agrupa_por()).size().reset_index(name="quantidades")

# FAZER UM FILTRO
# dados.loc[dados[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] == '23/09/2017']
