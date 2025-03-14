class LeitorDescricao:
    @staticmethod
    def ler_descricao(arquivo_txt):
        with open(arquivo_txt, 'r') as file:
            conteudo = file.read()
            return conteudo