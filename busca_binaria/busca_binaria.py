import random
from time import time

from utils.CalculadoraDeTempo import CalculadoraDeTempo
from utils.LeitorDescricao import LeitorDescricao


class BuscaBinaria:

    def __init__(self):
        self.vetor = []
        self.elemento_para_busca = None
        self.tempo_execucao_ms = 0
        self.qtd_pesquisas = 0


    def gerar_vetor_ordenado(self):
        for i in range(0, 50000):
            self.vetor.append(i)


    def gerar_elemento_para_busca(self):
        self.elemento_para_busca = random.randint(1, 50000)

    def busca_binaria(self):
        inicio_vetor = 0
        final_vetor = len(self.vetor) - 1

        tempo_inicial = time()
        while inicio_vetor <= final_vetor:
            metade = int((inicio_vetor + final_vetor) / 2)
            tentaviva = self.vetor[metade]
            print(tentaviva)
            self.qtd_pesquisas += 1

            if tentaviva == self.elemento_para_busca:
                tempo_final = time()
                self.tempo_execucao_ms = CalculadoraDeTempo.calcula_tempo_execucao_ms(tempo_final, tempo_inicial)
                return self.elemento_para_busca

            elif tentaviva > self.elemento_para_busca:
                final_vetor = metade - 1


            else:
                inicio_vetor = metade + 1


        tempo_final = time()
        self_tempo_execucao_ms = CalculadoraDeTempo.calcula_tempo_execucao_ms(tempo_final, tempo_inicial)
        return None

if __name__ == "__main__":
    print(LeitorDescricao.ler_descricao("busca_binaria.txt"))
    b = BuscaBinaria()
    b.gerar_vetor_ordenado()
    b.gerar_elemento_para_busca()
    elem = b.busca_binaria()
    print("Elemento buscado:", b.elemento_para_busca)
    print("Tempo de execução:", b.tempo_execucao_ms, "ms")
    print("Quantidade de pesquisas realizadas:", b.qtd_pesquisas)
