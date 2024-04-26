
'''
Given a number N. Find the minimum number of operations required to reach N starting from 0.
You have 2 operations available:
    a. Double the number
    b. Add one to the number

Approch: This function uses dynamic programming to calculate the minimum number of operations required to reach each number from 0 up to N.
It considers two operations: doubling the number and adding one to the number.
Finally, it returns the minimum number of operations required to reach N.

Time Complexity: O(N), where N is the given number.
Space Complexity: O(N) because we use a list of size N+1 to store the minimum number of operations 
                required to reach each number from 0 to N.

'''

def min_operations_to_N(N):
    # Create a list to store the minimum number of operations to reach each number
    dp = [0] * (N + 1)

    # Start from 1 since we already know it will take 1 operation to reach 1 from 0
    for i in range(1, N + 1):
        # Initialize the minimum operations for the current number to a large value
        dp[i] = float('inf')

        # Check if doubling the previous number results in the current number
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # Add one operation to the previous number to reach the current number
        dp[i] = min(dp[i], dp[i - 1] + 1)

    # Return the minimum operations required to reach N
    return dp[N]

# Example usage:
N = 10
print("Minimum number of operations to reach", N, ":", min_operations_to_N(N))
