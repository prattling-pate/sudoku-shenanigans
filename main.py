from file_reader import read_file
from sudoku_solver import solve_sudoku_implementation_heuristic, solve_sudoku_implementation_normal
from time import time
import sys


def print_solution(solution):
    for line in solution:
        print(line)


def time_function(function, *args):
    start = time()
    value = function(*args)
    print(f"Time taken: {time() - start}s")
    print_solution(value)


def main():
    files = sys.argv[1:]
    for file in files:
        problem = read_file(file)
        print("original problem")
        for line in problem:
            print(line)
        print("solution")
        print("Heuristic solution")
        time_function(solve_sudoku_implementation_heuristic, problem)
        print("non-heuristic solution")
        time_function(solve_sudoku_implementation_normal, problem)


if __name__ == "__main__":
    main()
