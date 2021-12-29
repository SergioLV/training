def moveElementToEnd(array, toMove):
    occurences = 0
    result = [numbers for numbers in array if numbers != toMove]

    for number in array:
        if number == toMove:
            occurences += 1
    for i in range(occurences):
        result.append(toMove)

    return result


def moveElementToEnd2(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:
        if array[leftIdx] == toMove and array[rightIdx] == toMove:
            rightIdx -= 1
        elif array[leftIdx] == toMove and array[rightIdx] != toMove:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
            leftIdx += 1
            rightIdx -= 1
        else:
            leftIdx += 1
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd2(array, toMove))
