#  File: Queens.py

#  Description: This program prompts the user to enter the desired size of a board and
#               prints out every possible solution to the N queens problem using that value

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 28th October 2018

#  Date Last Modified: 29th October 2018
import copy

# define a global variable to hold all possible solutions
solutions = []

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print all of the solutions
  def print_solutions(self, solutions):
    for sol in solutions:
      for i in range(self.n):
        for j in range(self.n):
          print(sol[i][j], end= ' ')
        print()
      print()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    if (col == self.n):
      return
    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          # when end of the board is reached, return from a recursive call and find next solution
          if (col == (self.n - 1)):
              self.add_solution()
              self.board[i][col] = '*'
              return
          self.recursive_solve(col + 1)
          self.board[i][col] = '*'

  # find all solutions and print them
  def solve(self):
      self.recursive_solve(0)
      self.print_solutions(solutions)

  # save the possible solutions to the global list solutions
  def add_solution(self):
      global solutions
      # make a copy so that it is not changed
      board = copy.deepcopy(self.board)
      solutions.append(board)

def main():
  # prompt the user for the size of the board
  n = int(input("Enter the size of the board (1-8): "))
  while n not in range(1, 9):
      n = int(input("Enter the size of the board (1-8): "))

  # create a regular chess board
  game = Queens (n)

  # place the queens on the board
  game.solve()


main()
