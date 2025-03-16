# Problem 2: First Missing Positive

def first_missing_positive(nums):
    nums = set(nums)
    i = 1
    while i in nums:
        i += 1
    return i

# Examples
print(first_missing_positive([1,2,0]))  # Output: 3
print(first_missing_positive([3,4,-1,1]))  # Output: 2
print(first_missing_positive([7,8,9,11,12]))  # Output: 1



# Explanation
# I convert the input list to a set for faster lookup.
# I start with the value 1 and increment it until I find the first missing positive integer.
# I return the first missing positive integer.
# The time complexity of this solution is O(n) since we iterate through the list once.
# The space complexity is O(n) due to the set used to store the input list.