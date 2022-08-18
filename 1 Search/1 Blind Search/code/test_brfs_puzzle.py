from puzzle import Puzzle
from BrFS import BrFS
from os.path import join

def load_problems(problems):  ## carga los problemas en memoria
    puzzles = list()
    with open('problems_r8.txt') as f:
        for line in f:
            puzzle = line.rstrip().split(' ', 1)[1]
            problems.append(Puzzle([int(x) for x in puzzle.split(' ')]))
            puzzles.append(puzzle)
    


show_solutions = False        # mostramos las soluciones?

problems = []
load_problems(problems)

total_time = 0
total_cost = 0
total_expansions = 0
num_problems = 3 # len(problems) # cambiar si quieres ejecutar sobre todos los problemas


print('prob\texp\tgenerated\t|sol|\ttiempo\n')

for prob in range(0, num_problems):
    init = problems[prob]
    s = BrFS(init) # agregar un tercer parámetro una vez que lo hayas transformado en Weighted A*
    result = s.search()
    print('%5d%10d%10d%10d%10.2f' % (prob+1, s.expansions, len(s.generated), result.g, s.end_time-s.start_time ))
    total_time += s.end_time - s.start_time
    total_cost += result.g
    total_expansions += s.expansions

    if show_solutions:
        print(result.trace())

    
print('Tiempo total:        %.2f'%(total_time))
print('Expansiones totales: %d'%(total_expansions))
print('Costo total:         %d'%(total_cost))
