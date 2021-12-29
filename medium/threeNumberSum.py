def threeNumberSum(array, targetSum):
    # array.sort()
    result = []
    for idx, num in enumerate(array):
        target = targetSum - num
        aux = twoNumberSum(array[idx+1:], target)
        if aux == []:
            continue
        else:
            aux2 = [num] + aux
            aux2.sort()
            result.append(aux2)
    result.sort()
    return result


# O(n^2) Time, O(n) space
def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        target = targetSum - array[i]
        remainder = array[i+1:]
        if target in remainder:
            return [array[i], target]
    return []


array = [1, 2, 3]
targetSum = 6
print(threeNumberSum(array, targetSum))
