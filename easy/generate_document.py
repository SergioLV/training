def generateDocument(characters, document):
    # Write your code here.
    goal = len(characters)-1
    sum = 0
    for idx, char in enumerate(document):
        if characters.count(char) >= document.count(char):
            sum += 1
    print(sum, goal)
    return sum == goal


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))
