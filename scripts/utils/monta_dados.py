import glob
import os

import pandas as pandas
from unidecode import unidecode

from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo
from scripts.utils.nome_colunas import Coluna


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


def _processar_csv(arquivo, separator, skip_rows, encoding):
    try:
        estado = _obter_estado(arquivo)
        arquivo_csv_lido = pandas.read_csv(arquivo, sep=separator, skiprows=skip_rows, encoding=encoding, decimal=',')
        arquivo_csv_lido.columns = arquivo_csv_lido.columns.str.strip().str.upper().map(unidecode)
        # adiciona estado nas colunas
        arquivo_csv_lido[Coluna.NOME_COLUNA_ESTADO.value] = estado
        return arquivo_csv_lido
    except Exception as exception:
        print(f"Erro ao processar o arquivo {arquivo}: {exception}")


class MontaDados:
    SEPARADOR = ';'
    PULAR_LINHAS = 8
    CODIFICACAO = 'cp1252'

    @staticmethod
    def via_arquivos_csv(caminho_raiz: DiretorioArquivoPeriodo,
                         separador=SEPARADOR, pular_linhas=PULAR_LINHAS,
                         codificacao=CODIFICACAO):
        arquivos_csv = glob.glob(os.path.join(f"{caminho_raiz.value}", "**/*.csv"))

        conjunto_dados = [_processar_csv(arquivo, separador, pular_linhas, codificacao) for arquivo in arquivos_csv]

        if conjunto_dados:
            return pandas.concat(conjunto_dados, ignore_index=True)
        else:
            print(f"Não foi encontrado nenhum arquivo csv em {caminho_raiz.value}")

    @staticmethod
    def via_arquivos_csv_gerados(caminho_raiz: DiretorioArquivoPeriodo,
                                 separador=SEPARADOR, pular_linhas=PULAR_LINHAS,
                                 codificacao=CODIFICACAO):
        arquivos_csv = glob.glob(os.path.join(f"{caminho_raiz.value}", "*.csv"))

        conjunto_dados = [_processar_csv(arquivo, separador, pular_linhas, codificacao) for arquivo in arquivos_csv]

        if conjunto_dados:
            return pandas.concat(conjunto_dados, ignore_index=False)
        else:
            print(f"Não foi encontrado nenhum arquivo csv em {caminho_raiz.value}")