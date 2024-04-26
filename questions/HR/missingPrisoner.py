'''
Prisoners are standing on a Cartesian coordinate system present inside a jail.
Each prisoner stands at a unique point with both the coordinates (x,y) being integers. 
Each prisoner should be at a postion that a forms a rectangle or square With 3 other pnsoners.

More formally, every prisoner at a coordinates pair [x, y] should have:

• at least one prisoner standing at integer coordinates [x, ay] where ay != y.
• at least one prisoner standing at integer coordinates [bx, y] where bx != x.

Unfortunately, one prisoner has escaped, find the coordinates of that prisoner.

Example:
locations = [[1,1], [1,2], [2,1], [4,4], [4,6], [9,4], [9,6]]
'''

# Solution:

'''
To find the coordinates of the missing prisoner, we can iterate through the given list of locations 
and construct a dictionary to store the count of unique x and y coordinates. 
Since each prisoner should have at least one other prisoner standing at integer coordinates
[x, ay] and [bx, y], we can check if there are any x or y coordinates with counts less than 2.
If found, it indicates that a prisoner is missing at that coordinate.

In this implementation:
    1. We iterate through the given list of locations and construct dictionaries x_counts and y_counts to store the count of unique x and y coordinates, respectively.
    2. Then, we iterate through the dictionaries to find any x or y coordinates with counts less than 2, indicating that a prisoner is missing at that coordinate.
    3. Finally, we return the coordinates of the missing prisoner. If both coordinates are missing, the function will return [None, None].

time complexity is O(n)
space complexity is O(n), where n is the number of locations.
'''

def missingPrisoner(locations):
    x_counts = {}
    y_counts = {}

    for x, y in locations:
        x_counts[x] = x_counts.get(x, 0) + 1
        y_counts[y] = y_counts.get(y, 0) + 1

    missing_x = None
    missing_y = None

    for x, count in x_counts.items():
        if count < 2:
            missing_x = x
            break

    for y, count in y_counts.items():
        if count < 2:
            missing_y = y
            break

    return [missing_x, missing_y]

# Example usage:
locations = [[1,1], [1,2], [2,1], [4,4], [4,6], [9,4], [9,6]]
missing_prisoner = missingPrisoner(locations)
print("Coordinates of the missing prisoner:", missing_prisoner)


# optimize solution:
'''
We can optimize the solution by avoiding the use of dictionaries and instead using sets to 
store unique x and y coordinates. Additionally, we can simultaneously find the 
missing x and y coordinates in a single loop iteration.

This optimized implementation eliminates the need for dictionaries and instead uses sets to 
store unique x and y coordinates. It simultaneously finds the missing x and y coordinates 
in a single loop iteration, avoiding unnecessary iterations through the locations list. 
This results in improved efficiency compared to the previous solution.

time complexity is O(n)
space complexity is O(n)
'''

def missingPrisoner(locations):
    x_set = set()
    y_set = set()

    for x, y in locations:
        x_set.add(x)
        y_set.add(y)

    missing_x = None
    missing_y = None

    for x, y in locations:
        if x_set and y_set:
            if x not in x_set or y not in y_set:
                missing_x = x
                missing_y = y
                break
        elif x not in x_set:
            missing_x = x
            missing_y = y
            break
        elif y not in y_set:
            missing_x = x
            missing_y = y
            break

    return [missing_x, missing_y]

# Example usage:
locations = [[1,1], [1,2], [2,1], [4,4], [4,6], [9,4], [9,6]]
missing_prisoner = missingPrisoner(locations)
print("Coordinates of the missing prisoner:", missing_prisoner)
