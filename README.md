# Practicing problem-solving skills on sudoku
## Algorithms:
1. Runs under assumption that the only correct moves are the ones with one possible move
 - Obviously doesn't work for complicated problems
2. Backtracking algorithm combined with the above algorithm via heuristic
 - Checks for the grid entry with the minimum possible moves to make and begins backtracking algorithm
   - Does this recursively: i.e. looks for minimum possible move entry, changes to one of possible moves, continues. If finds a 'bad' solution we backtrack to a past recursive stack frame.
