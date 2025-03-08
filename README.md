## Explanation

### Initialization  
I start by initializing `count_x` and `count_y` to zero and a hashmap `diff_map` with a key `0` mapped to `-1`.  
This helps in handling the case where the subarray starts from the beginning of the array.  

### Iteration  
As we iterate through the array, we update the counts of `x` and `y`.  
I then calculate the difference between these counts.  

### Tracking  
- If the difference has been seen before, it means that the subarray between the previous index (stored in the hashmap) and the current index has an equal number of `x` and `y`.  
- I update `max_length` if this subarray is longer than the previously recorded one.  

### Edge Case Handling  
If the difference is zero, it means that from the start of the array to the current index, the counts of `x` and `y` are equal.  

### Complexity  
This approach ensures that we efficiently find the longest subarray with equal occurrences of `x` and `y` in **O(n)** time complexity, which is optimal for the given constraints.  
