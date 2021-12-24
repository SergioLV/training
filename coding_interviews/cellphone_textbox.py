# Given a phone number and an array of words, return the words of the array
# that are contained in the phone number transformed to letters.

# 1 (800) 356 9377 -> 1 (800) flowers
# 253 6368 -> clement or clemdot or...

# 0	none (on some telephones, "OPERATOR" or "OPER")
# 1	none (on some older telephones, QZ)
# 2	ABC
# 3	DEF
# 4	GHI
# 5	JKL
# 6	MNO (on some older telephones, MN)
# 7	PQRS (on older telephones, PRS)
# 8	TUV
# 9	WXYZ (on older telephones, WXY)

# So, the 2 contains [a,b,c] ans 23 contains [a,b,c], [d,e,f], [ad,ae,af] and so on.

# The best solution I that i can think for the moment, is to translate the array into
# numbers and after that, check if the numbers contains the translation.

# Input phoneNumber = "3662277", words =["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]
#output ["bar", "cap", "car", "emo","foo","foobar"]

def validWords(phoneNumber, array):
    # phonepad = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl",
    #             6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    phonepad = {'a': '2', 'b': '2', 'c': '2',
                'd': '3', 'e': '3', 'f': '3',
                'g': '4', 'h': '4', 'i': '4',
                'j': '5', 'k': '5', 'l': '5',
                'm': '6', 'n': '6', 'o': '6',
                'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8',
                'u': '8', 'w': '9', 'v': '8',
                'w': '9', 'x': '9', 'y': '9', 'z': '9'}
    translated = []
    result = []

    for word in array:
        translation = ""
        for char in word:
            translation += phonepad[char]
        translated.append([word, translation])

    for word in translated:
        if word[1] in phoneNumber:
            result.append(word[0])
    result.sort()

    return result


print(validWords("3662277", ["foo", "bar", "baz",
      "foobar", "emo", "cap", "car", "cat"]))
