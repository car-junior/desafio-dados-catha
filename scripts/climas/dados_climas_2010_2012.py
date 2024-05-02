from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo
from scripts.utils.manipula_arquivo import DiretorioLerArquivo
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import TipoArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_2010_2012 = MontaDados.via_arquivos_csv_clima(caminho_raiz="C:\\Users\\carlo\\Downloads\\desafio-dados-catha\\arquivos_entrada\\registros_climaticos\\2010_2012")
FormataDados.renomear_colunas_dados_2010_2018(dados_2010_2012)
FormataDados.definir_data_para_ano_mes(dados_2010_2012)
FormataDados.substituir_valores(dados_2010_2012)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2010_2012),
    TipoArquivoPeriodo.DADOS_2010_2012_CSV,
    DiretorioArquivoPeriodo.MEDIA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_desvio_padrao(dados_2010_2012),
    TipoArquivoPeriodo.DADOS_2010_2012_CSV,
    DiretorioArquivoPeriodo.DESVIO_PADRAO
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_mediana(dados_2010_2012),
    TipoArquivoPeriodo.DADOS_2010_2012_CSV,
    DiretorioArquivoPeriodo.MEDIANA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_variancia(dados_2010_2012),
    TipoArquivoPeriodo.DADOS_2010_2012_CSV,
    DiretorioArquivoPeriodo.VARIANCIA
)

del dados_2010_2012
