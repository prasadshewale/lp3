# Python3 program to solve N Queen 
# Problem using backtracking
# NQueens
def nqueen(n, constraint):
  board = []
  for i in range(n):
    board.append([0]*n) 
  board[0][constraint] = 1
  helper(board, 1, n)

# A utility function to check if a queen can
# be placed on board[row][col]

def helper(board, row, n):
  if row >= n:
    printBoard(board)
    return True
  for col in range(n):
    if isSafe(board, row, col, n):         
      board[row][col] = 1
      out = helper(board, row+1, n)
      if out:
        return True
      board[row][col] = 0
  return False

 # function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens

def printBoard(board):
  for row in board:
    print(row)

def isSafe(board, row, col, n):
   # Check this row on left side
   # return True
  for j in range(n):
    if (board[row][j] == 1):
      return False
  for i in range(n):
    if (board[i][col] == 1):
      return False
  
  i=row+1
  j=col+1
  while (i< n and j < n):
    if (board[i][j] == 1):
      return False
    i+= 1
    j+=1

  i=row-1
  j=col-1
  while (i>=0 and j >= 0):
    if (board[i][j] == 1):
      return False
    i-= 1
    j-=1

  i=row+1
  j=col-1
  while (i < n and j >= 0):
    if (board[i][j] == 1):
      return False
    i+= 1
    j-=1

  i=row-1
  j=col+1
  while (i >= 0  and j < n):
    if (board[i][j] == 1):
      return False
    i-= 1
    j+=1

  return True


n = 4  #board size
c1 = 2        # constraint-1 must be betwwen [0,n-1]

nqueen(n,c1)