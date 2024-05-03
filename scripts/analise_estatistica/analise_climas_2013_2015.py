from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import ClimaDiretorioPeriodo
from scripts.utils.manipula_arquivo import DiretorioArquivoEntrada
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import ClimaArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_2013_2015 = MontaDados.via_arquivos_csv_clima(caminho_raiz=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2013_2015)
FormataDados.renomear_colunas_dados_2010_2018(dados_2013_2015)
FormataDados.definir_data_para_ano_mes(dados_2013_2015)
FormataDados.substituir_valores(dados_2013_2015)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2013_2015),
    ClimaArquivoPeriodo.MEDIA_2013_2015_CSV,
    ClimaDiretorioPeriodo.MEDIA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_desvio_padrao(dados_2013_2015),
    ClimaArquivoPeriodo.DESVIO_PADRAO_CLIMAS_2013_2015_CSV,
    ClimaDiretorioPeriodo.DESVIO_PADRAO
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_mediana(dados_2013_2015),
    ClimaArquivoPeriodo.MEDIANA_CLIMAS_2013_2015_CSV,
    ClimaDiretorioPeriodo.MEDIANA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_variancia(dados_2013_2015),
    ClimaArquivoPeriodo.VARIANCIA_CLIMAS_2013_2015_CSV,
    ClimaDiretorioPeriodo.VARIANCIA
)

del dados_2013_2015
