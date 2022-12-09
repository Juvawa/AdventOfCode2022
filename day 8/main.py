import numpy as np

if __name__ == '__main__':
    data = open('input.txt', 'r').readlines()
    forest = np.asarray([list(line.strip()) for line in data])
    height, width = forest.shape
    visible_trees = 0

    for y in range(height):
        for x in range(width):
            focust_tree = forest[y][x]
            row = forest[y]
            column = forest[:, x]
            if all(tree < focust_tree for tree in row[:x]) or \
                    all(tree < focust_tree for tree in row[x + 1:]) or \
                    all(tree < focust_tree for tree in column[:y]) or \
                    all(tree < focust_tree for tree in column[y + 1:]):
                visible_trees += 1

    print(visible_trees)