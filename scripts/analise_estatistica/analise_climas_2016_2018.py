from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import ClimaDiretorioPeriodo, DiretorioArquivoEntrada
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import ClimaArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_climas_2016_2018 = MontaDados.via_arquivos_csv_clima(
    diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2016_2018)
FormataDados.renomear_colunas_dados_2010_2018(dados_climas_2016_2018)
FormataDados.definir_data_para_ano_mes(dados_climas_2016_2018)
FormataDados.substituir_valores(dados_climas_2016_2018)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_climas_2016_2018),
    ClimaArquivoPeriodo.MEDIA_2016_2018_CSV,
    ClimaDiretorioPeriodo.MEDIA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_desvio_padrao(dados_climas_2016_2018),
    ClimaArquivoPeriodo.DESVIO_PADRAO_CLIMAS_2016_2018_CSV,
    ClimaDiretorioPeriodo.DESVIO_PADRAO
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_mediana(dados_climas_2016_2018),
    ClimaArquivoPeriodo.MEDIANA_CLIMAS_2016_2018_CSV,
    ClimaDiretorioPeriodo.MEDIANA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_variancia(dados_climas_2016_2018),
    ClimaArquivoPeriodo.VARIANCIA_CLIMAS_2016_2018_CSV,
    ClimaDiretorioPeriodo.VARIANCIA
)

del dados_climas_2016_2018
