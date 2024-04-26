'''
A Domain Name System (DNS) translates domain
names to IP addresses which are then used by
browsers to load internet resources. For quicker
DNS lookups, browsers often store a number of
recent DNS queries in a DNS cache. Retrieving data
from the cache is often faster than retrieving it
from a DNS server. This task aims to simulate DNS
resolution and determine the time taken to process
different URLs.

Assume that the DNS cache can store a maximum
of the cache_size most recent DNS requests, i.e.,
URL-IP mappings. The cache is initially empty. It
takes cache_time units of time to fetch data from
the DNS cache, and server_time units of time to
fetch data from the DNS server.

Given a list of n URLs visited as an array of strings,
urls, determine the minimum time taken to resolve
each DNS request.

Note: New DNS requests are dynamically added to
'''

# solution:

'''
To solve this problem in Python, we can simulate the DNS resolution process by maintaining
a cache to store the URL-IP mappings. We'll iterate through the list of URLs and check if 
the URL is present in the cache. If it is, we'll retrieve the IP address from the cache. 
Otherwise, we'll fetch the IP address from the DNS server and update the cache.

In this implementation:
    1. We initialize an empty dictionary cache to simulate the DNS cache.
    2. We iterate through each URL in the list of URLs.
    3. If the URL is present in the cache, we add the cache_time to the total time.
    4. If the URL is not present in the cache, we add the server_time to the total time and update the cache with the URL-IP mapping.
    5. If the size of the cache exceeds the cache_size, we remove the oldest entry from the cache.
    6. Finally, we return the total time taken for DNS resolution.

time complexity: O(n)
space complexity: O(cache_size), for the cache and O(1) for other variables.
'''

from collections import deque

def get_time_in_cache(urls, cache_size, cache_time, server_time):
    time_taken = []
    queue = deque()
    cache_set = set()

    for url in urls:
        if url in cache_set:
            time_taken.append(cache_time)
        else:
            if len(queue) >= cache_size:
                front_url = queue.popleft()
                cache_set.remove(front_url)
            
            time_taken.append(server_time)
            queue.append(url)
            cache_set.add(url)
            #time_taken.append(server_time)
    
    return time_taken


# Example usage:
urls = ["google.com", "example.com", "google.com", "facebook.com"]
cache_size = 2
cache_time = 2
server_time = 3
result = get_time_in_cache(urls, cache_size, cache_time, server_time)
print("Minimum time taken for DNS resolution:", result)



# optimized solution:

'''
To optimize the solution, we can use a data structure that allows for efficient lookup and 
removal of the oldest entry when the cache size exceeds the limit. 
We can achieve this by using a combination of OrderedDict and deque from the collections module in Python. 
OrderedDict will allow us to maintain the insertion order of URLs in the cache, 
while deque will allow us to efficiently remove the oldest entry when needed

In this optimized implementation:
    1. We use an OrderedDict cache to simulate the DNS cache, which maintains the insertion order of URLs.
    2. When accessing a URL in the cache, we update the total time and move the URL to the end of the OrderedDict to maintain its freshness.
    3. When adding a new URL to the cache, we update the total time and add the URL-IP mapping to the OrderedDict.
    4. If the cache size exceeds the maximum limit, we remove the oldest entry from the cache using popitem(last=False) to efficiently remove the first entry.
    5. This optimized solution ensures efficient lookup, insertion, and removal operations in the cache, leading to improved performance compared to the previous solution.
time complexity: O(n)
space complexity: O(cache_size), for the cache and O(1) for other variables.
'''

from collections import OrderedDict, deque

def minDNSResolutionTime(urls, cache_size, cache_time, server_time):
    cache = OrderedDict()  # Initialize an empty cache (OrderedDict)
    total_time = 0  # Initialize total time counter

    for url in urls:
        if url in cache:
            # If URL is in the cache, fetch IP address from cache
            total_time += cache_time
            # Move the URL to the end of the OrderedDict to maintain its freshness
            cache.move_to_end(url)
        else:
            # If URL is not in the cache, fetch IP address from DNS server
            total_time += server_time

            # Update cache with URL-IP mapping
            cache[url] = True

            # If cache size exceeds the maximum limit, remove the oldest entry
            if len(cache) > cache_size:
                # Remove the oldest entry from the cache
                oldest_url = cache.popitem(last=False)[0]

    return total_time

# Example usage:
urls = ["google.com", "example.com", "google.com", "facebook.com"]
cache_size = 2
cache_time = 5
server_time = 10
result = minDNSResolutionTime(urls, cache_size, cache_time, server_time)
print("Minimum time taken for DNS resolution:", result)


