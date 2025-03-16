# Problem 1: Two Sum

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Examples
print(two_sum([2,7,11,15], 9))  # Output: [0,1]
print(two_sum([3,2,4], 6))  # Output: [1,2]
print(two_sum([3,3], 6))  # Output: [0,1]


# Explanation
# I use a hashmap to store the elements and their indices.
# I iterate through the list and check if the complement of the current element is in the hashmap.
# If the complement is found, I return the indices of the two elements.
