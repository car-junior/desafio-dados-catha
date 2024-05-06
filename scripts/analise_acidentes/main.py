import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from scripts.utils.manipula_arquivo import DiretorioArquivoEntrada
from scripts.utils.monta_dados import MontaDados
from scripts.utils.nome_colunas import RegistroAcidente

acidentes_2013_2022 = MontaDados.via_arquivo_excel_acidentes(
    DiretorioArquivoEntrada.REGISTRO_ACIDENTES_2013_2022, RegistroAcidente.colunas_para_ler()
)

acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value] = pd.to_datetime(
    acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value]
)

acidentes_por_mes = acidentes_2013_2022.groupby(
    acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_DIA.value].dt.to_period('M')).size()

plt.figure(figsize=(12, 6))
acidentes_por_mes.plot()
plt.title('Número de Acidentes ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Acidentes')
plt.show()

tipos_de_acidentes = acidentes_2013_2022[RegistroAcidente.COLUNA_OCORRENCIA_TIPO.value].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=tipos_de_acidentes.values, y=tipos_de_acidentes.index, palette='viridis')
plt.title('Tipos Mais Comuns de Acidentes')
plt.xlabel('Número de Acidentes')
plt.ylabel('Tipo de Acidente')
plt.show()

aeronaves_envolvidas = acidentes_2013_2022[RegistroAcidente.COLUNA_AERONAVE_TIPO_VEICULO.value].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=aeronaves_envolvidas.values, y=aeronaves_envolvidas.index, palette='viridis')
plt.title('Aeronaves Mais Envolvidas em Acidentes')
plt.xlabel('Número de Acidentes')
plt.ylabel('Tipo de Aeronave')
plt.show()

causas_frequentes = acidentes_2013_2022[RegistroAcidente.COLUNA_FATOR_NOME.value].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=causas_frequentes.values, y=causas_frequentes.index, palette='viridis')
plt.title('Causas Mais Frequentes de Acidentes')
plt.xlabel('Número de Acidentes')
plt.ylabel('Causa do Acidente')
plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=acidentes_2013_2022, x=RegistroAcidente.COLUNA_OCORRENCIA_LONGITUDE.value,
    y=RegistroAcidente.COLUNA_OCORRENCIA_LATITUDE.value, alpha=0.5
)
plt.title('Distribuição Geográfica dos Acidentes')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
