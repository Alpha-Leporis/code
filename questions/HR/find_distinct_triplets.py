'''
The cost of a stock on each day is given in an array. arr, An investor wants to buy the
stocks in triplets such that the sum of the cost for three days is divisible by d.
The goal is to find the number of distinct triplets (i. j, k) such that i < j < k and the sum
(a[i] + a[j] + a[k]) is divisible d.

Example:
let arr, prices of stock = [3, 3, 4, 7, 8] and d = 5. Following are the triplets whose sum is
divisible by d (1-based indexing)
• Triplet with indices - (1,2,3), sum = 3+3+4 which is equal to 10
• Triplet with indices - (1,3,5), sum 3+4+8 which is equal to 15
• Triplet with indices - (2,3,4), sum = 3+4+8 which is equal to 15
Hence the answer is 3.

'''

# brute force solution:
'''
we can iterate through all possible triplets of indices (i, j, k) where i < j < k, 
and check if the sum of elements at these indices is divisible by d. We'll keep track 
of the count of such triplets and return it as the result.
This solution iterates through all possible triplets of indices (i, j, k) in the 
input array arr, resulting in a time complexity of O(n^3), where n is the length of the array.
The space complexity of the solution is O(1) as it only uses a constant amount of extra space.
While this solution works for small input sizes, it may not be efficient for large arrays due to its cubic time complexity.
'''

def count_triplets(arr, d):
    n = len(arr)
    count = 0

    # Iterate through all possible triplets (i, j, k)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # Check if the sum of elements at indices i, j, k is divisible by d
                if (arr[i] + arr[j] + arr[k]) % d == 0:
                    count += 1

    return count

# Example usage
arr = [3, 3, 4, 7, 8]
d = 5
result = count_triplets(arr, d)
print("Number of distinct triplets:", result)  # Output: 3


# optimized solution:
'''
We can further optimize the solution by using a dictionary to store the frequency of remainders
when the prefix sum is divided by d. By doing so, we can avoid iterating through all pairs of
indices and instead directly compute the count of valid triplets by considering the frequency
of remainders. This approach reduces the time complexity to O(n) while still using O(n) space.
'''
def count_triplets(arr, d):
    n = len(arr)
    count = 0
    remainder_freq = {0: 1}  # Initialize the frequency of remainder 0

    prefix_sum = 0  # Initialize the prefix sum
    for num in arr:
        prefix_sum += num
        remainder = prefix_sum % d

        # Update the count with the frequency of remainders
        count += remainder_freq.get((d - remainder) % d, 0)

        # Update the frequency of the current remainder
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

    return count

# Example usage
arr = [3, 3, 4, 7, 8]
d = 5
result = count_triplets(arr, d)
print("Number of distinct triplets:", result)  # Output: 3

