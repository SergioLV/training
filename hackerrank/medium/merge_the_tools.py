def mergeTheTools(string, k):
    chunks = [string[i:i+k] for i in range(0, len(string), k)]
    for elem in chunks:
        aux = set(elem)
        result = ''.join(aux)
        print(result)


string = "AABCAAADA"
k = 3
print(mergeTheTools(string, k))
