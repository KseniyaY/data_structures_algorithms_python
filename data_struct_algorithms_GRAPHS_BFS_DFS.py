import pprint
from collections import deque

"""The simplified solution 1 (from "Grokking Algoritms")

Breadth-first search takes O(number of
vertices + number of edges), and it’s more commonly written as O(V+E)
(V for number of vertices, E for number of edges).
"""

graph0 = {}

graph0["you"] = ["alice", "bob", "claire"]
graph0["bob"] = ["anuj", "peggy"]
graph0["alice"] = ["peggy"]
graph0["claire"] = ["thom", "jonny"]
graph0["anuj"] = []
graph0["peggy"] = []
graph0["thom"] = []
graph0["jonny"] = []


def search(name, graph):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


search("you", graph0)

"""
the Node class now has a visited flag that we can use during the traversals. 
Write a recursive solution for DFS and an iterative solution for BFS.
"""

# for prettier print


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers


class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The n-th name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        # create a new path object assigning 'node_from_val'
        # and 'node_to_val' parameters' values as object keys
        # None as object values so far
        path = {
            node_from_val: None,
            node_to_val: None
        }
        # if there is any node in the node list corresponding to
        # a key in the 'path' object, assign that node object from the list
        # as a value for a key-value pair of the 'path' object
        for node in self.nodes:
            if node.value in path:
                path[node.value] = node
                # stop looping through the list of nodes
                # as soon as both values in the 'path' object have been already assigned
                if all(path.values()):
                    break
        for node_val in path:
            # leave a value as is or if it is not defined
            # then insert a newly created node as a 'path' value
            path[node_val] = path[node_val] or self.insert_node(node_val)
        # assign node objects to 'node_from' and 'node_to' variables
        # and pass these variables as arguments to the constructor
        # for the new edge
        node_from = path[node_from_val]
        node_to = path[node_to_val]

        # now a new edge is ready to be constructed and added to the list of edges
        new_edge = Edge(new_edge_val, node_from, node_to)
        # append newly created edge to the exising edges in node objects
        # sitting, in their turn, in 'node_from' and 'node_to' objects,
        """should sort out why do we need these two code lines eventually????
        looks like cyclic edges"""
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        # add newly created edge to the list of edges as well
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value)
                for edge in self.edges]
        # list comprehension for placing tuples with three values for each edge

    def get_edge_list_names(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge.value,
                 self.node_names[edge.node_from.value],
                 self.node_names[edge.node_to.value])
                for edge in self.edges]

    def get_adjacency_list(self):
        # Return a list of lists
        max_index = self.calc_list_size()
        adjacency_list = [[] for _ in range(max_index)]
        for edge in self.edges:
            from_value, to_value = edge.node_from.value, edge.node_to.value
            """
            The indicies of the ajacency list represent "from" nodes.
            Each section in the adjency list will store a list
            of tuples that looks like this:
            (To Node/to_value, Edge Value)
            """
            adjacency_list[from_value].append((to_value, edge.value))
        return [a or None for a in adjacency_list]  # replace []'s with None

    def get_adjacency_list_names(self):
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""
        adjacency_list = self.get_adjacency_list()

        def convert_to_names_helper(pair, graph=self):
            node_number, node_value = pair
            return (graph.node_names[node_number], node_value)

        def map_name_conversion(adj_list_for_node):
            if adj_list_for_node is None:
                return None
            return map(convert_to_names_helper, adj_list_for_node)

        # list comprehension for each node tuple
        # extracted from the adjacency_list with mapping
        return [map_name_conversion(adj_list_for_node)
                for adj_list_for_node in adjacency_list]

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.calc_list_size()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]

        for edge in self.edges:
            from_index, to_index = edge.node_from.value, edge.node_to.value
            adjacency_matrix[from_index][to_index] = edge.value
        return adjacency_matrix

    # create a helper function to define the size of the lists
    # to build an adjacency list and adjacency matrix
    def calc_list_size(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_val = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_val:
                    max_val = node.value
                    # the size should equal to the max value among the nodes
                    # and serve as an edge value for the built-in range fuction
        return max_val

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self, start_node):
        """The helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        REQUIRES: self._clear_visited() to be called before
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """
        trav_list = [start_node.value]
        start_node.visited = True
        # grab all edges except that one which belongs to the start node
        edges_out = [edg for edg in start_node.edges
                     if edg.node_to.value != start_node.value]
        # loop through these edges now and if there is no visited nodes
        # put to the traversal list
        # repeat the entire process with the recursion until
        # there is no unvisited nodes left
        for edge in edges_out:
            if not edge.node_to.visited:
                trav_list.extend(self.dfs_helper(edge.node_to))
        return trav_list

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        """TODO: Create an iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        trav_list = []
        # Put start node in queue
        queue = [node]
        node.visited = True

        def enqueue(n, q=queue):
            n.visited = True
            q.append(n)

        def unvisited_outgoing_edge(node, edg):
            return ((edg.node_from.value == node.value) and
                    (not edg.node_to.visited))
        # while we have a node in the queue to traverse
        while queue:
            # remove the current node from the queue and
            # put this node to the trav_list with other traversed nodes
            node = queue.pop(0)
            trav_list.append(node.value)
            # then check each edge in the current node:
            # whether this current node value equals
            # a node value where the current edge
            # took its beginning from, and also
            #  whether that node, the current edge is traveling to,
            # is visited or not
            for edg in node.edges:
                if unvisited_outgoing_edge(node, edg):
                    # and if all conditions are true
                    # put such node ('node_to' from the edge)
                    # in the queue for the next iteration
                    enqueue(edg.node_to)
        return trav_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]


graph = Graph()

# You do not need to change anything below this line.
# You only need to implement Graph.dfs_helper and Graph.bfs

graph.set_node_names(('Mountain View',   # 0
                      'San Francisco',   # 1
                      'London',          # 2
                      'Shanghai',        # 3
                      'Berlin',          # 4
                      'Sao Paolo',       # 5
                      'Bangalore'))      # 6

graph.insert_edge(51, 0, 1)     # MV <-> SF
graph.insert_edge(51, 1, 0)     # SF <-> MV
graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
graph.insert_edge(932, 2, 4)    # London <-> Berlin
graph.insert_edge(932, 4, 2)    # Berlin <-> London
graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
# (6) 'Bangalore' is intentionally disconnected (no edges)
# for this problem and should produce None in the
# Adjacency List, etc.

pp = pprint.PrettyPrinter(indent=2)

print("Edge List")
pp.pprint(graph.get_edge_list_names())

print("\nAdjacency List")
pp.pprint(graph.get_adjacency_list_names())

print("\nAdjacency Matrix")
pp.pprint(graph.get_adjacency_matrix())

print("\nDepth First Search")
pp.pprint(graph.dfs_names(2))

# Should print:
# Depth First Search
# ['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin', 'Sao Paolo']

print("\nBreadth First Search")
pp.pprint(graph.bfs_names(2))
# test error reporting
# pp.pprint(['Sao Paolo', 'Mountain View', 'San Francisco',
#           'London', 'Shanghai', 'Berlin'])

# Should print:
# Breadth First Search
# ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']
