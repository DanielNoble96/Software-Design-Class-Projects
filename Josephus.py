#  File: Josephus.py

#  Description: This program solves the Josephus problm. It reads a data file and creates a circular linked list
#               based on that file. Given an elimination number and starting point, it then deletes links based on
#               that information until there is only one left, which is then also outputted

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 9th November 2018

#  Date Last Modified: 10th November 2018

class Link(object):
    # Constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
        
class CircularList(object):
    # Constructor
    def __init__ (self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        # create a link and set to start
        newLink = Link(data)
        current = self.first

        # check if list is empty and if so, add link
        if (current == None):
            self.first = newLink
            newLink.next = newLink
            return

        # search through list until end is found
        while (current.next != self.first):
            current = current.next

        # insert link at the end of the list
        current.next = newLink
        newLink.next = self.first
        

    # Find the link with the given data (value)
    def find(self, data):
        # set link to the beginning of the list
        current = self.first

        # search list for a match
        while (current.data != data):
            current = current.next

        # return the link if found; otherwise return None
        return current


    # Delete a link with a given data (value)
    def delete (self, data):
        # set to start of the list
        current = self.first
        previous = self.first

        # check if list is empty and return None if so
        if (current == None):
            return None

        # search the list until a match is found           
        while (current.data != data):
            previous = current
            current = current.next

        # check that there is still more than one link and delete
        if (self.first != self.first.next):
            self.first = current.next
        # check if there is only one link left and delete
        else:
            self.first = None

        previous.next = current.next


    # Delete the nth link starting from the Link start
    # Return the next link from the deleted link
    def deleteAfter (self, start, n):
        # set the starting link
        current = self.find(start)

        # look for the nth link from the starting link
        for i in range(1, n):
            current = current.next

        # print the nth link
        print(current.data)

        # delete the nth link
        self.delete(current.data)

        # return the next link from the deleted link
        return current.next

    # Return a string representation of a Circular List
    def __str__ (self):
        return str(current.data)
        
def main():
    # open file and read in the number of soliders, starting point and elimination number
    in_file = open("josephus.txt", "r")
    n_soldiers = int(in_file.readline())
    start = int(in_file.readline())
    n_eliminate = int(in_file.readline())

    # close the file
    in_file.close()


    # create a circular linked list of soldiers
    soldiers = CircularList()

    # populate the list with the soldiers as links
    for i in range(1, n_soldiers + 1):
        soldiers.insert(i)

    # go through the list,  deleting the appropriate link until there is one left
    for i in range(1, n_soldiers):
        start = soldiers.deleteAfter(start, n_eliminate)
        start = start.data

    # this is the last soldier who escapes; print out the soldier's number
    soldiers.deleteAfter(start, n_eliminate)
    
main()
