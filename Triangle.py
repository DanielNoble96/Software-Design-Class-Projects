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

        # increment counter
        counter += 1

        # go through linked list, updating for each node, until a node equals none
        while (current_link != None):
            current_link = current.next
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

        return current_link

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
        # start at beginning of the list
        current_link = self.first

        # check if list is empty
        if (current_link == None):
            return None

        while (current_link.data != None):
            # reached the end and it was not found
            if (current_link.next == None):
                return None
            # otherwise, move to the next link
            else:
                current_link = current_link.next

        return current_link

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

        return current_link

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

    # Reverse the contents of a list and return new list
    def reverse_list (self):

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):

    # Return True if a list is empty or False otherwise
    def is_empty (self):
        return (self.first == None)

def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    testList = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
    list1 = LinkedList()
    for el in testList:
        list1.insert_first(el)
    print(list1)
    print()

    # Test method insert_last()

    # Test method insert_in_order()

    # Test method get_num_links()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there

    # Test method delete_link()
    # Consider two cases - data is there, data is not there

    # Test method copy_list()

    # Test method reverse_list()

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()

if __name__ == "__main__":
    main()
