# The easiest way to find the shortest path between two nodes in a graph
'''
One of the simplest and most efficient algorithms for finding the shortest path between two nodes in a graph is Dijkstra's algorithm.

This code defines the dijkstra function that takes a graph represented as an adjacency list and the starting node. 
It returns a dictionary of shortest distances from the start node to every other node. Additionally, 
it finds and prints the shortest path from the start node to the end node.

time complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph.
space complexity: O(V), where V is the number of vertices in the graph.
'''

import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with start node having distance 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Priority queue to store nodes to visit, with their current shortest distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip nodes that have already been visited with a shorter distance
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If new distance is shorter, update distance and add to priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'

shortest_distances = dijkstra(graph, start_node)
shortest_path_distance = shortest_distances[end_node]
print(f"The shortest distance from {start_node} to {end_node} is: {shortest_path_distance}")

# Finding the shortest path
path = [end_node]
current_node = end_node
while current_node != start_node:
    for neighbor, weight in graph[current_node].items():
        if shortest_distances[current_node] == shortest_distances[neighbor] + weight:
            path.append(neighbor)
            current_node = neighbor
            break

path.reverse()
print(f"The shortest path is: {' -> '.join(path)}")

'''
A priority queue is the main element in this function which helps us keep track of distances from sources to other nodes 
which are present in the graph. The algorithm adds a source node to the priority queue and the priority queue is 
distinguished by the distances of the nodes in the queue. Shortest distance of node from source node will be present
at the front of the queue. The function here eliminates when the priority queue is emptying which tells us nodes present
in the graph have been traveled and their distances to the source node have been calculated.
'''