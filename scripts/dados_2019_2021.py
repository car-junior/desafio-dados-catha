from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo
from scripts.utils.manipula_arquivo import DiretorioLerArquivo
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import TipoArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_2019_2021 = MontaDados.via_arquivos_csv(caminho_raiz=DiretorioLerArquivo.REGISTRO_CLIMATICOS_2019_2021)
FormataDados.renomear_colunas_dados_2019_2021(dados_2019_2021)
FormataDados.definir_data_para_ano_mes(dados_2019_2021)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2019_2021),
    TipoArquivoPeriodo.DADOS_2019_2021_CSV,
    DiretorioArquivoPeriodo.MEDIA
)

del dados_2019_2021
