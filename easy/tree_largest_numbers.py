def findThreeLargestNumbers(array):
    if len(array) == 3:
        array.sort()

        return array
    result = array[:3]
    for i in range(3, len(array)):
        aux = replaceMaxValue(result, array[i])
        if aux != result:
            result = aux
    return aux


def replaceMaxValue(result, value):
    result.sort()
    for idx, num in enumerate(result):
        if value > num:
            result.pop(idx)
            result.append(value)
            break
    return result


array = [55, 7, 8, 3, 43, 11]

print(findThreeLargestNumbers(array))
