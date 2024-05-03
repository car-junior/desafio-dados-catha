from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.manipula_arquivo import DiretorioLerArquivo, GeradorArquivo, TipoArquivo, DiretorioGeraArquivo
from scripts.utils.monta_dados import MontaDados
from scripts.utils.nome_colunas import RegistroAcidente

dados_acidentes_2010_2021 = MontaDados.via_arquivo_excel_acidentes(
    caminho_raiz=DiretorioLerArquivo.REGISTRO_ACIDENTES_2010_2021,
    colunas_para_ler=RegistroAcidente.colunas_para_ler()
)

# Mudar o DiretorioGeraArquivo.DADOS_COMPLETOS nao vai mais ser dados completos
GeradorArquivo.gerar_csv(
    AnalisaDados.calcular_quantidade_acidentes(dados_acidentes_2010_2021),
    TipoArquivo.CONTAGEM_REGISTROS_ACIDENTES_2010_2021_CSV,
    DiretorioGeraArquivo.ANALISE_ESTATISTICA_ARQUIVOS_TEMP
)


del dados_acidentes_2010_2021
