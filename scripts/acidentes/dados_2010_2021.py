from scripts.utils.manipula_arquivo import DiretorioLerArquivo
from scripts.utils.monta_dados import MontaDados

dados_acidentes_2010_2021 = MontaDados.via_arquivo_excel_acidentes(
    caminho_raiz=DiretorioLerArquivo.REGISTRO_ACIDENTES_2010_2021
)
dados_acidentes_2010_2021.groupby([''])
print(dados_acidentes_2010_2021)
