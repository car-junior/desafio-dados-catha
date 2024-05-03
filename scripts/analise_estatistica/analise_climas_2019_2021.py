from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import ClimaDiretorioPeriodo, DiretorioArquivoEntrada
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import ClimaArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_2019_2021 = MontaDados.via_arquivos_csv_clima(caminho_raiz=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2019_2021)
FormataDados.renomear_colunas_dados_2019_2021(dados_2019_2021)
FormataDados.definir_data_para_ano_mes(dados_2019_2021)
FormataDados.substituir_valores(dados_2019_2021)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2019_2021),
    ClimaArquivoPeriodo.CLIMAS_2019_2021_CSV,
    ClimaDiretorioPeriodo.MEDIA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_desvio_padrao(dados_2019_2021),
    ClimaArquivoPeriodo.CLIMAS_2019_2021_CSV,
    ClimaDiretorioPeriodo.DESVIO_PADRAO
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_mediana(dados_2019_2021),
    ClimaArquivoPeriodo.CLIMAS_2019_2021_CSV,
    ClimaDiretorioPeriodo.MEDIANA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_variancia(dados_2019_2021),
    ClimaArquivoPeriodo.CLIMAS_2019_2021_CSV,
    ClimaDiretorioPeriodo.VARIANCIA
)

del dados_2019_2021
