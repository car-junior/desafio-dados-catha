import pandas as pandas
from pandas import DataFrame

from scripts.utils.nome_colunas import RegistroClimatico


class FormataDados:

    @staticmethod
    def substituir_valores(dados: DataFrame):
        # Substitui valores negativos encontrados
        dados.replace(-9999, 0, inplace=True)

    @staticmethod
    def definir_data_para_ano_mes(dados: DataFrame):
        # Transforma coluna em tipo datetime
        dados[RegistroClimatico.COLUNA_DATA.value] = pandas.to_datetime(dados[RegistroClimatico.COLUNA_DATA.value])

        # Converte data apenas para ANO/MES
        dados[RegistroClimatico.COLUNA_DATA.value] = dados[RegistroClimatico.COLUNA_DATA.value].dt.to_period('M')

    @staticmethod
    def definir_coluna_para_data(dados: DataFrame):
        # Transforma coluna em tipo datetime
        dados[RegistroClimatico.COLUNA_DATA.value] = pandas.to_datetime(dados[RegistroClimatico.COLUNA_DATA.value])

    @staticmethod
    def renomear_colunas_dados_2010_2018(dados_2010_2018: DataFrame):
        # Renomeia coluna DATA (YYYY-MM-DD) para Data
        dados_2010_2018.rename(columns={"DATA (YYYY-MM-DD)": f"{RegistroClimatico.COLUNA_DATA.value}"}, inplace=True)

        # Renomeia coluna HORA (UTC) para Hora
        dados_2010_2018.rename(columns={"HORA (UTC)": f"{RegistroClimatico.COLUNA_HORA.value}"}, inplace=True)

    @staticmethod
    def renomear_colunas_dados_2019_2021(dados_2019_2021: DataFrame):
        # Renomeia coluna HORA (UTC) para Hora
        dados_2019_2021.rename(columns={'HORA UTC': f"{RegistroClimatico.COLUNA_HORA.value}"}, inplace=True)

    @staticmethod
    def adicionar_prefixo_em_colunas(dados: DataFrame, prefixo: str, colunas: []):
        dados.rename(columns={col: f"{prefixo} - {col}" for col in colunas}, inplace=True)
