# Problem 1: Fibonacci Sequence (Top-Down Approach)
# Problem Statement:
# Compute the nth Fibonacci number using Dynamic Programming.

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Example Usage
print("Fibonacci(10):", fibonacci(10))


# Output
# Fibonacci(10): 55


# Explanation
# I use a top-down approach to compute the nth Fibonacci number.
# I store the results of subproblems in a dictionary to avoid redundant calculations.
# The time complexity of this solution is O(n) since we compute each Fibonacci number once.