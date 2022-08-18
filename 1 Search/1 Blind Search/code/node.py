class Node:
    def __init__(self, search_state, parent=None, action=''):
        self.state = search_state
        self.parent = parent      # Es el estado padre.
        if parent:                # compatibilidad con DFS/BrFS
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.action = action    # es el nombre de la accion
        #self.heap_index = 0     
        
    def __repr__(self):
        return self.state.__repr__()

    def trace(self): # reconstruye la solución
        s = ''
        if self.parent:
            s = self.parent.trace()
            s += '-' + self.action + '->'
        s += str(self.state)
        return s
