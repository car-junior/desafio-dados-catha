from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.formata_dados import FormataDados
from scripts.utils.manipula_arquivo import AnaliseCorrelacaoArquivo, AnaliseCorrelacaoDiretorio
from scripts.utils.manipula_arquivo import DiretorioArquivoEntrada
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.monta_dados import MontaDados

# Calcula media de climas 2013 a 2015 e gera csv
dados_2013_2015 = MontaDados.via_arquivos_csv_clima(diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2013_2015)
FormataDados.renomear_colunas_dados_2010_2018(dados_2013_2015)
FormataDados.substituir_valores(dados_2013_2015)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2013_2015),
    AnaliseCorrelacaoArquivo.MEDIA_CLIMAS_2013_2015_CSV,
    AnaliseCorrelacaoDiretorio.MEDIAS_POR_PERIODO
)

del dados_2013_2015

# Calcula media de climas 2016 a 2018 e gera csv
dados_2016_2018 = MontaDados.via_arquivos_csv_clima(diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2016_2018)
FormataDados.renomear_colunas_dados_2010_2018(dados_2016_2018)
FormataDados.substituir_valores(dados_2016_2018)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_2016_2018),
    AnaliseCorrelacaoArquivo.MEDIA_CLIMAS_2016_2018_CSV,
    AnaliseCorrelacaoDiretorio.MEDIAS_POR_PERIODO
)

del dados_2016_2018

# Calcula media de climas 2019 a 2021 e gera csv
dados_climas_2019_2021 = MontaDados.via_arquivos_csv_clima(
    diretorio=DiretorioArquivoEntrada.REGISTRO_CLIMATICOS_2019_2021)
FormataDados.renomear_colunas_dados_2019_2021(dados_climas_2019_2021)
FormataDados.definir_coluna_para_data(dados_climas_2019_2021)
FormataDados.substituir_valores(dados_climas_2019_2021)

GeradorArquivo.gerar_csv_periodo(
    AnalisaDados.calcular_media(dados_climas_2019_2021),
    AnaliseCorrelacaoArquivo.MEDIA_CLIMAS_2019_2021_CSV,
    AnaliseCorrelacaoDiretorio.MEDIAS_POR_PERIODO
)

del dados_climas_2019_2021
