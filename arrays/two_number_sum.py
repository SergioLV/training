# Problem Statement

# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
# If no two numbers sum up to the target sum, the function should return an empty array.
# Assume that there will be at most one pair of numbers summing up to the target sum.

# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 Sample output: [-1, 11]


# Naive approach, O(n^2) time and O(1) space
def two_number_sum_naive(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i]+arr[j] == target and arr[i] != arr[j]):
                return sorted([arr[i], arr[j]])

    return []


# O(n), O(n)
def two_number_sum(arr, target):
    for i in range(len(arr)):
        target_sum = target - arr[i]
        sec_array = arr[i+1:len(arr)]
        if(target_sum in sec_array):
            return sorted([target_sum, arr[i]])
    return []


arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(two_number_sum(arr, target))
