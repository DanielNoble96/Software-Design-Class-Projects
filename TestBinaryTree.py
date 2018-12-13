#  File: TestBinaryTree.py

#  Description: This program creates trees and tests several functions that compare the trees,
#               prints the nodes at each level, counts the number of nodes, and gives the tree heights

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 13th November 2018

#  Date Last Modified: 16th November 2018

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__ (self):
        self.root = None
        self.size = 0

    # insert data into a tree
    def insert (self, data):
        new_node = Node (data)

        if (self.root == None):
            self.root = new_node
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

        self.size += 1

    # search for a node with a key
    def search (self, data):
        current = self.root
        while (current != None) and (current.data != data):
            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild
        return current

    # in order traversal - left, center, right
    def in_order (self, aNode):
        if (aNode != None):
            self.in_order (aNode.lchild)
            print (aNode.data)
            self.in_order (aNode.rchild)

    # pre order traversal - center, left, right
    def pre_order (self, aNode):
        if (aNode != None):
            print (aNode.data)
            self.pre_order (aNode.lchild)
            self.pre_order (aNode.rchild)

    # post order traversal - left, right, center
    def post_order (self, aNode):
        if (aNode != None):
            self.post_order (aNode.lchild)
            self.post_order (aNode.rchild)
            print (aNode.data)

    # delete a node with a given key
    def delete (self, data):
        delete_node = self.root
        parent = self.root
        is_left = False

        # if empty tree
        if (delete_node == None):
            return None

        # find the key if it exists
        while (delete_node != None) and (delete_node.data != data):
            parent = delete_node
            if (data < delete_node.data):
                delete_node = delete_node.lchild
                if_left = True
            else:
                delete_node = delete_node.rchild
                is_left = False

        # if node not found
        if (delete_node == None):
            return None

        # check if the delete node is a leaf node
        if (delete_node_node.lchild == None) and (delete_node.rchild == None):
            if (delete_node == self.root):
                self.root = None
            elif (is_left):
                parent.lchild = None
            else:
                parent.rchild = None

        # check if the delete node is a node with only a left child
        elif (delete_node.rchild == None):
            if (delete_node == self.root):
                self.root = delete_node.lchild
            elif (is_left):
                parent.lchild = delete_node.lchild
            else:
                parent.rchild = delete_node.lchild

        # check if the delete node has only a right child


        # delete node has both left and right children
        else:
            # find the delete node's successor and successor's parent
            successor = delete_node.rchild
            successor_parent = delete_node

            while (successor.lchild != None):
                successor_parent = successor
                successor = successor.lchild

            if (delete_node == self.root):
                self.root = successor
            elif (is_left):
                parent.lchild = successor
            else:
                parent.rchild = successor

            # connect the delete node's child to be the successor's left child
            successor.lchild = delete_node.lchild

            if (successor != delete_node.rchild):
                successor_parent.lchild = successor.rchild
                successor.rchild = delete_node.rchild

        return delete_node

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        # check if both trees are empty
        if (self.root==None and pNode.root==None):
            return True

        # ensure the trees are the same size
        elif self.size != pNode.size:
            return False

        # call recursive helper function to compare the trees
        else:
            return (self.is_similar_helper(self.root,pNode.root))

    def is_similar_helper(self, node1, node2):
        # check if both nodes are empty
        if ((node1 == None) and (node2 == None)):
            return True

        # go to the next nodes
        elif ((node1.data == node2.data) and self.is_similar_helper(node1.lchild, node2.lchild) and self.is_similar_helper(node1.rchild, node2.rchild)):
            return True

        else:
            return False

    # Prints out all nodes at the given level
    def print_level (self, level):
        # create empty array for the nodes
        nodes = []
        # call helper function
        self.print_level_helper (level, 1, nodes, self.root)

        # no nodes at this level
        if len(nodes) == 0:
            return
        else:
            for node in nodes:
                print(node)

    # Helper function to print the nodes at the level
    def print_level_helper (self, level, current_level, nodes, aNode):
        if current_level > level:
          return

        if aNode == None:
          return
        else:
          if current_level == level:
            nodes.append(aNode.data)
          else:
            self.print_level_helper (level, current_level + 1, nodes, aNode.lchild)
            self.print_level_helper (level, current_level + 1, nodes, aNode.rchild)

    # Returns the height of the tree
    def get_height (self):
        # check if tree is empty
        if (self.root == None):
            return 0
        # call function to find height
        else:
            return self.get_height_helper (self.root)

    def get_height_helper (self, root2):
        # check if empty node has been reached
        if (root2 == None):
            return 0
        # go to the next node
        else:
            left_height = self.get_height_helper (root2.lchild)
            right_height = self.get_height_helper (root2.rchild)

        if (left_height > right_height):
            return (left_height + 1)
        else:
            return (right_height + 1)


    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        return self.num_nodes_helper(self.root)

    # counts the number of nodes
    def num_nodes_helper(self, node1):
        if node1 == None:
            return 0
        else:
            return 1 + self.num_nodes_helper (node1.lchild) + self.num_nodes_helper (node1.rchild)

def main():
    # Create three trees - two are the same and the third is different
    tree_1=Tree()
    tree_2=Tree()
    tree_3=Tree()
    elements =[50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]

    # Make trees 1 and 2 identical to one another
    for el in elements:
        tree_1.insert(el)
        tree_2.insert(el)

    # Make tree 3 different from the others
    for i in range(10):
        tree_3.insert(i)

    # print out each of the trees
    print('Tree 1: ')
    tree_1.in_order(tree_1.root)
    print()

    print('Tree 2: ')
    tree_2.in_order(tree_2.root)
    print()

    print('Tree 3: ')
    tree_3.in_order(tree_3.root)
    print()

    # Test the is_similar function
    print('\nTesting for the is_similar function: ')

    # Compare trees 1 and 2
    if (tree_1.is_similar(tree_2)):
        print('Tree 1 is similar to Tree 2.')
    else:
        print('Tree 1 is not similar to Tree 2.')

    # Compare trees 2 and 3
    if (tree_2.is_similar(tree_3)):
        print('Tree 2 is similar to Tree 3.\n')
    else:
        print('Tree 2 is not similar to Tree 3.\n')

    # Print the various levels of two of the trees that are different
    # Test the print_level function
    print('\nTesting for the print_level function: ')

    # Print level 1 for two of the different trees
    print('\nPrint level 1 of tree 1:')
    tree_1.print_level(1)

    print('\nPrint level 1 of tree 3:')
    tree_3.print_level(1)

    # Print level 2 for two of the different trees
    print('\nPrint level 2 of tree 1:')
    tree_1.print_level(2)

    print('\nPrint level 2 of tree 3:')
    tree_3.print_level(2)

    # Get the height of the two trees that are different
    print('\nTesting for the get_height function: ')
    print('Tree 1 height: ', tree_1.get_height())
    print('Tree 3 height: ', tree_3.get_height())

    # Get the total Number of nodes a binary search tree
    print('\nTesting for the num_nodes function: ')
    print('Number of nodes in tree 1: ', tree_1.num_nodes())
    print()
    print('Number of nodes in tree 3: ', tree_3.num_nodes())
    print()

main()
