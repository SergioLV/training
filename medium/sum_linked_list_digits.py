# The LL 1 -> 3 -> 4 -> None represents the number 431
# Sum 2 LL that represents a number like that.
# The weird version is long and it take too much memory. Adding zeros to the shorter list and then sum
# the values is a way of solving the problem, but is not the best way to do it. I think it is a good approach
# but is not as efficient as I would like. I feel that doing this in an interview is not the right thing to do.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfTwoWeird(linkedListOne, linkedListTwo):
    first_list_length = getLinkedListLength(linkedListOne)
    second_list_length = getLinkedListLength(linkedListTwo)

    if first_list_length < second_list_length:
        shorter = first_list_length
        larger = second_list_length
    elif first_list_length > second_list_length:
        shorter = second_list_length
        larger = first_list_length
    elif first_list_length == second_list_length:
        shorter = 0
    difference = larger - shorter
    formated_shorter = addZeros(shorter, difference)


def getLinkedListLength(linkedList):
    length = 0
    current = linkedList

    while current != None:
        length += 1
        current = current.next
    return length


def addZeros(linkedList, zeros):
    current = linkedList
    while zeros > 0:
        if current.next is None:
            current.next = LinkedList(0)
            current = current.next
            zeros -= 1
        else:
            current = current.next
    return linkedList


def sumOfLinkedLists(linkedListOne, linkedListTwo):


a = LinkedList(1)
a.next = LinkedList(2)
b = addZeros(a, 3)

current = b
while current != None:
    print(current.value)
    current = current.next
