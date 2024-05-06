## Desafio PUC GO 2024 - Análise de Dados Climáticos e Acidentes

Este projeto tem como objetivo explorar a possível relação entre dados climáticos e ocorrências de acidentes, utilizando técnicas de análise de dados e ciência de dados. O foco principal é determinar se existem padrões ou correlações entre certas condições climáticas e a incidência de acidentes.

### Configuração do Projeto

Para executar o projeto é necessário baixar uma pasta compactada e extrair a mesma para o diretorio raiz do projeto, siga os passos abaixo:
- Baixe o arquivo compactado em: [https://drive.google.com/file/d/1G6rfYh3fcwJ_7VL3mJfpAaumKx_WJZE5/view?usp=sharing](https://drive.google.com/file/d/1G6rfYh3fcwJ_7VL3mJfpAaumKx_WJZE5/view?usp=sharing)
- Extraia o arquivo no diretorio raiz do projeto, a pasta arquivos_entrada tem que ficar no mesmo nivel que scripts
- Verifique se dentro da pasta arquivos_entrada contem duas subpastas: `registros_acidentes` e `registros_climaticos`

Feito os passos anteriores para executar o projeto siga as instruções mostradas em `Estrutura do Projeto`

### Estrutura do Projeto

O projeto está dividido em três pacotes/módulos:
* scripts/analise_estatistica
* scripts/analise_correlacao

####  scripts/analise_estatistica:
Neste módulo é feito os seguintes calculos estátisticos media, mediana, variância e desvio padrão para os dados climáticos, fizemos isso agrupando por Ano, Mês e Estado.
No final geramos um csv com essas estatisticas para os climas de 2010 a 2021.

Como executar ?
- Acesse o arquivo main em `scripts/analise_estatistica`, execute o mesmo após finalizar execução será gerado um arquivo csv `arquivos/analise_estatistica_climas_2010_2021.csv` que contem media, mediana, variância e desvio padrão dos registros climaticos