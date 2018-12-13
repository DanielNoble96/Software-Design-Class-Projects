#  File: Work.py 

#  Description: This program uses a modified binary search algorithm to compute
#               the minimum value of v, lines of code to write before the
#               productivity factor k halves v, in order to write n lines

#  Student Name: Daniel A. Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 7th October 2018

#  Date Last Modified: 7th October 2018


# Function checks whether value of v is valid for the given n and k
def check_lines (n, k, v):
    p = 1          # p is number of iterations
    total_written = v

    # Determine if v is valid for given n and k, by computing series sum
    while (total_written < n):
        # check number of lines written, and calculate next amount
        lines_written = v // k ** p
        
        if lines_written != 0:
            total_written += lines_written
            p += 1

        # if no more lines can be written
        elif lines_written == 0:
            break

    # return whether or not v works
    if total_written >= n:
        return True
    else:
        return False

        
# Function to compute v, the minimum lines to write before coffee
# Takes as input the productivity factor k and total lines n
# Works as a modified binary search algorithm
def determine_lines (n, k):
    low = 1
    high = n

    # loop runs as long as low is not set higher than high
    while (low <= high):
        mid = (low + high) // 2

        v_works = check_lines(n, k, mid)
        # check if v meets criteria and save value in case smaller v not found
        if v_works:
            high = mid - 1
            v = mid

        # check if v is too small and increase low
        elif (not v_works):
            low = mid + 1
    
    return v


def main():
    # Open the work file
    in_file = open('work.txt', 'r')

    # Read the number of test cases (first line)
    test_cases = int(in_file.readline())
    
    for i in range(test_cases):
        # read values for n and k
        line = in_file.readline()
        line = line.strip()
        my_list = line.split(" ")

        n = int(my_list[0])
        k = int(my_list[1])

        min_lines = determine_lines(n, k)
        print(min_lines)
        
    # Close the work file
    in_file.close()

    
main()
