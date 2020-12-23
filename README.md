# Sudoku-Solver

Sudoku is a logic based, combinatorial number placement puzzle.. In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

Input

0 9 0  | 0 0 0  | 0 7 0
0 7 8  | 0 1 4  | 0 5 3
0 0 0  | 0 6 0  | 0 9 0
 - - - - - - - - - - - -
0 6 0  | 0 2 0  | 0 3 0
0 5 3  | 0 0 0  | 4 6 0
0 0 0  | 0 9 0  | 0 8 0
 - - - - - - - - - - - -
0 3 0  | 0 4 0  | 0 2 0
9 2 0  | 3 7 0  | 6 4 0
0 0 0  | 0 0 0  | 0 1 0

'0' represent blank positions

Steps

1) Pass the input sudoku
2) Find the first empty space in the input sudoku. It is done with the help of find_empty function used in the code
3) After that, at the empty position numbers from 1 to 9 are inserted until a valid input is found
4) Repeat 
5) Backtrack


Output

5 9 4  | 8 3 2  | 1 7 6
6 7 8  | 9 1 4  | 2 5 3
3 1 2  | 5 6 7  | 8 9 4
 - - - - - - - - - - - -
8 6 9  | 4 2 5  | 7 3 1
2 5 3  | 7 8 1  | 4 6 9
1 4 7  | 6 9 3  | 5 8 2
 - - - - - - - - - - - -
7 3 5  | 1 4 6  | 9 2 8
9 2 1  | 3 7 8  | 6 4 5
4 8 6  | 2 5 9  | 3 1 7

