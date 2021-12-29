def isMonotonic(array):
    increasing = sorted(array)
    decreasing = sorted(array, reverse=True)

    if array == increasing or array == decreasing:
        return True
    return False


def isMonotonic2(array):
    if array == []:
        return True
    increasing = 0
    decreasing = 0
    length = len(array) - 1
    for i in range(1, len(array)):
        if array[i] >= array[i-1]:
            increasing += 1
        if array[i] <= array[i-1]:
            decreasing += 1
    if increasing == length or decreasing == length:
        return True
    return False
    # return [increasing, decreasing, length, decreasing == length]


array = [-1, -2, -3, -4]
print(isMonotonic2(array))
