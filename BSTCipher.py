#  File: BST_Cipher.py

#  Description:

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 10th November 2018

#  Date Last Modified: 10th November 2018

class Node (object):
    def __init__ (self, data, left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None

        for char in encrypt_str:
            if ((ord(char) >= 97 and ord(char) <= 122) or (ord(char) == 32)):
                self.insert(char)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        # create a new node
        new_node = Node(ch)

        # check if the BST is empty and insert node
        if (self.root == None):
            self.root = new_node

        # set cursor to the root and create pointer to parent
        cursor = self.root
        parent = self.root

        # go down through the BST until correct node is reached
        while (cursor != None):
            # save the parent pointer
            parent = cursor

            # check whether to move left or right
            if (ch < cursor.data):
                cursor = cursor.left_child
            elif (ch > cursor.data):
                cursor = cursor.right_child
            # break out if a character already in the BST
            else:
                return

        # use parent pointer to assign node as either left or right child
        if (ch < parent.data):
            parent.left_child = new_node
        elif (ch > parent.data):
            parent.right_child = new_node

        return

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        # set cursor to the root of the BST
        cursor = self.root

        # check if character is the root of the BST
        if (cursor.data == ch):
            return '*'

        strng = ''

        # go through the BST until character is found or end is reached
        while (cursor != None):
            # add either < or > for each left or right taken respectively
            if (ch < cursor.data):
                strng += '<'
                cursor = cursor.left_child
            elif (ch > cursor.data):
                strng += '>'
                cursor = cursor.right_child
            # if character is found in the BST, break out of the loop
            else:
                break

        return strng

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        cursor = self.root

        for char in st:
            if (cursor != None):
                if (char == '*'):
                    break
                elif (char == '<'):
                    cursor = cursor.left_child
                elif (char == '>'):
                    cursor = cursor.right_child
            else:
                return ''

        return cursor.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        # initialize encrypted, which will hold encrypted string
        encrypted_string = ''
        st = st.lower()

        # go through string and generate encrypted string
        for char in st:
            # ignore ineligible characters
            if ((ord(char) >= 97 and ord(char) <= 122) or (ord(char) == 32)):
                # find path taken to get to the char and separate these by !
                encrypted_char = self.search(char)
                encrypted_string += encrypted_char + '!'

        # remove ! at the end of the string
        encrypted_string = encrypted_string[:-1]

        return encrypted_string

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        decrypted_string = ''

        # make a list of the encrypted chars to go through
        encrypted_chars = st.split('!')

        # go through the encrypted characters and decrypt them, adding them to decrypted_string
        for char in encrypted_chars:
            decrypted_char = self.traverse(char)
            decrypted_string += decrypted_char

        return decrypted_string

def main():
    # prompt user for encryption key
    encrypt_key = input('Enter encryption key: ')
    encrypt_key = encrypt_key.lower()
    print()

    # create the binary search tree with the encryption key
    BST = Tree(encrypt_key)

    # prompt user for string to be encrypted
    encrypt_string = input('Enter string to be encrypted: ')
    print('Encrypted string: ' + BST.encrypt(encrypt_string))
    print()

    # prompt user for string to be decrypted
    decrypt_string = input('Enter string to be decrypted: ')
    print('Decrypted string: ' + BST.decrypt(decrypt_string))
    print()

main()
