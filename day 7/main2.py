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

    total_size_filesystem = 70000000
    needed_update_space = 30000000

    current_free_space = total_size_filesystem - root.size
    nodes = findall(root, lambda node: node.size >= (needed_update_space - current_free_space))
    resultlist = []
    for node in nodes:
        resultlist.append(node.size)

    print(min(resultlist))