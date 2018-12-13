#  File: TopoSort.py

#  Description: This program reads a text file and creates a directed graph
#               based on this information. It then checks if the graph is cyclical
#               and outputs the results of a topological sort.

#  Student Name: Daniel Alejandro Noble Hernandez

#  Student UT EID: dan833

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 2nd December 2018

#  Date Last Modified: 3rd December 2018

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append ( item )

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek (self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty (self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len(self.stack))


class Queue (object):
    # constructor
    def __init__ (self):
        self.queue = []

    # adds an item to the queue
    def enqueue (self, item):
        self.queue.append (item)

    # removes an item from the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # checks if the queue is empty
    def isEmpty (self):
        return (len (self.queue) == 0)

    # returns the size of the queue
    def size (self):
        return len (self.queue)


class Vertex (object):
    # constructor
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def wasVisited (self):
        return self.visited

    # determine the label of the vertex
    def getLabel (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)


class Edge (object):
    # constructor
    def __init__ (self, fromVertex, toVertex, weight = 1):
        self.fr = fromVertex
        self.to = toVertex
        self.weight = weight


class Graph (object):
    # constructor
    def __init__ (self):
        self.Vertices = []
        self.Edges = []
        self.adjMat = []

    # check if a vertex already exists in the graph
    def hasVertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).label):
                return True
            return False


    # given a label get the index of a vertex
    def getIndex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if ((self.Vertices[i]).label == label):
                return i
        return -1


    # add a Vertex with a given label to the graph
    def addVertex (self, label):
        # check that vertex does not already exist before adding it
        if not self.hasVertex(label):
            self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix for the new Vertex
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new Vertex in the adjacency matrix
        newRow = []
        for i in range(nVert):
            newRow.append(0)
        self.adjMat.append(newRow)


    # add weighted directed edge to graph
    def addDirectedEdge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def addUndirectedEdge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v
    def getAdjUnvisitedVertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
                return i
        return -1


    # do the depth first search in a graph
    def dfs (self, v):
        # create a Stack
        theStack = Stack()

        # mark vertex v as visited and push on the stack
        (self.Vertices[v]).visited = True
        print (self.Vertices [v])
        theStack.push (v)

        # vist other vertices according to depth
        while (not theStack.isEmpty()):
            # get an adjacent unvisited vertex
            u = self.getAdjUnvisitedVertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push(u)

        # the stack is empty let us reset the falgs
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do breadth first search in a graph
    def bfs (self, v):
        # create a Queue
        theQueue = Queue ()

        # mark vertex v as visited and add to the queue
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theQueue.enqueue(v)

        # visit other vertices according to breadth
        while (not theQueue.isEmpty()):
            # get vertex at the front and an unvisited adjacted vertex
            vertex = theQueue.dequeue()
            u = self.getAdjUnvisitedVertex(vertex)
            while (u != -1):
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)
                u = self.getAdjUnvisitedVertex(vertex)

        # reset flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
        x = self.getIndex(fromVertexLabel)
        y = self.getIndex(toVertexLabel)
        if (self.adjMat[x][y] != 0):
            return self.adjMat[x][y]
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def getNeighbors (self, vertexLabel):
        # create a list to hold the immediate neighbors
        neighbours = []

        # find current index
        idx = self.getIndex(vertexLabel)

        for i in range(len(self.adjMat[idx])):
            if (self.adjMat[idx][i] != 0):
                neighbours.append(self.Vertices[i])
        return neighbours

    # get a copy of the list of vertices
    def getVertices (self):
        return self.Vertices[:]

    # delete an edge from the adjacency matrix
    def deleteEdge (self, fromVertexLabel, toVertexLabel):
        # get index of from and to labels
        x = self.getIndex(fromVertexLabel)
        y = self.getIndex(toVertexLabel)

        # search list of edges and remove the appropriate one
        for edge in self.Edges:
            if ((edge.fr.label == fromVertexLabel) and (edge.to.label == toVertexLabel)):
                self.Edges.remove(edge)

        # update the adjacency matrix
        self.adjMat[x][y] = 0


    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def deleteVertex (self, vertexLabel):
        # gets index of the vertex label
        idx = self.getIndex(vertexLabel)

        # removes vertex from the graph
        for vertex in self.Vertices:
            if vertexLabel == vertex.label:
                self.Vertices.remove(vertex)

        # updates the adjacency matrix to reflect the graph
        for i in range(len(self.adjMat)):
            del self.adjMat[i][idx]
        del self.adjMat[idx]

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def hasCycle (self):
        for i in range(len(self.Vertices)):
            # create a stack
            theStack = Stack()

            # mark the vertex as visited and push on the stack
            (self.Vertices[i]).visited = True
            theStack.push (i)

            # Once empty, all vertices have been visited
            while (not theStack.isEmpty()):
                # Check if a back edge to the starting vertex exists and return true if so
                if self.hasCycle_helper(theStack.peek(), i):
                    return True
                # get an adjacent unvisited vertex
                u = self.getAdjUnvisitedVertex (theStack.peek())
                if (u == -1):
                    u = theStack.pop()
                else:
                    (self.Vertices[u]).visited = True
                    theStack.push(u)

            # reset the flags
            nVert = len(self.Vertices)
            for i in range(nVert):
                (self.Vertices[i]).visited = False
        return False

    # Helper function for hasCycle
    def hasCycle_helper(self, unvisited, visited):
        # checks if vertex at index u is goes to vertex at index v
        for edge in self.Edges:
            if (edge.u == self.Vertices[u]) and (edge.v == self.Vertices[v]):
                return True
        return False


    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        # initialize index and lists to keep track of location
        sorted = []
        delete = []
        idx = 0
        # make a copy of the existing graph
        copy = Graph()
        copy.Vertices = self.Vertices
        copy.adjMat = self.adjMat

        while (len(copy.Vertices) > 0):
            idx = 0
            while (idx < len(copy.Vertices)):
                # set the visited flag to false and obtain vertex label
                visited = False
                vertex = copy.Vertices[idx].label
                for i in range(len(copy.Vertices)):
                    # check if the vertex has been visited
                    if (copy.adjMat[i][idx] == 1):
                        visited = True
                        break
                # increment the index for visited vertex
                if (visited):
                    idx += 1
                else:
                    sorted.append(vertex)
                    delete.append(vertex)
                    idx += 1
            while (len(delete) > 0):
                copy.deleteVertex(delete[0])
                delete.pop(0)

        return sorted


def main():
    # create a Graph object
    graph = Graph()

    # open file for reading
    inFile = open("topo.txt", "r")

    # read the Vertices
    numVertices = int((inFile.readline()).strip())

    # create the graph with vertices from the file
    for i in range(numVertices):
        vertex = (inFile.readline()).strip()
        graph.addVertex(vertex)

    # read the edges
    numEdges = int((inFile.readline()).strip())

    # add the edges to the graph
    for i in range(numEdges):
        edge = (inFile.readline()).strip()
        edge = edge.split()
        start = int(graph.getIndex(edge[0]))
        finish = int(graph.getIndex(edge[1]))
        graph.addDirectedEdge(start, finish)

    # close file
    inFile.close()

    # test if a directed graph has a cycle
    cyclical = graph.hasCycle()
    print('Graph has a cycle: ', cyclical)

    # test topological sort
    print('Topological sort: ')
    topological = graph.toposort()
    for vertex in topological:
        print(vertex)


if __name__ == "__main__":
    main()
