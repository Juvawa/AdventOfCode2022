'''A = steen
B = papier
C = schaar
X = lose 1
Y = draw 2
Z = win 3
verlies = 0
gelijk = 3
winst = 6'''

scenarios ={
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7
}

if __name__ == '__main__':
    file = open('input.txt', 'r')
    result = 0
    for line in list(file.readlines()):
        result += scenarios[line.strip().replace(' ', '')]

    print(result)


