"""
You should become comfortable with various graph representations—graphs
crop up often in interviews and in computer science in general,
and you could need to represent it in any of it's forms.

In this exercise you'll need to add functions to a Graph class
to return various representations of the same graph.
Your graph will have two different components: Nodes and Edges.
A Graph class contains a list of nodes and edges. You can sometimes get by with
just a list of edges, since edges contain references to the nodes they connect to,
or vice versa. However, our Graph class is built with both for the following reasons:

If you're storing a disconnected graph, not every node will be tied to an edge,
so you should store a list of nodes.
We could probably leave it there, but storing an edge list will make our lives
much easier when we're trying to print out different types of graph representations.
Unfortunately, having both makes insertion a bit complicated.
We can assume that each value is unique, but we need to be careful about
keeping both nodes and edges updated when either is inserted.
You'll also be given these insertion functions to help you out:
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    # def insert_node(self, new_node_val):
    #     new_node = Node(new_node_val)
    #     self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            # if node with a val we want to add an edge from exists
            # we assign that node to the variable 'node from val'
            # same thing for the second condition with 'node_to_val'
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        # if we couldn't find a corresponding node for node_from_val and node_to_val
        # while looping through all existing nodes, then we create new nodes with values
        # equal to 'node_from_val' and 'node_to_val' arguments and assign those newly created nodes
        # to varibles 'from_found' and 'to_found' as well as append newly created nodes
        # to the list of nodes. This way while inserting/creating edges, we at the same time
        # also create new/missing nodes for
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        # now a new edge is ready to be constructed and added to the list of edges
        new_edge = Edge(new_edge_val, from_found, to_found)
        self.edges.append(new_edge)

        # from_found.edges.append(new_edge)
        # to_found.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        if self.edges:
            for edge in self.edges:
                edge_list.append(
                    (edge.value, edge.node_from.value, edge.node_to.value))
            return edge_list
        return None

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indicies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        size = self.calc_list_size()
        adjacency_list = [None for i in range(size)]
        for edge in self.edges:
            # if there are also tuples at this adjecency_list position, we extend the inner list
            #  with an additional tuple
            if adjacency_list[edge.node_from.value]:
                adjacency_list[edge.node_from.value].append(
                    (edge.node_to.value, edge.value))
            else:
                # just put the tuple in a brand new list at this adjacency list position
                adjacency_list[edge.node_from.value] = [
                    (edge.node_to.value, edge.value)]
        # those positions in the adjency list which didn't correspond to any value of the
        # 'from_node' value in the list of edges, are simply skipped and left as None
        return adjacency_list

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        size = self.calc_list_size()
        adjacency_matrix = [[0 for i in range(size)] for j in range(size)]
        for edge in self.edges:
            #matrix[n][m] = edge.val
            adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjacency_matrix

    # create a helper function to define the size of the lists
    # to build an adjacency list and adjacency matrix
    def calc_list_size(self):
        max_val = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_val:
                    max_val = node.value
                    # the size should equal to the max value among the nodes + 1
        return max_val + 1


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
