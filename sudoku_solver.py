import math
import copy
type IntegerMatrix = list[list[int]]


def possibilities(P: IntegerMatrix, i: int, j: int) -> set[int]:
    possibilities_set: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for k in range(len(P)):
        if k != j:
            possibilities_set.discard(P[i][k])
        if k != i:
            possibilities_set.discard(P[k][j])
    n = round(math.sqrt(len(P)))
    super_row = (i // n) * n
    super_column = (j // n) * n
    for k_1 in range(super_row, super_row + n):
        for k_2 in range(super_column, super_column + n):
            possibilities_set.discard(P[k_1][k_2])
    return possibilities_set


def find_minimum_possibility_i_j(P):
    minimum = 0
    minimum_i_j = (0, 0)
    possibilities_minimum = set()
    for i in range(len(P)):
        for j in range(len(P)):
            if P[i][j] != 0:
                continue
            if minimum == 0:
                minimum_i_j = (i, j)
                possibilities_minimum = possibilities(P, i, j)
                minimum = len(possibilities_minimum)
            elif minimum > len(possibilities(P, i, j)):
                minimum_i_j = (i, j)
                possibilities_minimum = possibilities(P, i, j)
                minimum = len(possibilities(P, i, j))
    return minimum_i_j, possibilities_minimum


def valid_solution(P):
    # by construction no cosntraints are broken
    # but if there exists a 0 then the problem
    # is unsolved
    for i in range(len(P)):
        for j in range(len(P)):
            if P[i][j] == 0:
                return False
    return True


def recurse(f, P, minimums, i, j):
    result = f(P)
    # if result is empty -> backtrack
    if result == []:
        P_copy = copy.deepcopy(P)
        if len(minimums) > 0:
            P_copy[i][j] = minimums.pop()
            return recurse(f, P_copy, minimums, i, j)
    return result


def solve_sudoku_implementation_heuristic(P: IntegerMatrix):
    """
    Solves a given sudoku matrix, only solves problems with a distinct solution
    Uses recursion (backtracking) to solve sudoku problems under uncertainty, always provides 
    a solution (provided one exists).
    Has an added heuristic which picks the moves with the lowest uncertainty (lowest possible moves)
    """
    if (len(P) != len(P[0])):
        raise SudokuException()
    minimum_possibility_entry, possibilities_minimum = find_minimum_possibility_i_j(
        P)
    # we are done
    if len(possibilities_minimum) == 0:
        # backtrack case - no solution ... yet
        if not valid_solution(P):
            return []
        # base case - solution found
        return P
    # assume that a random one of these is the solution
    P_copy = copy.deepcopy(P)
    P_copy[minimum_possibility_entry[0]
           ][minimum_possibility_entry[1]] = possibilities_minimum.pop()
    return recurse(solve_sudoku_implementation_heuristic,
                   P_copy, possibilities_minimum, *minimum_possibility_entry)


def get_first_possibility(P):
    n = len(P)
    for i in range(n):
        for j in range(n):
            if (P[i][j] != 0):
                continue
            possibilities_i_j = possibilities(P, i, j)
            return (i, j), possibilities_i_j
    return (0, 0), set()


# implement one without hte heuristic and compare performance times???
def solve_sudoku_implementation_normal(P: IntegerMatrix):
    """
    Solves a given sudoku matrix, only solves problems with a distinct solution
    Uses recursion (backtracking) to solve sudoku problems under uncertainty, always provides 
    a solution (provided one exists).
    Has an added heuristic which picks the moves with the lowest uncertainty (lowest possible moves)
    """
    if (len(P) != len(P[0])):
        raise SudokuException()
    possibility_entry, possibilities = get_first_possibility(P)
    # we are done
    if len(possibilities) == 0:
        if not valid_solution(P):
            return []
        # display the sudoku grid
            # base case - solution found
        return P
    # assume that a random one of these is the solution
    P_copy = copy.deepcopy(P)
    P_copy[possibility_entry[0]][possibility_entry[1]] = possibilities.pop()
    return recurse(solve_sudoku_implementation_normal,
                   P_copy, possibilities, *possibility_entry)


class SudokuException(Exception):
    def __init__(self):
        super()
