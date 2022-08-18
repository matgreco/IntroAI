from node import Node
import time
from open_list import OpenList

class BrFS:
    def __init__(self, initial_state):
        self.expansions = 0
        #self.generated = 0 # es la lista de estados generados OPEN U CLOSE
        self.initial_state = initial_state
        self.solution = None
        self.open = OpenList()
        self.generated = {}



    def search(self):
        self.start_time = time.process_time()
        
        #self.expansions = 0
        #self.solution = None
        initial_node = Node(self.initial_state)
        initial_node.g = 0
        initial_node.key = initial_node.g

        self.open.insert(initial_node)      
        self.generated[self.initial_state] = initial_node # para cada estado alguna vez generado, generated almacena el Node object que le corresponde

        while not self.open.is_empty():           # Mientras la OPEN no esté vacia  (ciclo de expansiones) 
            n = self.open.extract()               # extrae n de la open (el con menor key (en este caso profundidad))

            if n.state.is_goal():                 # Si el estado extraido es el estado objetivo (el problema resuelto)
                self.end_time = time.process_time() 
                self.solution = n                 # Define el estado extraido como solución (para reconstruirlo luego)
                return n
            succ = n.state.successors()           # Genera los sucesores
            self.expansions += 1                  # Aumenta en 1 las expansiones
            for child_state, action, cost in succ:            # Por cada uno de los estados sucesores
                child_node = self.generated.get(child_state)  # Lo agrega a generados
                path_cost = n.g + cost                        # costo del camino encontrado hasta child_state
                if child_node is None :                       # si el estado no existe en OPEN U CLOSE
                    child_node = Node(child_state, n)         # creamos el nodo de child_state
                    self.generated[child_state] = child_node  # lo agregamos a generados
                    child_node.action = action                # definimos el nombre de la acción del nodo
                    child_node.parent = n                     # definimos el padre
                    child_node.g = path_cost                  # aumentamos el costo del camino con el costo de la accion
                    child_node.key = child_node.g             # actualizamos la key (que ordenará la OPEN LIST)
                    self.open.insert(child_node)              # agrega el nodo a la OPEN 
        
        self.end_time = time.process_time()  
        print("No solution found")                # Si el ciclo de expansiones termina sin encontrar solución, no existe solución.
        return None

    
