'''
1. Tracks in Hackathon

There a hackathon by HackerRank
which has 2 separate tracks. healthcare and e-commerce. 
For track 1, the required team size
teamSize_1, while for track 2, the required team
size is teamSize_2. The total number of participants is p.

Find the minimum number of teams into which the
participants can be divided such that each
participant belongs to exactly one team (either of
track 1 or track 2), and each team has a size equal to
either teamSize_1 or teamSize_2. If no such drwsaon
is possible, return -1.

Example
Consider teamSize_1 = 3, teamSize_2 = 4 and
number of participants p = 7.

Optimally there is 1 team of 3 and 1 team of 4. The
mininum number Of teams is 2.

Function Description:
Complete the function countTeams.
The function countTeams has the following parameters:
• teamSize_1 - total number of participents in team 1
• teamSize_2 - total number of participents in team 2
• p - total number of participents

Returns:
the minimum number of teams into which the 
participents can be divided.

Constraints
• 1 <= teamSize_1 >= 10^5
• 1 <= teamSize_2 >= 10^5
• 1 <= p >= 10^5

'''

# Solution:

'''
To solve this problem, we need to find the minimum number of teams into which 
the participants can be divided such that each participant belongs to exactly one team, 
and each team has a size equal to either teamSize_1 or teamSize_2. We can approach this 
problem by iterating through possible team compositions and checking if it satisfies the conditions.

This function iterates through the possible number of teams for track 1 (num_team_1) and 
calculates the remaining participants. If the remaining participants can be evenly divided 
into teams for track 2, it calculates the number of teams for track 2 (num_team_2). 
Finally, it returns the minimum number of teams required to accommodate all participants or -1 if it's not possible.

time complexity: O(p / teamSize_1).
space complexity: O(1), constant space.
'''

def countTeams(teamSize_1, teamSize_2, p):
    min_teams = float('inf')

    for num_team_1 in range(p // teamSize_1 + 1):
        remaining_participants = p - num_team_1 * teamSize_1
        if remaining_participants % teamSize_2 == 0:
            num_team_2 = remaining_participants // teamSize_2
            min_teams = min(min_teams, num_team_1 + num_team_2)

    return min_teams if min_teams != float('inf') else -1

# Example usage:
teamSize_1 = 3
teamSize_2 = 4
p = 6
print(countTeams(teamSize_1, teamSize_2, p))  # Output: 2
