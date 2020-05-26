graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {
    'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = float("inf")
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + \
                    shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graph, 'a', 'b')


# Solution 2
"""
Timecomplexity is probably O(V^2 + E) where V is number of vertices
and E is number of edges. 
However, if the find_cheapest_vertex was implemented better as
a min que heap, O(V lg V + E) could be achievable
"""
inf = float("inf")
start_vertex = "a"
stop_vertex = "b"

graph2 = {}
graph2["a"] = {}
graph2["a"]["b"] = 10
graph2["a"]["c"] = 3

graph2["b"] = {}
graph2["b"]["c"] = 1
graph2["b"]["d"] = 2

graph2["c"] = {}
graph2["c"]["b"] = 4
graph2["c"]["d"] = 8
graph2["c"]["e"] = 2

graph2["d"] = {}
graph2["d"]["e"] = 7

graph2["e"] = {}
graph2["e"]["d"] = 9

# if the vertex doesn't connect to anything else new further
# then we just create the empty object for it. For instance,
# if there would be no other child vertices for D, then it would be simply initiated like:
# graph2["d"] = {}

# graph2 = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {
#     'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra2(graph, start, stop):
    costs = {}
    predecessors = {}

    for vertex in graph:
        costs[vertex] = inf  # as a start value before it is changed
        predecessors[vertex] = {}

        costs[start] = 0

    def find_cheapest_vertex(costs, unvisited):
        cheapest_vertex = None
        lowest_cost = inf
        for vertex in unvisited:
            if costs[vertex] < lowest_cost:
                lowest_cost = costs[vertex]
                cheapest_vertex = vertex
        return cheapest_vertex

    not_checked = [vertex for vertex in costs]
    vertex = find_cheapest_vertex(costs, not_checked)
    while not_checked:
        #print(f"Not Checked: {not_checked}")
        cost = costs[vertex]
        child_cost = graph[vertex]
        for c in child_cost:
            if costs[c] > cost + child_cost[c]:
                costs[c] = cost + child_cost[c]
                predecessors[c] = vertex
        not_checked.pop(not_checked.index(vertex))
        vertex = find_cheapest_vertex(costs, not_checked)
    print(f"Costs: {costs}")
    print(f"The cost to go from {start} to {stop} is {costs[stop]}!")

    # print the path
    if costs[stop] < inf:
        path = [stop]
        i = 0
        while start not in path:
            path.append(predecessors[path[i]])
            i += 1
        print(f"The shortest path is {path[::-1]}")
    else:
        print("A path could not be found")


dijkstra2(graph2, start_vertex, stop_vertex)

graph3 = {}
start_point = "Noob"
stop_point = "GodOfCode"

graph3["Noob"] = {}
graph3["Noob"]["BS"] = 4
graph3["Noob"]["SelfTaught"] = 1
graph3["Noob"]["Bootcamp"] = 2

graph3["SelfTaught"] = {}
graph3["SelfTaught"]["EntryLevel"] = 3
graph3["SelfTaught"]["Networked"] = 1
graph3["SelfTaught"]["Bootcamp"] = 0.5

graph3["Bootcamp"] = {}
graph3["Bootcamp"]["EntryLevel"] = 0.5

graph3["Networked"] = {}
graph3["Networked"]["EntryLevel"] = 0.5

graph3["BS"] = {}
graph3["BS"]["MS"] = 2
graph3["BS"]["EntryLevel"] = 0.5

graph3["MS"] = {}
graph3["MS"]["PhD"] = 3
graph3["MS"]["MidLevel"] = 1

graph3["PhD"] = {}
graph3["PhD"]["PostDoc"] = 2
graph3["PhD"]["MidLevel"] = 0
graph3["PhD"]["Expert"] = 2

graph3["PostDoc"] = {}
graph3["PostDoc"]["Academic"] = 10

graph3["Academic"] = {}
graph3["Academic"]["GodOfCode"] = inf

graph3["EntryLevel"] = {}
graph3["EntryLevel"]["MidLevel"] = 5

graph3["MidLevel"] = {}
graph3["MidLevel"]["Expert"] = 5

graph3["Expert"] = {}
graph3["Expert"]["GodOfCode"] = 5

graph3["GodOfCode"] = {}


dijkstra2(graph3, start_point, stop_point)
