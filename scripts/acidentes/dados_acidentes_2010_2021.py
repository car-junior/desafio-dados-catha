from scripts.utils.analisa_dados import AnalisaDados
from scripts.utils.manipula_arquivo import DiretorioLerArquivo
from scripts.utils.monta_dados import MontaDados
from scripts.utils.nome_colunas import RegistroAcidente

dados_acidentes_2010_2021 = MontaDados.via_arquivo_excel_acidentes(
    caminho_raiz=DiretorioLerArquivo.REGISTRO_ACIDENTES_2010_2021,
    colunas_para_ler=RegistroAcidente.colunas_para_ler()
)

AnalisaDados.calcular_quantidade_acidentes(dados_acidentes_2010_2021)

a = dados_acidentes_2010_2021
# dados_acidentes_2010_2021.groupby([''])
print(dados_acidentes_2010_2021)
