def is_monotonic(array):
    # Check if the array is non-decreasing
    is_non_decreasing = all(array[i] <= array[i + 1] for i in range(len(array) - 1))
    
    # Check if the array is non-increasing
    is_non_increasing = all(array[i] >= array[i + 1] for i in range(len(array) - 1))
    
    # Return True if either condition is met
    return is_non_decreasing or is_non_increasing

# Test cases
print(is_monotonic([1, 2, 3, 4, 5]))   # True (non-decreasing)
print(is_monotonic([5, 4, 3, 2, 1]))   # True (non-increasing)
print(is_monotonic([1, 3, 2, 5, 4]))   # False
print(is_monotonic([1, 1, 1, 1, 1]))   # True (all elements are equal)
