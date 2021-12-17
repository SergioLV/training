def bubbleSortBad(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] <= array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def bubbleSort(array):
    isSorted = False
    counter = 0

    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
        counter += 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]

print(bubbleSortBad(array))
print(bubbleSort(array))
