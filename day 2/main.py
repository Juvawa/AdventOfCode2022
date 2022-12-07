'''A = steen
B = papier
C = schaar
X = steen 1
Y = papier 2
Z = schaar 3
verlies = 0
gelijk = 3
winst = 6'''

scenarios ={
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6,
}

if __name__ == '__main__':
    file = open('input.txt', 'r')
    result = 0
    for line in list(file.readlines()):
        result += scenarios[line.strip().replace(' ', '')]

    print(result)


