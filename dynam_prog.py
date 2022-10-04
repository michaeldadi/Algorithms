# Kadane's algorithm
def max_sum_subarray(arr):
    n = len(arr)
    max_sum = -1e8

    for i in range(0, n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(current_sum, max_sum)

    return max_sum
