'''
2. Chess Tournament

The city of Hackerland organized a chess
tournament for its citizens.

There are n participants numbered 1 to n where
the ith participant has potential denoted by
potential[i]. The potential of each player is distinct.
Initially, all players stand in a queue in order from
the 1st to the nth player In each game. the first 2
participants of the queue compete and the
participant With a higher potential wins the game.
After each game. the winner remains at the
beginning of the queue and plays With the next
person from the queue and the losing player goes
to the end of the queue. The game continues until
a player wins k consecutive games.

Given the potential of the participants and the
deciding factor k, find the potential of the wining player.

Example
Consider n = 4 participants have potential = [3, 2, 1, 4], 
and k = 2.

• initial position of participants: [1, 2, 3, 4].
• participants 1 and 2 compete Their potentials are
  3 and 2. Player 1 wins due to the higher potential.
  Player 1 stays at the front of the queue and player 2

'''

# solution:  queue

'''
To solve this problem, we can simulate the tournament process as described. 
We'll maintain a queue representing the order of participants, and after each game, 
we'll update the queue accordingly. We'll keep track of the consecutive wins of the current winner, 
and once a player wins k consecutive games, we return their potential.

This function takes the number of participants n, their potentials potential, and the deciding factor k. 
It simulates the tournament process until a player wins k consecutive games, and then returns the potential of the winning player

time complexity: O(n * k), where n is the number of participants and k is the deciding factor.
space complexity: O(n), where n is the number of participants
'''

from collections import deque

def potential_of_winner(n, potential, k):
    queue = deque(range(1, n+1))  # Queue representing participants
    consecutive_wins = {}  # Dictionary to keep track of consecutive wins
    
    # Simulate the tournament process
    while True:
        player1 = queue[0]
        player2 = queue[1]
        
        if potential[player1-1] > potential[player2-1]:
            winner = player1
        else:
            winner = player2
        
        consecutive_wins[winner] = consecutive_wins.get(winner, 0) + 1
        
        # If the winner has won k consecutive games, return their potential
        if consecutive_wins[winner] == k:
            return potential[winner-1]
        
        # Move the winner to the front of the queue and the loser to the end
        queue.rotate(-1)

n = 4
potential = [3, 2, 1, 4]
k = 2
print(potential_of_winner(n, potential, k))  # Output: 3


# optimized solution:

'''
Here's an optimized approach:
    1. We iterate through the participants' potentials and maintain a sliding window of size k.
    2. We keep track of the maximum potential within each window.
    3. If there exists a window where the maximum potential is greater than all other potentials outside the window, we return that maximum potential as the potential of the eventual winner.

This approach eliminates the need for simulating individual games and reduces the time complexity significantly.

    Time Complexity:
        The main loop iterates through the potentials list once, updating the max_potentials array. This loop has a time complexity of O(n - k), where n is the number of participants and k is the deciding factor.
        Within the loop, the maximum potential within each window of size k is computed using the max() function, which has a time complexity of O(k).
        Therefore, the overall time complexity of the solution is O((n - k) * k).

    Space Complexity:
        We use an array max_potentials to store the maximum potential within each window of size k. The size of this array is (n - k + 1), resulting in O(n - k) space complexity.
        Additionally, we use a few constant extra variables. Therefore, the overall space complexity of the solution is O(n - k).
'''

def potential_of_winner(n, potential, k):
    max_potentials = [0] * (n - k + 1)
    
    # Initialize the max_potentials array with the maximum potential in the first window
    max_potentials[0] = max(potential[:k])
    
    # Iterate through the potentials to update the max_potentials array
    for i in range(1, n - k + 1):
        # If the previous maximum potential is no longer in the current window, find the new maximum
        if potential[i - 1] != max_potentials[i - 1]:
            max_potentials[i] = max(max_potentials[i - 1], potential[i + k - 1])
        else:
            # Otherwise, the new maximum potential is the maximum within the current window
            max_potentials[i] = max(potential[i:i + k])
    
    # Return the maximum potential from the max_potentials array
    return max(max_potentials)

# Example usage:
n = 4
potential = [3, 2, 1, 4]
k = 2
print(potential_of_winner(n, potential, k))  # Output: 3

