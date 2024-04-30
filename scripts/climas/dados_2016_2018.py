from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo
from scripts.utils.manipula_arquivo import DiretorioLerArquivo
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import TipoArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_2016_2018 = MontaDados.via_arquivos_csv_clima(caminho_raiz=DiretorioLerArquivo.REGISTRO_CLIMATICOS_2016_2018)
FormataDados.renomear_colunas_dados_2010_2018(dados_2016_2018)
FormataDados.definir_data_para_ano_mes(dados_2016_2018)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2016_2018),
    TipoArquivoPeriodo.DADOS_2016_2018_CSV,
    DiretorioArquivoPeriodo.MEDIA
)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_desvio_padrao(dados_2016_2018),
    TipoArquivoPeriodo.DADOS_2016_2018_CSV,
    DiretorioArquivoPeriodo.DESVIO_PADRAO
)

del dados_2016_2018
