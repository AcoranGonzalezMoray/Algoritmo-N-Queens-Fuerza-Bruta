from comb_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    Return a list of lists. For example, if num_queens = 4
    we have two solutions, and we return:
       solutions_list = [ [2, 4, 1, 3], [3, 1, 4, 2] ]
    """

    solutions_list = []
    tablero = Comb_Iterator(num_queens, num_queens).comb_generator()

    while tablero:
        for L in tablero:
            cumple_condicion = True
            if 0 in L:
                cumple_condicion = False
            for i, x in enumerate(L):
                for y in L[(i + 1):]:
                    if abs(x - y) == abs(L.index(x) - L.index(y)):
                        cumple_condicion = False
            if cumple_condicion:
                solutions_list.append(list(L))
        else:
            break

    return solutions_list
