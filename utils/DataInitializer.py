import random


class DataInitializer:

    @staticmethod
    def iniciar_vetor_desordenado(tamanho):
        return [random.randint(0, tamanho-1) for i in range(tamanho)]

    @staticmethod
    def iniciar_vetor_ordenado(tamanho):
        return [i for i in range(tamanho)]

    @staticmethod
    def gerar_elemento_de_busca(valor_maximo):
        return random.randint(0, valor_maximo)

