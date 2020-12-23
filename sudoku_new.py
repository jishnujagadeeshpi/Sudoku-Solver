
# Sudoku Solver

print("\n Please enter your numbers row by row...")
print("\n Insert 0 for blank spaces...")

grid=[]

# to pass the input sudoku
for i in range(9):
    a=[]
    for j in range(9):
        a.append(int(input()))
    grid.append(a)

def solve(grid):

    find = find_empty(grid)
    if not find:
        return True
    else:
        row,col = find
    
    for i in range(1,10):
        if valid(grid,i,(row,col)):
            grid[row][col] = i

            if solve(grid):
                return True
            
            grid[row][col] = 0
    return False

def valid(grid,num,pos):

# to check rows
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1]!=i:
            return False

# to check columns
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0]!=i:
            return False

# to check the subgrid
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if grid[i][j] == num and (i,j)!=pos:
                return False

    return True

def print_grid(grid):

    for i in range(len(grid)):
        if i%3 == 0 and i!=0:
            print(" - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j%3 == 0 and j!=0:
                print(" | ", end="")
            
            if j==8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def find_empty(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i,j)

    return None

print_grid(grid)
solve(grid)
print("\n")
print_grid(grid)


'''

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

'''
