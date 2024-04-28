from scripts.utils.manipula_arquivo import DiretorioArquivoPeriodo
from scripts.utils.manipula_arquivo import DiretorioGeraArquivo
from scripts.utils.manipula_arquivo import GeradorArquivo
from scripts.utils.manipula_arquivo import TipoArquivo
from scripts.utils.monta_dados import MontaDados

print("Criando dados do registros climáticos a partir de 2010 a 2012")
exec(open('dados_2010_2012.py').read())

print("Criando dados do registros climáticos a partir de 2013 a 2015")
exec(open('dados_2013_2015.py').read())

print("Criando dados do registros climáticos a partir de 2016 a 2018")
exec(open('dados_2016_2018.py').read())

print("Criando dados do registros climáticos a partir de 2019 a 2021")
exec(open('dados_2019_2021.py').read())

media_dados_2010_2021 = MontaDados.via_arquivos_csv_gerados(caminho_raiz=DiretorioArquivoPeriodo.MEDIA,
                                                            pular_linhas=0)
GeradorArquivo.gerar_csv(media_dados_2010_2021,
                         TipoArquivo.DADOS_MEDIA_2010_2021_CSV,
                         DiretorioGeraArquivo.DADOS_COMPLETOS)
