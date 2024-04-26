
# Write a program to find the sum of A.P series
'''
Algorithm:

Sum of arithmetic series is ((n / 2) * (2 * a + (n - 1) * d))
           Where
               a is First term
               d is Common difference
               n is No of terms
TC = O(1)
SC = O(1)
'''

def sum_of_ap(first_term, common_diff, num_terms):
    # Calculate the sum of the A.P series
    sum_ap = (num_terms * (2 * first_term + (num_terms - 1) * common_diff)) // 2 # Calculating the Sum
    return sum_ap # Returning the Sum

# Example usage:
first_term = int(input("Enter the first term of the A.P series: "))
common_diff = int(input("Enter the common difference of the A.P series: "))
num_terms = int(input("Enter the number of terms in the A.P series: "))

print("The sum of the A.P series is:", sum_of_ap(first_term, common_diff, num_terms))

'''
This program calculates the sum of an A.P series using the formula:
Sum=n/2 * (2a+(n−1)d)
Where:
    nn is the number of terms,
    aa is the first term, and
    dd is the common difference.
'''