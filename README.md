# Practicing problem-solving skills on sudoku
## Algorithms:
1. Non-optimized backtracking
2. Backtracking algorithm with heuristic
 - Checks for the grid entry with the minimum possible moves to make and begins backtracking algorithm
   - Does this recursively: i.e. looks for minimum possible move entry, changes to one of possible moves, continues. If finds a 'bad' solution we backtrack to a past recursive stack frame.
