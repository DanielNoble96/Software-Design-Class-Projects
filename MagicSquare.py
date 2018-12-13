'''
File: MagicSquare.py

Description: Programming Assignment 1: This program prompts the user for an odd number n greater than 1
             and creates an n x n magic square, which it then outputs to the screen.

Student's Name: Daniel A. Noble Hernandez

Student's UT EID: dan833

Course Name: CS 313E

Unique Number: 51345

Date Created: 5th September 2018

Date Last Modified: 7th September 2018
'''


# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
    # Create an n x n list of zeros
    magic_square = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        magic_square.append(temp)

    # Find starting location for the magic square      
    row = n - 1
    column = n // 2

    # Populate each cell of the magic square
    for counter in range(1, n**2):
        # Update value of current magic square cell
        magic_square[row][column] = counter

        # Update the current row, column and counter
        row += 1
        column += 1
        counter += 1

        # Check for each of the five possible cases that emerge
        # when moving to the next cell and respond appropriately
        if (row >= n) and (column < n):
            row = 0
            magic_square[row][column] = counter
        elif (row < n) and (column >= n):
            column = 0
            magic_square[row][column] = counter
        elif (row >= n) and (column >= n):
            row -= 2
            column -= 1
            magic_square[row][column] = counter
        elif magic_square[row][column] > 0:
            row -= 2
            column -= 1
            magic_square[row][column] = counter
        else:
            magic_square[row][column] = counter

    return magic_square

    
# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    # Get number of rows (n)
    num_rows = len(magic_square)
    n = str(num_rows)
    print('\nHere is a ' + n + ' x ' + n + ' magic square:\n')

    # Print right-justified magic square
    for i in range(num_rows):
        for j in range(num_rows):
            print(str(magic_square[i][j]).rjust(4), end= '')
        print('\n')

        
# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    n = len(magic_square)
    square_sum = n * (n**2 + 1) / 2

    # Sum each of the rows and check against square_sum
    true_row_num = 0
    for i in range(n):
        row_sum = sum(magic_square[i])    
        if row_sum == square_sum:
            true_row_num += 1

    # Sum each of the columns and check against square_sum
    true_col_num = 0   
    col_sum = 0
    for i in range(n):
        for j in range(n):
            col_sum = col_sum + magic_square[j][i]
        if col_sum == square_sum:
            true_col_num += 1
        col_sum = 0
        
    # Sum the two main diagonals
    diag1_sum = 0;
    diag2_sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                diag1_sum = diag1_sum + magic_square[i][j]
            if i + j == n - 1:
                diag2_sum = diag2_sum + magic_square[i][j]

    # Check whether or not it is a magic square
    if (true_row_num == n and true_col_num == n and
            diag1_sum == square_sum and diag2_sum == square_sum):
        print('This is a magic square and the canonical sum is', int(square_sum))
    else:
        print('This is not a magic square')
   
   
def main():
  # Prompt the user to enter an odd number 1 or greater
    print('Please enter an odd number 1 or greater:', end = ' ')
    n = int(input())
    
  # Check the user input
    is_odd = n % 2
    while (is_odd == 0) or (n < 1):
        print('Number is not odd and greater than 1.')
        print('Please enter an odd number 1 or greater:', end= ' ')
        n = int(input())
        is_odd = n % 2
        
  # Create the magic square
    magic_square = make_square(n)
    
  # Print the magic square
    print_square(magic_square)
    
  # Verify that it is a magic square
    check_square(magic_square)
    
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
