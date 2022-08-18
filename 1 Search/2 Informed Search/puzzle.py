import sys
import copy
import numpy as np


class Puzzle:
    goal8 = list(range(9))
    def __init__(self, board=None, blank=-1):
        if not board:
            self.x = 3
            self.size = 9
            self.board = [i for i in range(0, self.size)]
            self.blank = 0
        else:
            self.board = board
            if len(self.board) == 9:
                self.x = 3
                self.size = 9
            else:
                print('puzzle size not supported')
                sys.exit(1)
            if blank == -1:
                self.blank = board.index(0)


    def __hash__(self):
        return hash(tuple(self.board))

    def __eq__(self, other):
        return self.board == other.board

    def __repr__(self):
        def tostr(d):
            if d > 0:
                return "%2d" % (d)
            else:
                return "  "
        s = '\n'
        for i in range(0, self.x):
            s += "|"
            s += "|".join([tostr(d) for d in self.board[i*self.x:i*self.x+self.x]])
            s += "|\n"
        return s

    def successors(self):
        '''
            Crea una lista de tuplas de la forma (estado, accion, costo)
            donde estado es el estado sucesor de self que se genera al ejecutar
            accion (un string) y costo (un numero real) es el costo de accion
        '''
        def create_child(newblank):
            child = copy.deepcopy(self)
            child.blank = newblank
            child.board[child.blank] = 0
            child.board[self.blank] = self.board[newblank]
            return child

        succ = []
        if self.blank > self.x - 1:
            c = create_child(self.blank-self.x)
            succ.append((c, 'down', 1))
        if self.blank % self.x > 0:
            c = create_child(self.blank-1)
            succ.append((c, 'right', 1))
        if self.blank % self.x < self.x - 1:
            c = create_child(self.blank+1)
            succ.append((c, 'left', 1))
        if self.blank < self.size - self.x:
            c = create_child(self.blank+self.x)
            succ.append((c, 'up', 1))
        return succ

    def is_goal(self):
        return Puzzle.goal8 == self.board 
