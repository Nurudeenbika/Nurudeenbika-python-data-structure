# Problem 1: Move Zeros to the End

def move_zeros(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return nums

# Examples
print(move_zeros([0,1,0,3,12]))  # Output: [1,3,12,0,0]
print(move_zeros([0,0,1]))  # Output: [1,0,0]
print(move_zeros([4,2,4,0,0,3,0,5,1,0]))  # Output: [4,2,4,3,5,1,0,0,0,0]



# Explanation
# I maintain an index that points to the position where the next non-zero element should be placed.
# I iterate through the array and swap the current element with the element at the index.
# I increment the index only when a non-zero element is encountered.
# This way, all non-zero elements are moved to the front of the array, and zeros are moved to the end.
# The time complexity of this solution is O(n) since we iterate through the array once.
# The space complexity is O(1) since we do not use any extra space.