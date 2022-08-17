class Node:
    def __init__(self, search_state, parent=None, action=''):
        self.state = search_state
        self.parent = parent      # Es el estado padre.
        if parent:                # compatibilidad con DFS/BrFS
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.action = action    # es el nombre de la accion
        self.key = -1           # el el criterio de ordenamiento del nodo
        self.g = 0              # corresponde al costo del camino
        self.heap_index = 0     
        
    def __repr__(self):
        return self.state.__repr__()

    def __gt__(self, other):
        if self.key > other.key:
            return True
        else :
            return False

    def __lt__(self, other):
        if self.key < other.key:
            return True
        else :
            return False

    def trace(self):
        s = ''
        if self.parent:
            s = self.parent.trace()
            s += '-' + self.action + '->'
        s += str(self.state)
        return s
