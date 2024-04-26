'''
Given n request ids as an array of strings,
requests, and an integer k. after all requests are
received, find the k most recent requests. Report
the answer in order of most recent to least recent.

Example:
Suppose n = 5, requests= ["item1", "item2", "item3",
"item1", "item3"], and k = 3.

Starting from the right and moving left, collecting
distinct requests, there iS "item3" followed by
"item1". Skip the second Instance of "Item3" and
find "item2". The answer is ["item3", "item1",
"item2"].

Function Description
Complete the function getLatestKRequests

'''

'''
To solve this problem , we can use a deque (double-ended queue) to
efficiently maintain the k most recent requests.

In this code:
    1. We use a deque called recent_requests to maintain the k most recent requests. We set the maximum length of the deque to k so that it automatically discards older requests when new ones are added.
    2. We also use a set called seen to keep track of distinct requests encountered so far.
    3. We iterate through the requests list in reverse order (from the end to the beginning).
    4. For each request, if it's not in the seen set, we prepend it to the recent_requests deque and add it to the seen set.
    5. Finally, we convert the deque to a list and return it as the k most recent requests.

This solution efficiently finds the k most recent requests while preserving their order from most recent to least recent.

time complexity is O(n), where n is the number of requests
space complexity is O(n + k), where n is the number of requests, deque has maximum length of k
'''

from collections import deque

def getLatestKRequests(requests, k):
    recent_requests = deque(maxlen=k)
    seen = set()
    for request in reversed(requests):
        if request not in seen:
            recent_requests.appendleft(request)
            seen.add(request)
    return list(recent_requests)

# Example usage:
requests = ["item1", "item2", "item3", "item1", "item3"]
k = 3
latest_requests = getLatestKRequests(requests, k)
print("The k most recent requests:", latest_requests)


# optimized solution
'''
To optimize the solution, we can eliminate the need for the seen set and improve the time complexity
by directly using a deque to store the most recent requests while ensuring uniqueness. 
We can achieve this by modifying the logic to append requests to the deque only if they are not already present in it.

In this optimized solution:
    1. We still use a deque called recent_requests to maintain the k most recent requests. The maximum length of the deque is set to k.
    2. We iterate through the requests list in reverse order (from the end to the beginning).
    3. For each request, if it's not already in the deque, we prepend it to the deque and add it to the seen set to ensure uniqueness.
    4. We return the list representation of the deque as the k most recent requests.

This optimized solution eliminates the need for the seen set and directly ensures uniqueness within the deque. It improves the time complexity by avoiding redundant set lookups.

time complexity is O(n), where n is the number of requests
space complexity is O(k) because we use a deque to store at most k recent requests, where k is the maximum number of recent requests to be maintained.
'''

from collections import deque

def getLatestKRequests(requests, k):
    recent_requests = deque(maxlen=k)
    seen = set()
    for request in reversed(requests):
        if request not in seen:
            recent_requests.appendleft(request)
            seen.add(request)
    return list(recent_requests)

# Example usage:
requests = ["item1", "item2", "item3", "item1", "item3"]
k = 3
latest_requests = getLatestKRequests(requests, k)
print("The k most recent requests:", latest_requests)

