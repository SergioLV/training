def isPalindromeBad(string):
    reversed = ""
    string_len = len(string)-1
    for i in range(string_len, -1, -1):
        reversed += string[i]
    return reversed == string


def isPalindrome(string):
    left = 0
    right = len(string) - 1
    isPalindrome = False

    while not isPalindrome:
        if left == right or (left + 1 == right and string[left] == string[right]):
            return True
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False


string = "aba"
print(isPalindrome(string))
