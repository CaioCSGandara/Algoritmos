from time import time

from utils.CalculadoraDeTempo import CalculadoraDeTempo
from utils.DataInitializer import DataInitializer
from utils.LeitorDescricao import LeitorDescricao


class BuscaBinaria:

    def __init__(self):
        self.vetor = []
        self.elemento_para_busca = None
        self.tempo_execucao_ms = 0
        self.qtd_pesquisas = 0


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
    buscador = BuscaBinaria()
    buscador.vetor = DataInitializer.iniciar_vetor_ordenado(50000)
    buscador.elemento_para_busca = DataInitializer.gerar_elemento_de_busca(50000)
    elem = buscador.busca_binaria()
    print("Elemento buscado:", buscador.elemento_para_busca)
    print("Tempo de execução:", buscador.tempo_execucao_ms, "ms")
    print("Quantidade de pesquisas realizadas:", buscador.qtd_pesquisas)
