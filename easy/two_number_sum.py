# Naive approach, O(n^2) time and O(1) space
def twoNumberSumNaive(array, targetSum):
    # Write your code here.
    if array == []:
        return []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if(array[i] + array[j] == targetSum):
                return [array[i], array[j]]
    return []


# O(n^2) time, O(n) space.
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)):
        resto = targetSum - array[i]
        remainder = array[i+1:len(array)]
        if(resto in remainder):
            return [target, array[i]]
    return []

    


arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
twoNumberSum(arr, target)
