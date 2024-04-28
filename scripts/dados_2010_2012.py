from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo
from scripts.utils.manipula_arquivo import DiretorioLerArquivo
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import TipoArquivoPeriodo
from scripts.utils.monta_dados import MontaDados

dados_2010_2012 = MontaDados.via_arquivos_csv(caminho_raiz=DiretorioLerArquivo.REGISTRO_CLIMATICOS_2010_2012)
FormataDados.renomear_colunas_dados_2010_2018(dados_2010_2012)
FormataDados.definir_data_para_ano_mes(dados_2010_2012)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2010_2012),
    TipoArquivoPeriodo.DADOS_2010_2012_CSV,
    DiretorioArquivoPeriodo.MEDIA
)

del dados_2010_2012
# AnalisaDados.calcular_desvio_padrao(dados_2010_2014)
# AnalisaDados.calcular_mediana(dados_2010_2014)

# media_registro_climatico_2010_2018.to_csv('dados_por_ano/registros_climaticos_desvio_padrao_2010_2018.csv', index=False, decimal=',', sep=';')