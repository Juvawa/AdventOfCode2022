def intersection(lst):
    return list(set(lst[0]) & set(lst[1]) & set(lst[2]))


if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    triplets = []
    i = 0
    for line in range(int(len(lines)/3)):
        triplets.append(lines[i:i+3])
        i += 3

    result = []
    for triplet in triplets:
        result.append(intersection(triplet))

    num_res = []
    for char in result:
        if char[0].isupper():
            num_res.append(ord(char[0]) - 38)
        elif char[0].islower():
            num_res.append(ord(char[0]) - 96)
    print(sum(num_res))

