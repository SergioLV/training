def solution(array, target):
    # Tiempo O(nlogn), Espacio O(1)
    before = array
    array.sort()
    left_idx = 0
    right_idx = len(array) - 1

    while right_idx > left_idx:
        if array[left_idx] + array[right_idx] > target:
            right_idx -= 1
        elif array[left_idx] + array[right_idx] < target:
            left_idx += 1
        else:
            return [left_idx, right_idx, before, array]


array = [4, 5, 7, 3, 9, 43, 65, -1, -4, -6]
target = 12
print(solution(array, target))
