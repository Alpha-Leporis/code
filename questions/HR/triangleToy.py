'''
In the assembly line, the factory assembles three parts 'a' 'b' 'c' of a triangle toy. 
A valid toy is one where the two shorter sides added together are greater in length than the longest side.

There are two forms of valid triangles to identify.

• If 2 parts are of equal length, the form is 'Isosceles'
• If all 3 parts are of equal length, the form is 'Equilateral'

If a toy is not valid or is not one of those 2 forms, it is 'None of these'

Example:
triangleToy=['2 2 1', '3 3 3', '3 4 5', '1 1 3']

• the first valid and has 2 equal parts. so the form is 'Isosceles'
• the second valid and has 3 equal parts, so the form is 'Equilateral'
• the third is valid but not one of the two specific forms.
• the fourth is not  valid, The two sides of 1 unit length cannot  meet if the third side is 3 units.
• the result is ['Isosceles','Equilateral', 'None of these', 'None of these']
'''

# solution:
'''
we can iterate through the list of triangle toy specifications and check each one to determine its form. 
We'll parse each specification to get the lengths of the three sides, then apply the conditions for 
an equilateral triangle, an isosceles triangle, or none of these.

In this code:
    1. The identify_triangle_forms function takes a list of triangle toy specifications as input.
    2. It iterates through each specification and parses it to get the lengths of the three sides.
    3. It sorts the sides in ascending order to easily check for equilateral and isosceles triangles.
    4. It checks the conditions for an equilateral triangle, an isosceles triangle, or none of these.
    5. It appends the determined form to the forms list.
    6. Finally, it returns the list of forms for all triangle toy specifications.

time complexity is O(n), where n is the number of triangle toy specifications.
space complexity is O(n)
'''

def identify_triangle_forms(triangleToy):
    forms = []
    for spec in triangleToy:
        sides = list(map(int, spec.split()))
        sides.sort()  # Sort the sides to easily check for equilateral and isosceles triangles
        if sides[0] + sides[1] > sides[2]:  # Check if it's a valid triangle
            if sides[0] == sides[1] == sides[2]:  # All sides are equal
                forms.append('Equilateral')
            elif sides[0] == sides[1] or sides[1] == sides[2]:  # Two sides are equal
                forms.append('Isosceles')
            else:
                forms.append('None of these')
        else:
            forms.append('None of these')
    return forms

# Example usage:
triangleToy = ['2 2 1', '3 3 3', '3 4 5', '1 1 3']
forms = identify_triangle_forms(triangleToy)
print(forms)


# optimized soluton:
'''
We can optimize the solution by directly checking the conditions for an equilateral triangle 
and an isosceles triangle without sorting the sides. This way, we avoid unnecessary sorting 
operations and simplify the code.

This optimized solution directly checks the conditions for an equilateral triangle and 
an isosceles triangle based on the input sides without sorting them. It simplifies the code
and avoids unnecessary sorting operations, resulting in improved efficiency.

time complexity is O(n), where n is the number of triangle toy specifications.
space complexity is O(n)
'''
