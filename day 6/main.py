if __name__ == '__main__':
    file = open('input.txt', 'r')
    line = file.readline()
    result = 0

    for i, c in enumerate(line):
        substring = line[i:i+4]
        doubled = False
        for char in substring:
            if substring.count(char) > 1:
                doubled = True
                break

        if doubled is False:
            print(i+4)
            break