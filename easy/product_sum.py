def productSum(array):
    if array != []:
        return productSumHelper(array, 1)
    else:
        return 0


def productSumHelper(array, depth):
    sum = 0
    for elem in array:
        if type(elem) == list:
            sum += productSumHelper(elem, depth+1)
        else:
            sum += elem
    return sum * depth


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# print(type(array) == list)
print(productSum(array))
# Recorrer el array.
# Ver si el elemento es un arreglo
# Recorrer el array
# ver si el elemento es un arreglo
