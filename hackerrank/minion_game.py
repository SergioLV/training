# The solution I gave to this problem is the approach. Even if it works, the approach is too slow.
# This works only if I want to know a brute force solution.
# A better approach is to know all the possible substrings in a string of length n.
# (n-1) + (n-2) + ... or n*(n+1)/2.
def minionGame(string):
    string = string.lower()
    stuart_points = pointsWithConsonants(string)
    kevin_points = pointsWithVowels(string)
    if stuart_points > kevin_points:
        return 'Stuart ' + str(stuart_points)
    return 'Kevin ' + str(kevin_points)


def pointsWithConsonants(string):
    consonants = 'qwrtypsdfghjklzxcvbnm'
    posible_words = []
    left = 0
    right = 0
    i = 0

    while i < len(string):
        if string[i] in consonants:
            left = i
            right = i
            while right <= len(string):
                posible_words.append(string[left:right])
                right += 1
        left += 1
        i += 1
    score = calculateScore(string, posible_words)

    return score


def pointsWithVowels(string):
    vowels = 'aeiou'
    posible_words = []

    left = 0
    right = 0
    i = 0

    while i < len(string):
        if string[i] in vowels:
            left = i
            right = i
            while right <= len(string):
                posible_words.append(string[left:right])
                right += 1
        left += 1
        i += 1
    score = calculateScore(string, posible_words)

    return score


def calculateScore(string, posible_words):
    word_count = {}
    score = 0
    for word in posible_words:
        if word != '':
            word_count[word] = 0
    for word in posible_words:
        if word != '':
            word_count[word] += 1

    for key in word_count.keys():
        score += word_count[key]

    return score


string = 'BANAASA'
print(minionGame(string))
