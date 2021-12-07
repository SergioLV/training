
# O(n) Time, O(1) Space
def isValidSubsequence(array, sequence):
    for i in range(len(array)):
        if sequence == []:
            break
        if array[i] == sequence[0]:
            del sequence[0]
    if sequence == []:
        return True
    return False
