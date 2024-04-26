'''
One of the shops in HackerMalI Offering
discount coupons based on a puzzling
problem. There are n tags where each tag
has a value denoted by val[i].
A customer needs to choose the lags in 
such a way that the sum of values is even.

The goal is to find the maximum possible
even sum of values of tags thatcan be
chosen.

Note:
• It is guaranteed that there is at least one
tag with an even value.
• The tags can have positive or negative value.
'''
# Solution:

'''
Time complexity: O(n), where n is the length of the array.
Space complexity: O(1)
'''

def getMaximumEvenSum(arr):
    pos_sum = 0
    # Calculate the sum of all the possible elements of the
    for num in arr:
        if num > 0:
            pos_sum += num
    # if the sum of positive elements is even, then return it
    if pos_sum % 2 == 0:
        return pos_sum
    # find the maximum even sum by modifying the odd positive elements
    ans = float('-inf')
    for num in arr:
        if num % 2 != 0:
            if num > 0:
                ans = max(ans, pos_sum - num)
            else:
                ans = max(ans, pos_sum + num)
    return ans

arr = [-1, -2, -3, 8, 7]
print(getMaximumEvenSum(arr)) # Output = 14