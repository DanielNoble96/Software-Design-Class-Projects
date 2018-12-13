#  File: EvenMagicSquare.py

#  Description: This program prompts a user for a desired number of magic squares
#               of size 4 x 4 and uses permutation to generate and print out that
#               number of magic squares of order 4

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 20th October 2018

#  Date Last Modified: 24th October 2018

import math

# Initialize a global variable to serve as a counter
global counter
counter = 0

# This function takes a 1D list and turns it into a 2D list
def make_two_dim (one_dim):
    # create a 2D list based on the 1D list permutation
    square = []

    # for loop uses math and variables rather than explicit values so that 2D list creation
    # is possible for any nxn square such that n is an even integer greater than 1
    factor = int(math.sqrt(len(one_dim)))
    for i in range(int(len(one_dim) / factor)):
        square.append(one_dim[(factor * i):((factor * i) + factor)])
    return square

# This function checks that the input square is a magic square by comparing
# the sums of its rows, columns and diagonals to the specified formula.
def check_square (square):
    n = len(square)
    square_sum = n * (n**2 + 1) / 2

    # Sum each of the rows and check against square_sum
    true_row_num = 0
    for i in range(n):
        row_sum = sum(square[i])
        if row_sum == square_sum:
            true_row_num += 1

    # Sum each of the columns and check against square_sum
    true_col_num = 0
    col_sum = 0
    for i in range(n):
        for j in range(n):
            col_sum = col_sum + square[j][i]
        if col_sum == square_sum:
            true_col_num += 1
        col_sum = 0

    # Sum the two main diagonals
    diag1_sum = 0;
    diag2_sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                diag1_sum = diag1_sum + square[i][j]
            if i + j == n - 1:
                diag2_sum = diag2_sum + square[i][j]

    # Check whether or not it is a magic square
    if (true_row_num == n and true_col_num == n and
            diag1_sum == square_sum and diag2_sum == square_sum):
        return True
    else:
        return False

# This function prints out the magic square in a formatted manner
def print_square ( magic_square ):
    # Get number of rows (n)
    num_rows = len(magic_square)
    n = str(num_rows)

    # Print right-justified magic square
    for i in range(num_rows):
        for j in range(num_rows):
            print(str(magic_square[i][j]).rjust(4), end= '')
        print('\n')
    print()

# This is a recursive function that creates all possible permutations of input list
def permute(a, lo, n):
    hi = len(a)
    # global variable, counter, is used to stop printing magic squares
    global counter
    # if sufficient squares have been printed, return from recursive calls
    if counter == n:
        return

    if (lo == hi):
        # make 1D list into 2D list
        square = make_two_dim(a)

        # print the square if it is a magic square
        if check_square(square):
            print_square(square)
            counter += 1


    # chck that each of the rows adds to correct value before calling recursive function
    else:
        for i in range(lo, hi):
            if (((a[0] + a[1] + a[2] + a[3]) == 34) or lo < 5):
                if ((a[4] + a[5] + a[6] + a[7]) == 34 or lo < 10):
                    if ((a[8] + a[9] + a[10] + a[11]) == 34 or lo < 15):
                        if ((a[12] + a[13] + a[14] + a[15]) == 34 or lo < 20):
                            a[lo], a[i] = a[i], a[lo]
                            permute(a, lo + 1, n)
                            a[lo], a[i] = a[i], a[lo]

def main():
    n = int(input("Enter number of magic squares(1-10): "))
    # generate a 1D list of integers 1 through 16
    int_list = []
    for i in range(1, 17):
        int_list.append(i)

    while n not in range(1, 11):
        n = int(input("Enter number of magic squares (1-10): "))
    # create all possible permutations of list and print out magic squares
    permute(int_list, 0, n)

main()
