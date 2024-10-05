from file_reader import read_file
from sudoku_solver import solve_sudoku_problem_implementation_one, solve_sudoku_problem_implementation_two
import sys


def main():
    sys.setrecursionlimit(1000)
    files = sys.argv[1:]
    for file in files:
        problem = read_file(file)
        print("original problem")
        for line in problem:
            print(line)
        soln = solve_sudoku_problem_implementation_two(problem)
        print("solution")
        for line in soln:
            print(line)


if __name__ == "__main__":
    main()
