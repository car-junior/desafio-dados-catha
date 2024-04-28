import pandas as pandas

from scripts.utils.nome_colunas import Coluna


class FormataDados:

    @staticmethod
    def definir_data_para_ano_mes(dataset):
        # Dropa coluna hora
        dataset.drop(columns=[Coluna.NOME_COLUNA_HORA.value], inplace=True)
        # Substitui valores negativos encontrados
        dataset.replace(-9999, 0, inplace=True)

        # Transforma coluna em tipo datetime
        dataset[Coluna.NOME_COLUNA_DATA.value] = pandas.to_datetime(dataset[Coluna.NOME_COLUNA_DATA.value])

        # Converte data apenas para ANO/MES
        dataset[Coluna.NOME_COLUNA_DATA.value] = dataset[Coluna.NOME_COLUNA_DATA.value].dt.to_period('M')

        dataset['Estado - Data'] = dataset[Coluna.NOME_COLUNA_ESTADO.value].str + ' - ' + dataset[
            Coluna.NOME_COLUNA_DATA.value]
        dataset.drop(columns=[Coluna.NOME_COLUNA_DATA.value], inplace=True)
        dataset.drop(columns=[Coluna.NOME_COLUNA_ESTADO.value], inplace=True)

    @staticmethod
    def renomear_colunas_dados_2010_2018(dados_2010_2018):
        # Renomeia coluna DATA (YYYY-MM-DD) para Data
        dados_2010_2018.rename(columns={'DATA (YYYY-MM-DD)': Coluna.NOME_COLUNA_DATA.value}, inplace=True)

        # Renomeia coluna HORA (UTC) para Hora
        dados_2010_2018.rename(columns={'HORA (UTC)': Coluna.NOME_COLUNA_HORA.value}, inplace=True)

    @staticmethod
    def renomear_colunas_dados_2019_2021(dados_2019_2021):
        # Renomeia coluna HORA (UTC) para Hora
        dados_2019_2021.rename(columns={'HORA UTC': Coluna.NOME_COLUNA_HORA.value}, inplace=True)
