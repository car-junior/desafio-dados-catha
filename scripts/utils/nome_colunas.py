from enum import Enum


class RegistroClimatico(Enum):
    COLUNA_DATA = "DATA"
    COLUNA_HORA = "HORA"
    COLUNA_ESTADO = "ESTADO"

    @staticmethod
    def agrupa_por():
        return [RegistroClimatico.COLUNA_DATA.value, RegistroClimatico.COLUNA_ESTADO.value]


class RegistroAcidente(Enum):
    # COLUNA_OCORRENCIA_HORA = "ocorrencia_hora" #TODO: Usar coluna hora como groupby tambem ? para ser mais preciso
    COLUNA_OCORRENCIA_CLASSIFICACAO = "ocorrencia_classificacao"
    COLUNA_ESTADO = "ocorrencia_uf"
    COLUNA_OCORRENCIA_DIA = "ocorrencia_dia"
    COLUNA_INVESTIGACAO_AERONAVE_LIBERADA = "investigacao_aeronave_liberada"
    COLUNA_INVESTIGACAO_STATUS = "investigacao_status"
    COLUNA_TOTAL_AERONAVES_ENVOLVIDAS = "total_aeronaves_envolvidas"
    COLUNA_OCORRENCIA_SAIDA_PISTA = "ocorrencia_saida_pista"
    COLUNA_OCORRENCIA_TIPO = "ocorrencia_tipo"
    COLUNA_AERONAVE_MATRICULA = "aeronave_matricula"
    COLUNA_AERONAVE_TIPO_VEICULO = "aeronave_tipo_veiculo"
    COLUNA_AERONAVE_FABRICANTE = "aeronave_fabricante"
    COLUNA_AERONAVE_MODELO = "aeronave_modelo"
    COLUNA_AERONAVE_TIPO_ICAO = "aeronave_tipo_icao"
    COLUNA_AERONAVE_TIPO_MOTOR = "aeronave_motor_tipo"
    COLUNA_AERONAVE_MOTOR_QUANTIDADE = "aeronave_motor_quantidade"
    COLUNA_AERONAVE_PMD = "aeronave_pmd"
    COLUNA_AERONAVE_PMD_CATEGORIA = "aeronave_pmd_categoria"
    COLUNA_AERONAVE_MOTOR_ASSENTOS = "aeronave_assentos"
    COLUNA_AERONAVE_ANO_FABRICACAO = "aeronave_ano_fabricacao"
    COLUNA_AERONAVE_REGISTRO_CATEGORIA = "aeronave_registro_categoria"
    COLUNA_AERONAVE_VOO_ORIGEM = "aeronave_voo_origem"
    COLUNA_AERONAVE_VOO_DESTINO = "aeronave_voo_destino"
    COLUNA_AERONAVE_FASE_OPERACAO = "aeronave_fase_operacao"
    COLUNA_AERONAVE_TIPO_OPERACAO = "aeronave_tipo_operacao"
    COLUNA_AERONAVE_NIVEL_DANO = "aeronave_nivel_dano"
    COLUNA_AERONAVE_FATALIDADES_TOTAL = "aeronave_fatalidades_total"
    COLUNA_FATOR_NOME = "fator_nome"
    COLUNA_FATOR_ASPECTO = "fator_aspecto"
    COLUNA_FATOR_CONDICIONANTE = "fator_condicionante"
    COLUNA_FATOR_AREA = "fator_area"

    @staticmethod
    def colunas_para_ler():
        return [coluna.value for coluna in RegistroAcidente]

    @staticmethod
    def obter_duplicadas():
        return [
            RegistroAcidente.COLUNA_ESTADO.value,
            RegistroAcidente.COLUNA_OCORRENCIA_DIA.value,
            RegistroAcidente.COLUNA_AERONAVE_MATRICULA.value,
            RegistroAcidente.COLUNA_OCORRENCIA_CLASSIFICACAO.value
            #     Adicionar hora ?
        ]

    @staticmethod
    def agrupa_por():
        return [
            RegistroAcidente.COLUNA_ESTADO.value,
            RegistroAcidente.COLUNA_OCORRENCIA_DIA.value,
            RegistroAcidente.COLUNA_OCORRENCIA_CLASSIFICACAO.value
            #     Adicionar hora ?
        ]
