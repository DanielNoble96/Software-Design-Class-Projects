#  File: TestLinkedList.py

#  Description: This program tests a number of helper functions that modify a
#               linked list class that simulates that abstract data type

#  Student Name: Daniel A. Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 3rd November 2018

#  Date Last Modified: 4th November 2018

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class LinkedList (object):
    def __init__ (self):
        self.first = None


    # get number of links
    def get_num_links (self):
        # initialize counter and first link
        counter = 0
        current_link = self.first

        # check for empty list
        if (current_link == None):
            return counter

        # go through linked list, updating for each node, until a node equals none
        while (current_link != None):
            current_link = current_link.next
            counter += 1

        # return the counter value
        return counter


    # add an item at the beginning of the list
    def insert_first (self, data):
        # create a new link
        new_Link = Link(data)

        # specify next value for the link and update first value of linked list
        new_Link.next = self.first
        self.first = new_Link


    # add an item at the end of the list
    def insert_last (self, data):
        # create a new link
        new_Link = Link(data)

        # start at beginning of the linked list
        current_link = self.first

        # check if list is empty
        if (current_link == None):
            self.first = new_Link
            return

        # look for end of the linked list
        while (current_link.next != None):
            current_link = current_link.next

        # set last link's pointer to the new link
        current_link.next = new_Link


    # add an item in an ordered list in ascending order
    def insert_in_order (self, data):
        # create a new link
        new_Link = Link(data)

        # start at the beginning of the linked list
        current_link = self.first
        previous_link = self.first

        # place new link at the beginning if the list is empty or new link's value is smallest
        if (current_link == None) or (current_link.data >= data):
            new_Link.next = self.first
            self.first = new_Link
            return

        while (current_link.next != None):
            if (current_link.data <= data):
                # save current link as previous link for use in else statement
                previous_link = current_link
                current_link = current_link.next
            else:
                # inset link in correct location
                new_Link.next = previous_link.next
                previous_link.next = new_Link
                return

        if (current_link.data <= data):
            current_link.next = new_Link
        else:
            new_Link.next = previous_link.next
            previous_link.next = new_Link
        return


    # search in an unordered list, return None if not found
    def find_unordered (self, data):
        # start at beginning of the list
        current_link = self.first

        # check if list is empty
        if (current_link == None):
            return None

        # check if link was found
        while (current_link.data != data):
            # reached end of list and link was not found
            if (current_link.next == None):
                return None
            # move to the next link
            else:
                current_link = current_link.next

        return current_link.data

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
        # start at beginning of the list
        current_link = self.first

        # check if list is empty
        if (current_link == None):
            return None

        while (current_link.data != data):
            # reached the end and it was not found
            if (current_link.next == None):
                return None
            # otherwise, move to the next link
            else:
                if (current_link.next.data > data):
                    return None
                else:
                    current_link = current_link.next

        return current_link.data

    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        current_link = self.first
        previous_link = self.first

        # check if list is empty
        if (current_link == None):
            return None

        # search for link
        while (current_link.data != data):
            # reached the end and link was not found
            if (current_link.next == None):
                return None
            # save current link as previous link and move to next
            else:
                previous_link = current_link
                current_link = current_link.next

        # delete the link from the list
        if (current_link == self.first):
            self.first = self.first.next
        else:
            previous_link.next = current_link.next

        return current_link.data

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current_link = self.first
        strng = ''
        counter = 0

        if self.is_empty():
            return None

        while (current_link != None):
            # add data for current link to strng, move to next link and increment counter
            strng += str(current_link.data) + '  '
            current_link = current_link.next
            counter += 1

            # if 10 items have been reached, move to a new line
            if (counter % 10 == 0):
                strng += '\n'

        return strng


    # Copy the contents of a list and return new list
    def copy_list (self):
        # create a copy
        copy = LinkedList()
        current_link = self.first

        # check if list is empty
        if (self.first == None):
            return None

        # copy over data to the new list
        while (current_link != None):
            copy.insert_last(current_link.data)
            current_link = current_link.next

        return copy


    # Reverse the contents of a list and return new list
    def reverse_list (self):
        # create list to hold reverse values
        reverse = LinkedList()
        current_link = self.first

        # check if list is empty
        if (self.first == None):
            return None

        # add data from list in reverse order
        while (current_link != None):
            reverse.insert_first(current_link.data)
            current_link = current_link.next

        return reverse


    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):
        # create list to hold sorted contents
        sorted = LinkedList()
        current_link = self.first

        while (current_link != None):
            # insert link in order
            sorted.insert_in_order(current_link.data)
            # move to next link; break out when end of list is reached
            if (current_link.next != None):
                current_link = current_link.next
            else:
                break

        return sorted


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        current_link = self.first

        # go through the list and return False if ascending order condition is not met
        while (current_link.next != None):
            if (current_link.data > current_link.next.data):
                return False
            current_link = current_link.next

        # return True if it made it through the whole list
        return True


    # Return True if a list is empty or False otherwise
    def is_empty (self):
        return (self.first == None)


    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        # make a sorted copy of the list
        merged = self.copy_list()
        merged = merged.sort_list()
        current_link = other.first

        # check cases where one or both lists may be empty
        if (self.first == None):
            if (other.first == None):
                return merged
            else:
                merged = other.copy_list()
                return merged

        elif (other.first == None):
            return merged

        # insert links from other into merged list in ascending order
        while (current_link != None):
            merged.insert_in_order(current_link.data)
            current_link = current_link.next

        return merged


    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        current_link1 = self.first
        current_link2 = other.first

        # check if both are empty
        if (self.is_empty() and other.is_empty()):
            return True

        # check that they have the same number of links
        if (self.get_num_links() != other.get_num_links()):
            return False

        # go through the lists, comparing them link by link
        while (current_link1 != None):
            if (current_link1.data != current_link2.data):
                return False
            current_link1 = current_link1.next
            current_link2 = current_link2.next

        # if the end of the lists are reached, then they are the same
        return True


    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        removed = self.copy_list()
        current_link = removed.first
        previous_link = removed.first
        elements = []

        while (current_link != None):
            if (current_link.data in elements):
                # remove from the linked list if element has been encountered
                current_link = current_link.next
                previous_link.next = current_link
            else:
                elements.append(current_link.data)
                previous_link = current_link
                current_link = current_link.next

        return removed


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    print('Test methods insert_first() and __str__():')
    test = [32, 57, 34, 64, 12, 90, 46, 59, 73, 84, 91, 18, 40, 99]
    list1 = LinkedList()
    for el in test:
        list1.insert_first(el)
    print(list1)
    print()

    # Test method insert_last()
    print('Test method insert_last():')
    list2 = LinkedList()
    for el in test:
        list2.insert_last(el)
    print(list2)
    print()

    # Test method insert_in_order()
    print('Test method insert_in_order():')
    list3 = LinkedList()
    for el in test:
        list3.insert_in_order(el)
    print(list3)
    print()

    # Test method get_num_links()
    print('Test method get_num_links():')
    print(list1.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print('Test method find_unordered():')
    print(list1.find_unordered(57))     # data is there
    print(list1.find_unordered(101))    # data is not there
    print()

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print('Test method find_ordered():')
    print(list3.find_ordered(57))     # data is there
    print(list3.find_ordered(101))    # data is not there
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print('Test method delete_link():')
    print(list1.delete_link(12))
    print(list1.delete_link(101))
    print(list1)                    # 12 is no longer in list1
    print()

    # Test method copy_list()
    print('Test method copy_list():')
    print(list1.copy_list())
    print()

    # Test method reverse_list()
    print('Test method reverse_list():')
    print(list1.reverse_list())
    print()

    # Test method sort_list()
    print('Test method sort_list():')
    print(list1.sort_list())
    print()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print('Test method is_sorted():')
    print(list3.is_sorted())        # sorted list
    print(list2.is_sorted())        # unsorted list
    print()

    # Test method is_empty()
    print('Test method is_empty():')
    list4 = LinkedList()
    print(list4.is_empty())         # empty
    print(list1.is_empty())         # not empty
    print()

    # Test method merge_list()
    print('Test method merge_list():')
    print(list1.merge_list(list2))
    print()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print('Test method is_equal():')
    print(list1.is_equal(list1))    # equal
    print(list1.is_equal(list2))    # not equal
    print()

    # Test remove_duplicates()
    print('Test method remove_duplicates():')
    duplicates = [1, 2, 4, 2, 4, 6, 3, 7]
    list5 = LinkedList()
    for el in duplicates:
        list5.insert_in_order(el)
    print(list5.remove_duplicates())
    print()

if __name__ == "__main__":
    main()
