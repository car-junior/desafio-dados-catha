import glob
import os

import pandas as pandas
from unidecode import unidecode

from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo, DiretorioLerArquivo
from scripts.utils.nome_colunas import RegistroClimatico, RegistroAcidente


def _obter_estado(caminho_arquivo):
    linha_estado = 2
    # Abrir o arquivo CSV em modo de leitura
    with open(caminho_arquivo, 'r') as arquivo:
        for _ in range(linha_estado - 1):
            # Obtem estado do arquivo atual
            arquivo.readline()

        estado = arquivo.readline().replace("\n", "")[-2:]
        arquivo.close()
        return estado


def _processar_csv_clima(arquivo, separator, skip_rows, encoding):
    try:
        estado = _obter_estado(arquivo)
        dados_csv = pandas.read_csv(arquivo, sep=separator, skiprows=skip_rows, encoding=encoding, decimal=',')
        dados_csv.columns = dados_csv.columns.str.strip().str.upper().map(unidecode)
        # adiciona estado nas colunas
        dados_csv[RegistroClimatico.COLUNA_ESTADO.value] = estado
        return dados_csv
    except Exception as exception:
        print(f"Erro ao processar o arquivo {arquivo}: {exception}")


def _processar_csv_gerado(arquivo):
    try:
        return pandas.read_csv(arquivo, sep=";", encoding='utf-8', decimal=',')
    except Exception as exception:
        print(f"Erro ao processar o arquivo {arquivo}: {exception}")


def _processar_excel_acidentes(arquivo, colunas_para_ler):
    try:
        dados_acidentes = pandas.read_excel(arquivo, usecols=colunas_para_ler)
        dados_acidentes.drop_duplicates(subset=RegistroAcidente.obter_duplicadas(), inplace=True)
        return dados_acidentes
    except Exception as exception:
        print(f"Erro ao processar o arquivo {arquivo}: {exception}")


class MontaDados:
    SEPARADOR = ';'
    PULAR_LINHAS = 8
    CODIFICACAO = 'cp1252'

    @staticmethod
    def via_arquivos_csv_clima(caminho_raiz: DiretorioLerArquivo,
                               separador=SEPARADOR, pular_linhas=PULAR_LINHAS,
                               codificacao=CODIFICACAO):
        arquivos_csv = glob.glob(os.path.join(f"{caminho_raiz.value}", "**/*.csv"))

        conjunto_dados = [_processar_csv_clima(arquivo, separador, pular_linhas, codificacao) for arquivo in
                          arquivos_csv]

        if conjunto_dados:
            conjunto_dados = pandas.concat(conjunto_dados, ignore_index=True)
            conjunto_dados = conjunto_dados.loc[:, ~conjunto_dados.columns.str.contains('^UNNAMED')]
            return conjunto_dados
        else:
            print(f"Não foi encontrado nenhum arquivo csv em {caminho_raiz.value}")

    @staticmethod
    def via_arquivos_csv_gerados(caminho_raiz: DiretorioArquivoPeriodo):
        arquivos_csv = glob.glob(os.path.join(f"{caminho_raiz.value}", "*.csv"))

        conjunto_dados = [_processar_csv_gerado(arquivo) for arquivo in arquivos_csv]

        if conjunto_dados:
            return pandas.concat(conjunto_dados, ignore_index=False)
        else:
            print(f"Não foi encontrado nenhum arquivo csv em {caminho_raiz.value}")

    @staticmethod
    def via_arquivo_excel_acidentes(caminho_raiz: DiretorioLerArquivo, colunas_para_ler: []):
        return _processar_excel_acidentes(f"{caminho_raiz.value}", colunas_para_ler)
