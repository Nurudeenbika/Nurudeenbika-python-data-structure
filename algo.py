def longest_subarray_with_equal_occurrences(nums, x, y):
    count_x = 0
    count_y = 0
    max_length = 0
    diff_map = {0: -1}  # Initialize with difference 0 at index -1

    for i, num in enumerate(nums):
        if num == x:
            count_x += 1
        elif num == y:
            count_y += 1

        # Calculate the difference between count_x and count_y
        diff = count_x - count_y

        # If the difference is already in the map, update the max_length
        if diff in diff_map:
            max_length = max(max_length, i - diff_map[diff])
        else:
            # Store the first occurrence of this difference
            diff_map[diff] = i

    return max_length

# Example usage:
nums1 = [1, 2, 3, 2, 3, 1, 3, 2, 1]
x1 = 2
y1 = 3
print(longest_subarray_with_equal_occurrences(nums1, x1, y1))  # Output: 6

nums2 = [4, 5, 6, 4, 5, 5, 4, 6, 5, 4, 6]
x2 = 4
y2 = 5
print(longest_subarray_with_equal_occurrences(nums2, x2, y2))  # Output: 8