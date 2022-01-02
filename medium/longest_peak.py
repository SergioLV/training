def longestPeak(array):
    length = len(array) - 2
    longestPeak = 0
    leftIdx = 0
    rightIdx = 1
    if len(array) <= 2:
        return 0

    while rightIdx <= length:
        if array[rightIdx] > array[rightIdx - 1] and array[rightIdx] > array[rightIdx + 1]:
            b = searchLength(array[rightIdx + 1:])
            c = searchLength(array[rightIdx-1::-1])
            if b+c+1 > longestPeak:
                longestPeak = b+c+1
        rightIdx += 1
    return longestPeak


def searchLength(array):
    length = 1
    for i in range(1, len(array)):
        if array[i] < array[i-1]:

            length += 1
        else:
            return length
    return length


def searchLeftLength(array):
    length = 1
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            length += 1
        else:
            return length
    return length


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# array = [1, 2, 3, 4, 5, 1]
print(longestPeak(array))
