"""
Dada uma lista encadeada com as operações prepend(value), que insere um elemento no início da lista; append(value),
que insere um elemento no final da lista; removeFirst() -> value, que remove e retorna o elemento no início da lista;
removeLast() -> value, que remove e retorna o elemento no final da lista,
 implemente uma classe Pilha, que possui o comportamento de uma estrutura LIFO (Last In, First Out),
 e que possua os métodos push(value), para inserção, pop() -> value, para exclusão, e peek() -> value, para consultar,
 sem remover, o próximo elemento.
"""


class Stack:
    def __init__(self):
        self.__stack = []

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.__stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.__stack[-1]
