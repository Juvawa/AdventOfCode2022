from itertools import islice
import re

if __name__ == '__main__':
    with open("input.txt") as myfile:
        stacks = [list(line.strip()) for line in list(islice(myfile, 9))]
        moves = [re.findall(r'\d+', line) for line in myfile.readlines()[:]]
    print(stacks)
    print(moves)

    # move 3 from 8 to 2
    for move in moves:
        for i in range(int(move[0])):
            popped = stacks[int(move[1]) - 1].pop()
            stacks[int(move[2]) - 1].append(popped)

    result = ""
    for stack in stacks:
        result += stack.pop()
    print(result)