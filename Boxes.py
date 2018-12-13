#  File: Boxes.py

#  Description: This program takes a list of boxes of varying dimensions and
#               returns the largest subsets of boxes that are nestable - or
#               in other words, fit within one another.

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 16th October 2018

#  Date Last Modified: 17th October 2018

# recursive function that goes through and determines the subsets of boxes
def sub_sets(a, b, lo, nested):
    hi = len (a)
    # base case
    if (hi == lo):
        # append the subset to the nested list to save subsets that are nestable
        if all_fit(b):
            nested.append(b)
            return
    # recursive case
    else:
        c = b[:]
        b.append(a[lo])
        sub_sets(a, c, lo + 1, nested)
        sub_sets(a, b, lo + 1, nested)

# given a subset of boxes, check that the sorted boxes are nestable
# this means that the previous box has to be strictly smaller than the next
def all_fit(sub_set):
    for i in range(len(sub_set) - 1):
        if (not does_fit(sub_set[i], sub_set[i + 1])):
            return False
    return True

# check that box 1 has strictly smaller dimensions than box 2
def does_fit(box1, box2):
    return ((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2]))

def main():
    # open the file and read number of boxes
    in_file = open('boxes.txt', 'r')
    line = in_file.readline()
    num_boxes = int(line)

    # create list to store dimensions of all boxes in file
    box_dims = []

    # append dimensions of each box to 2D list, box_dims
    for i in range(num_boxes):
        line = in_file.readline()
        line.strip()
        x, y, z = line.split(' ')
        dims = [int(x), int(y), int(z)]
        dims.sort()
        box_dims.append(dims)
    # Sort the boxes' in ascending order by dimensions
    box_dims.sort()
    # close the file
    in_file.close()

    # create list that will store all nestable subsets
    nestable = []

    # call recursive sub_sets function
    b = []
    sub_sets(box_dims, b, 0, nestable)

    # determine the max length of the subsets
    max = 0
    for sub_set in nestable:
        if (len(sub_set) > max):
            max = len(sub_set)

    # create a temporary list to save subsets that are not of max size
    temp = []
    # cannot remove directly from nestable since that will change the indices mid-loop
    for i in range(0, len(nestable)):
        if (len(nestable[i]) != max):
            # store these smaller subsets in temp list
            temp.append(nestable[i])

    # use temp list to remove subsets that are not of max size
    for sub_set in temp:
        nestable.remove(sub_set)

    # sort list of nestable subsets of max size
    nestable.sort()

    # print out the largest subsets of nesting boxes if applicable
    if (len(nestable) > 0):
        print('Largest Subset of Nesting Boxes')
        # go through the subsets and print out the boxes
        for sub_set in nestable:
            for box in sub_set:
                print(box)
            print()
    # notify if there are no nesting boxes in the set
    else:
        print('No Nesting Boxes')

main()
