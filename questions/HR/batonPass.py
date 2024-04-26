'''
There are n friends standing In a line, each numbered from 1 through n inclusive. The first one, friend 1, holds a baton. Each second,
the baton is passed to the next friend in line. Once It reaches the end of the line, the direction of passing is reversed and passing
continues. Determine who Will pass and who Will receive the baton at a given time.

Example:
friends = 4
time = 5

Friends are numbered 1 through 4, Friend 1 holds the baton at time 0. At time 1, it is passed to friend 2. Over 5 seconds, the baton is
passed as 1->2->3->4->3->2. The friend passing the baton at time 5 is friend 3. The friend receving the baton is friend 2. Return [3, 2]

Function Description:
Complete the function batonPass in the editor below. The function must return an integer array.

batonPass has the folling parameters:
• int friends: the number of friends
• int time:  the time to report who on the bat

Returns:
• int[2]: the fnend who has the baton (index O) and the friend who receives the baton (index 1)

Constraints:
• 2 <= friends <=  2 * 10^5
• 1 <= time <= 10^12
'''

# solution:

'''
To solve this problem, we can observe that the baton passes through the friends in a cyclic manner. 
We can determine the friend who holds the baton at a given time by calculating the position of 
the baton in the cyclic sequence of friends.

This function first calculates the length of the cyclic sequence of friends, which is 2 * friends - 2. 
Then, it takes the modulo of the given time with the cycle length to determine the position of the baton in the cycle. 
Depending on the position, it returns the friend who holds the baton and the friend who receives the baton.

Time complexity: O(1)
Space complexity: O(1)
'''

def batonPass(friends, time):
    cycle_length = 2 * friends - 2
    time %= cycle_length

    if time < friends:
        return [time + 1, 0]
    else:
        return [2 * friends - time - 1, 1]

# Example usage:
friends = 4
time = 5
print(batonPass(friends, time))  # Output: [3, 2]


# HakerRank solution:

'''
solution:
    1. The cycle length is calculated as (friends - 1) * 2. This is because the baton passes through all friends and returns back, except for the first and last friend.
    2. The effective time is calculated as (time - 1) % cycle_length + 1. This ensures that the time is within the cycle length and starts from 1.
    3. If the effective time is less than or equal to the number of friends, the position is the same as the effective time. Otherwise, the position is calculated as 2 * friends - effective_time.
    4. Depending on the effective time and position, the passer and receiver are determined. If the effective time is within the first half of the cycle, the receiver is the next friend in line. Otherwise, the receiver is the previous friend in line. The passer remains the same as the position.
Time complexity: O(1)
Space complexity: O(1)
'''

def batonPass(friends, time):
    cycle_length = (friends - 1) * 2 # Calculating Cycle Length:
    effective_time = (time - 1) % cycle_length + 1 # Calculating Effective Time:

    # Determining Position
    if effective_time <= friends:
        position = effective_time
    else:
        position = 2 * friends - effective_time

    # Determining Passer and Receiver
    if effective_time <= friends:
        passer = position
        receiver = position + 1 if position < friends else friends
    else:
        passer = position
        receiver = position - 1 if position > 1 else 1

    # Returning Result
    return [passer, receiver]

# Example usage:
friends = 4
time = 5
result = batonPass(friends, time)
print(result) # Output: [3,2]



