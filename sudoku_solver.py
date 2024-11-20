from collections.abc import Callable
import math
import copy
from typing import Tuple
type IntegerMatrix = list[list[int]]


def get_possibilities(problem: IntegerMatrix, i: int, j: int) -> set[int]:
    """
    Returns all possible plays on the current square in the sudoku matrix
    """
    possibilities_set: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for k in range(len(problem)):
        if k != j:
            possibilities_set.discard(problem[i][k])
        if k != i:
            possibilities_set.discard(problem[k][j])
    n = round(math.sqrt(len(problem)))
    super_row = (i // n) * n
    super_column = (j // n) * n
    for k_1 in range(super_row, super_row + n):
        for k_2 in range(super_column, super_column + n):
            possibilities_set.discard(problem[k_1][k_2])
    return possibilities_set


def find_minimum_possibility_i_j(problem: IntegerMatrix) -> Tuple[Tuple[int, int], set[int]]:
    """
    Returns the entry in the sudoku problem matrix with the least possibilities along with its possibilities
    """
    minimum = 0
    minimum_i_j = (0, 0)
    possibilities_minimum = set()
    for i in range(len(problem)):
        for j in range(len(problem)):
            if problem[i][j] != 0:
                continue
            if minimum == 0:
                minimum_i_j = (i, j)
                possibilities_minimum = get_possibilities(problem, i, j)
                minimum = len(possibilities_minimum)
            elif minimum > len(get_possibilities(problem, i, j)):
                minimum_i_j = (i, j)
                possibilities_minimum = get_possibilities(problem, i, j)
                minimum = len(get_possibilities(problem, i, j))
    return minimum_i_j, possibilities_minimum


def is_valid_solution(problem: IntegerMatrix) -> bool:
    """
    Checks if the constructed solution is a valid solution by checking if there are any 0 entries
    (by construction the rules of sudoku are not violated so we do not check for those)
    """
    # by construction no constraints are broken
    # but if there exists a 0 then the problem
    # is unsolved
    for i in range(len(problem)):
        for j in range(len(problem)):
            if problem[i][j] == 0:
                return False
    return True


def backtrack_on_problem(solving_function: Callable, problem: IntegerMatrix, minimums: set[int], i: int, j: int) -> IntegerMatrix:
    result = solving_function(problem)
    # if result is empty -> backtrack
    if result == []:
        problem_copy = copy.deepcopy(problem)
        if len(minimums) > 0:
            problem_copy[i][j] = minimums.pop()
            return backtrack_on_problem(solving_function, problem_copy, minimums, i, j)
    return result


def solve_sudoku_implementation_heuristic(problem: IntegerMatrix) -> IntegerMatrix:
    """
    Solves a given sudoku matrix, only solves problems with a distinct solution
    Uses recursion (backtracking) to solve sudoku problems under uncertainty, always provides
    a solution (provided one exists).
    Has an added heuristic which picks the moves with the lowest uncertainty (lowest possible moves)
    """
    # problem is a non-square matrix -> not a sudoku problem
    if (len(problem) != len(problem[0]) or len(problem) != len(problem[0]) or len(problem) ** 2 != len(problem)*len(problem[0])):
        raise SudokuException()
    minimum_possibility_entry, possibilities_minimum = find_minimum_possibility_i_j(
        problem)
    # we are done
    if len(possibilities_minimum) == 0:
        # backtrack case - no solution ... yet
        if not is_valid_solution(problem):
            return []
        # base case - solution found
        return problem
    # assume that a random one of these is the solution
    problem_copy = copy.deepcopy(problem)
    problem_copy[minimum_possibility_entry[0]
                 ][minimum_possibility_entry[1]] = possibilities_minimum.pop()
    return backtrack_on_problem(solve_sudoku_implementation_heuristic,
                                problem_copy, possibilities_minimum, *minimum_possibility_entry)


def get_first_possibility(problem: IntegerMatrix) -> Tuple[Tuple[int, int], set[int]]:
    n = len(problem)
    for i in range(n):
        for j in range(n):
            if (problem[i][j] != 0):
                continue
            possibilities_i_j = get_possibilities(problem, i, j)
            return (i, j), possibilities_i_j
    return (0, 0), set()


# implement one without hte heuristic and compare performance times???
def solve_sudoku_implementation_normal(problem: IntegerMatrix) -> IntegerMatrix:
    """
    Solves a given sudoku matrix, only solves problems with a distinct solution
    Uses recursion (backtracking) to solve sudoku problems under uncertainty, always provides
    a solution (provided one exists).
    Has an added heuristic which picks the moves with the lowest uncertainty (lowest possible moves)
    """

    # problem is a non-square matrix -> not a sudoku problem
    if (len(problem) != len(problem[0]) or len(problem) != len(problem[0]) or len(problem) ** 2 != len(problem)*len(problem[0])):
        raise SudokuException()
    possibility_entry, possibilities = get_first_possibility(problem)
    # we are done
    if len(possibilities) == 0:
        # backtrack if not valid solution
        if not is_valid_solution(problem):
            return []
        # base case - solution found
        return problem
    # assume that a random one of these is the solution
    problem_copy = copy.deepcopy(problem)
    problem_copy[possibility_entry[0]
                 ][possibility_entry[1]] = possibilities.pop()
    return backtrack_on_problem(solve_sudoku_implementation_normal,
                                problem_copy, possibilities, *possibility_entry)


class SudokuException(Exception):
    """
    Custom exception which terminates program if invalid problem is given
    """

    def __init__(self):
        super()
