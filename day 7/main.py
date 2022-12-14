from bigtree import Node, findall, print_tree

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = [line.strip().replace('$ ', '') for line in file.readlines()]
    root = Node("/", size=0, directory="/")
    currentNode = root
    for line in lines:
        command = line.split(' ')
        if command[0] == "ls":
            continue
        elif command[0] == "cd":
            if command[1] == "..":
                currentNode = currentNode.parent
            else:
                for node in currentNode.children:
                    if node.directory == command[1]:
                        currentNode = node
                        break
        elif command[0].isnumeric():
            currentNode.size += int(command[0])
            tempnode = currentNode
            while tempnode.parent:
                tempnode = tempnode.parent
                tempnode.size += int(command[0])

        elif command[0] == "dir":
            Node(command[1], size=0, parent=currentNode, directory=command[1])

    resultList = findall(root, lambda node: node.size <= 100000)
    result = 0
    for node in resultList:
        result += node.size

    print(result)