# Binary search True if finds the target
def binarySearch(array, target):
    mid = len(array)//2
    if mid == 0:
        return False
    # print(array)
    if array[mid] == target:
        return True
    if array[mid] > target:
        return binarySearch(array[:mid], target)
    elif array[mid] < target:
        return binarySearch(array[mid:], target)
    # print(mid)


def binarySearchIndex(array, target):
    if array == []:
        return -1
    else:
        return binarySearchIndexHelper(array, target, 0, len(array)-1)


def binarySearchIndexHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearchIndexHelper(array, target, mid+1, right)
    elif array[mid] > target:
        return binarySearchIndexHelper(array, target, left, mid-1)


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

print(binarySearchIndex(array, target))
