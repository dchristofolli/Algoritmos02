"""
Lista Duplamente Encadeada

A cabeça da lista sempre aponta para o primeiro nó
O rabo da lista sempre aponta para o próximo nó

None <--- | 2 |  ---> None
None <--- | 2 | <---> | 5 |  ---> None
None <--- | 2 | <---> | 5 | <---> | 12 |  ---> None
None <--- | 2 | <---> | 5 | <---> | 12 | <---> | 20 | ---> None

"""


class No:
    def __init__(self, dado, anterior, proximo):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo


class ListaDuplamenteEncadeada:
    cabeca = None
    rabo = None

    def append(self, dado):
        """Cria um novo nó no final da lista, apontando para None (anterior e próximo)"""
        novo_no = No(dado, None, None)

        # Se a cabeça é None, a lista estará vazia
        # Tanto a cabeça quanto o rabo recebem o novo Nó
        if self.cabeca is None:
            self.cabeca = novo_no
            self.rabo = novo_no
        # Caso contrário, se já existir algum valor na lista
        else:
            # O anterior aponta para o rabo (último nó adicionado)
            novo_no.anterior = self.rabo
            # O próximo sempre aponta para None
            novo_no.proximo = None
            # O próximo do rabo sempre aponta para o novo nó
            self.rabo.proximo = novo_no
            # O rabo agora é o novo nó
            self.rabo = novo_no

    def remover(self, dado):
        # Remove um nó da lista. O nó atual é o primeiro nó da lista
        no_atual = self.cabeca

        # Vamos procurar pelo dado que queremos remover
        # Enquanto o nó atual for válido
        while no_atual is not None:
            # Verifica se é o dado que estamos procurando
            if no_atual.dado == dado:
                # Se o dado que estamos procurando está no primeiro
                # nó da lista, não temos anterior
                if no_atual.anterior is None:
                    # A cabeça aponta para o próximo nó da lista
                    self.cabeca = no_atual.proximo
                    # E o anterior do próximo nó aponta para None
                    no_atual.proximo.anterior = None
                else:
                    # Exemplo: Removendo o valor 5
                    # ... <---> | 2 | <---> | 5 | <---> | 12 | <---> ...
                    #
                    # O proximo do valor 2 passa a apontar para o 12 e
                    # o anterior do valor 12 passa a apontar para o 2
                    #                     ---------------
                    # ... <---> | 2 | <---|--- | 5 | ---|---> | 12 | <---> ...
                    no_atual.anterior.proximo = no_atual.proximo
                    no_atual.proximo.anterior = no_atual.anterior

                # Se não é o que estamos procurando, vai para o próximo
                no_atual = no_atual.proximo

    def mostrar(self):
        """ Mostra todos os itens da lista. """
        print('Lista Duplamente Encadeada: ')
        # O nó atual é o primeiro da lista
        no_atual = self.cabeca

        no = ""
        # Para cada  nó válido na lista
        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None"
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "<---> None"

            no_atual = no_atual.proximo
        print(no)
        print('=' * 80)


lista = ListaDuplamenteEncadeada()

lista.append(2)
lista.mostrar()
lista.append(5)
lista.mostrar()
lista.append(12)
lista.mostrar()
lista.append(20)
lista.mostrar()

lista.remover(12)
lista.mostrar()
lista.remover(5)
lista.mostrar()

