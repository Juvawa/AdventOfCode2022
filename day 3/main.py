def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


if __name__ == '__main__':
    file = open('input.txt', 'r')
    resultlist = []
    result = []
    for line in list(file.readlines()):
        line = list(line.strip())
        half = int(len(line) / 2)
        resultlist.append(intersection(line[:half], line[half:]))

    print(resultlist)
    flat_resultlist = [item for sublist in resultlist for item in sublist]
    print(len(flat_resultlist))

    for char in flat_resultlist:
        if char.isupper():
            result.append(ord(char) - 38)
        elif char.islower():
            result.append(ord(char) - 96)
    print(len(result))
    print(sum(result))

