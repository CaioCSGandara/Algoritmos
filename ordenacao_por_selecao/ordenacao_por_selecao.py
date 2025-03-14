from time import time

from utils.CalculadoraDeTempo import CalculadoraDeTempo
from utils.DataInitializer import DataInitializer
from utils.LeitorDescricao import LeitorDescricao


class OrdenacaoPorSelecao:

    def __init__(self):
        self.tempo_execucao = 0


    def encontra_menor_elemento(self, vetor):
        menor = vetor[0]
        indice_menor = 0
        for i in range(len(vetor)):
                if menor > vetor[i]:
                    menor = vetor[i]
                    indice_menor = i
        return indice_menor


    def cria_vetor_ordenado(self, vetor):
        vetor_ordenado = []
        tempo_inicial = time()
        while vetor:
            menor = OrdenacaoPorSelecao.encontra_menor_elemento(self, vetor)
            vetor_ordenado.append(vetor.pop(menor))
        tempo_final = time()
        self.tempo_execucao = CalculadoraDeTempo.calcula_tempo_execucao_ms(tempo_final, tempo_inicial)

        return vetor_ordenado


if __name__ == "__main__":

    print(LeitorDescricao.ler_descricao("ordenacao_por_selecao.txt"))
    vetor_desordenado = DataInitializer.iniciar_vetor_desordenado(10000)
    print("Vetor antes da ordenação:",vetor_desordenado)
    elemento_buscado = DataInitializer.gerar_elemento_de_busca(10000)

    ordenador = OrdenacaoPorSelecao()
    vetor_ordenado = ordenador.cria_vetor_ordenado(vetor_desordenado)
    print("Vetor após a ordenação: ",vetor_ordenado)
    print("Tempo de execução:", ordenador.tempo_execucao, "ms")

