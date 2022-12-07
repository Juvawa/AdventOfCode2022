import pickle


if __name__ == '__main__':
    input = []
    result = 0
    file = open('input.txt', 'rb')
    for line in file.readlines():
        number = line.decode('utf-8').strip()
        if number != '':
            result = result + int(number)
        else:
            input.append(result)
            result = 0
    print(input)
    print(sorted(input, reverse=True)[:3])
    print(sum(sorted(input, reverse=True)[:3]))




