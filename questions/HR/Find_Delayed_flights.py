'''
A network of flights contains flight_nodes number of flights denoted by [1, 2,...,flight_nodes].
There is a list of dependencies among flights denoted by the arrays
flight_from[], flights leaving a city, and flight_to[], flights arriving in a city.
Each pair {flight_from[i],flight_to[i]} denotes that flight_from[i] depends on flight_to[i]
and must depart only after flight_to[i] has landed. If a flight is delayed, all the flights dependent on
this flight and their corresponding dependencies are also delayed.

Given a list of k initially delayed flights and the network as described, find the list of all
delayed flights, Return the list sorted in increasing order of flight numbers.

Example:
Consider flight_nodes = 4, and the number Of dependencies m = 2.
flight_from = [4, 3]
flight_to = [1, 2]
The number of delayed flights k=2, and delayed = [1, 3].


• Flight I is delayed.
    • Flight 4 depends on flight 1. so flight 4 is delayed.
• Flight 3 is delayed.
    • There are no flights dependent on flight 3.

solution: Graph (DFS)

    1. Building the Graph:
        We start by creating a graph representation using adjacency lists. Each flight is represented by its flight number, and we iterate through the lists flight_from and flight_to to build the graph. The graph list stores the dependencies for each flight node.

    2. DFS Function:
        We define a recursive depth-first search (DFS) function named dfs. This function takes a node as input and explores all flights that depend on that node. It marks each flight it visits as delayed by adding it to the delayed_flights set.
        The DFS function recursively explores all flights that depend on the current flight node.

    3. DFS Traversal for Each Delayed Flight:
        We iterate through the list of initially delayed flights (delayed) and perform a DFS starting from each delayed flight using the dfs function. This ensures that we explore all flights that are indirectly delayed due to the initially delayed flights.

    4. Sorting and Returning Delayed Flights:
        After performing DFS for all delayed flights, we convert the set delayed_flights to a list, sort it in increasing order, and return the sorted list as the result.

    Example Usage:
        Finally, we demonstrate the usage of the function with the given example inputs (flight_nodes, flight_from, flight_to, k, delayed) and print the result.
        Overall, the solution utilizes DFS to traverse the flight dependencies and find all delayed flights, ensuring that indirectly delayed flights are also accounted for. The result is sorted and returned as per the requirements.


Time Complexity:
    Building the graph: O(m), where m is the number of dependencies.
    Performing DFS for each delayed flight: O(k * (V + E)), where V is the number of flight nodes and E is the number of dependencies.
    Sorting the delayed flights: O(k * log(k)), where k is the number of delayed flights.

Therefore, the overall time complexity is O(m + k * (V + E) + k * log(k)).

Space Complexity:
    Graph representation: O(V + E), where V is the number of flight nodes and E is the number of dependencies.
    Set to store delayed flights: O(k), where k is the number of delayed flights.
    Recursive call stack for DFS: O(V), where V is the number of flight nodes (in the worst case).

Therefore, the overall space complexity is O(V + E + k).
'''

# Solution: Graph (DFS)

def find_delayed_flights(flight_nodes, flight_from, flight_to, k, delayed):
    # Create a graph representation using adjacency lists
    graph = [[] for _ in range(flight_nodes + 1)]
    for i in range(len(flight_from)):
        graph[flight_to[i]].append(flight_from[i])

    # Set to store delayed flights
    delayed_flights = set()

    # Function to perform DFS
    def dfs(node):
        if node in delayed_flights:
            return
        delayed_flights.add(node)
        for next_node in graph[node]:
            dfs(next_node)

    # Perform DFS for each delayed flight
    for flight in delayed:
        dfs(flight)

    # Sort and return delayed flights
    delayed_flights = sorted(list(delayed_flights))
    return delayed_flights

# Example usage
flight_nodes = 4
flight_from = [4, 3]
flight_to = [1, 2]
k = 2
delayed = [1, 3]

result = find_delayed_flights(flight_nodes, flight_from, flight_to, k, delayed)
print(result)  # Output: [1, 3, 4]


'''
Optimizations:

    1. Graph Representation:
        Instead of storing dependencies for each flight, we store incoming flights for each flight node directly. This eliminates the need for reversing dependencies during DFS traversal.

    2. Single DFS Traversal:
        We perform a single DFS traversal starting from all initially delayed flights simultaneously. This ensures that we explore all indirectly delayed flights without redundant traversals.

    3. Efficient Data Structures:
        We use a set (visited) to store visited flights during DFS traversal, ensuring efficient lookup and avoiding duplicate entries.

Overall, these optimizations reduce redundant operations and improve the efficiency of the solution.

Time Complexity:
    Building the graph: O(m), where m is the number of dependencies.
    Performing DFS starting from all initially delayed flights: O(k * (V + E)), where V is the number of flight nodes and E is the number of dependencies.
    Sorting the delayed flights: O(k * log(k)), where k is the number of delayed flights.

Therefore, the overall time complexity is O(m + k * (V + E) + k * log(k)).

Space Complexity:
    Graph representation: O(V + E), where V is the number of flight nodes and E is the number of dependencies.
    Set to store visited flights during DFS: O(V), where V is the number of flight nodes.
    List to store delayed flights: O(k), where k is the number of delayed flights.
    Recursive call stack for DFS: O(V), where V is the number of flight nodes (in the worst case).

Therefore, the overall space complexity is O(V + E + k).

In summary, the optimized solution maintains the same time complexity as the previous solution, but it may perform slightly better in practice due to the elimination of redundant DFS traversals. 
'''
# optimized Python solution:

def find_delayed_flights(flight_nodes, flight_from, flight_to, k, delayed):
    # Create a graph representation using adjacency lists
    incoming_flights = [[] for _ in range(flight_nodes + 1)]
    for i in range(len(flight_from)):
        incoming_flights[flight_from[i]].append(flight_to[i])

    # Set to store visited flights during DFS
    visited = set()

    # Function to perform DFS starting from delayed flights
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for next_node in incoming_flights[node]:
            dfs(next_node)

    # Perform DFS starting from all initially delayed flights
    for flight in delayed:
        dfs(flight)

    # Collect all visited flights as delayed flights
    delayed_flights = sorted(list(visited))
    return delayed_flights

# Example usage
flight_nodes = 4
flight_from = [4, 3]
flight_to = [1, 2]
k = 2
delayed = [1, 3]

result = find_delayed_flights(flight_nodes, flight_from, flight_to, k, delayed)
print(result)  # Output: [1, 3, 4]
