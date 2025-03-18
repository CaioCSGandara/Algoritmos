# exercicios página 77 "Entendendo Algoritmos"

class Recursao:

    @staticmethod
    def soma_vetor(soma, indice, vetor):
        if len(vetor)==indice:
            return soma
        else:
            return Recursao.soma_vetor(soma+vetor[indice], indice+1, vetor)

    @staticmethod
    def conta_numero_itens_lista(qtd, vetor):
         if len(vetor) == qtd:
            return qtd
         else:
            return Recursao.conta_numero_itens_lista(qtd+1, vetor)




if __name__ == "__main__":
    vetor = [1, 2, 3 , 4, 5]
    qtd = Recursao.conta_numero_itens_lista(0, vetor)
    print("qtd itens na lista:",qtd)

    soma = Recursao.soma_vetor(0, 0, vetor)
    print("soma dos numeros no vetor: ", soma)





