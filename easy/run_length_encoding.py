

def runLengthEncoding(string):
    new_string = ""
    start = 0

    for idx, char in enumerate(string):
        if new_string.count(char) == 0:
            new_string += formatString(char, string.count(char))
        else:
            continue
    return new_string


def formatString(char, count):
    formatted_string = ""
    if count > 9:
        formatted_string +=

    return str(count) + str(char)


# string = "AAAAAAAAAAAAABBCCCCDD"
string = "AAAAABBCCCEEE"
print(runLengthEncoding(string))
