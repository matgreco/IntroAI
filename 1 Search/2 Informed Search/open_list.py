import heapq

class OpenList:
    # Inicia una lista vacia
    def __init__(self):
        self.items = []

    # La cantidad de elementos en el heap
    @staticmethod
    def size(self):
        return len(self.items)

    # Retorna el mejor elemento del heap
    def top(self):
        if self.size == 0:
            return None
        else:
            return self.items[0]
    # Retorna el mejor elemento del heap y lo elimina
    def extract(self):
        if len(self.items):
            return heapq.heappop(self.items)
        else : 
            None

    # Inserta un elemento en el heap
    def insert(self, element):
        heapq.heappush(self.items, element)

    # Verifica si esta vacia
    def is_empty(self):
        return self.size == 0
