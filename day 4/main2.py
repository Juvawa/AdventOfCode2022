if __name__ == '__main__':
    file = open('input.txt', 'r')
    list_of_tuples = [[range(int(line.split('-')[0]), int(line.split('-')[1]) + 1) for line in x.strip().split(',')] for x in file.readlines()]

    number_of_pairs = 0
    for range1, range2 in list_of_tuples:
        if len(set(range1).intersection(range2)) > 0:
            number_of_pairs += 1

    print(number_of_pairs)
