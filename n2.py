class Pilha:        # não vou deixar os atributos privados

    def __init__(self):
        self.pilha = []

    def append(self, item):
        self.pilha.insert(0, item)
    
    def is_empty(self):
        return len(self.pilha) == 0

    def size(self):
        return len(self.pilha)
    
    def pop(self):
        if not self.is_empty():
            return self.pilha.pop(0)  # Remove o item da "primeira posição"
        else:
            return "A pilha está vazia!"
    
    def peek(self):
        if not self.is_empty():
            return self.pilha[0]  # O topo está na "primeira posição"
        else:
            return "A pilha está vazia!"
    
    def get_pilha(self):
        return self.pilha



minha_pilha = Pilha()       # instanciando objeto

minha_pilha.append('copo')
minha_pilha.append('garfo')
minha_pilha.append('faca')
minha_pilha.append('prato')

print(minha_pilha.size())       # tamanho da lista = 4
print(minha_pilha.peek())       # no topo sempre está o ultimo adicionado
print(minha_pilha.pop())        # do topo sempre é o que será apagado
print(minha_pilha.is_empty())   # testo pra ver se está vazia. Return = False
print(minha_pilha.peek())       # olho o topo de novo e agora é a faca
print(minha_pilha.pop())        # apaga a faca e retorna ela
print(minha_pilha.pop())        # apaga o garfo e retorna ele
print(minha_pilha.pop())        # apaga o copo e apaga ele
print(minha_pilha.is_empty())   # testo pra ver se está vazia. Return = True
print(minha_pilha.get_pilha())  # retorno a pilha vazia []


