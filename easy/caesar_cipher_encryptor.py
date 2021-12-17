# O(n^2) Time, O(n) Space
def caesarCipherEncryptorBad(string, key):
    # Write your code here.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = {}
    for idx, char in enumerate(alphabet):
        alphabet_dict[char] = idx

    new_string = ""
    for char in string:
        keys = [k for k, v in alphabet_dict.items() if v ==
                (alphabet_dict[char] + (key)) % 26]
        new_string += str(keys[0])
    return new_string

# Time O(n), Space O(1)


def caesarCipherEncryptor(string, key):
    new_string = ""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for char in string:
        new_string += getNewLetter(char, key, alphabet)
    return new_string


def getNewLetter(char, key, alphabet):
    new_index = (alphabet.index(char) + key)
    return alphabet[new_index % 26]


string = "xyz"
key = 2
print(caesarCipherEncryptor(string, key))
