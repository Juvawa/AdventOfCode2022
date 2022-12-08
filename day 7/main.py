from bigtree import Node, find, findall, print_tree, find_children, find_full_path

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

    print_tree(root, attr_list=["size"])
    resultList = findall(root, lambda node: node.size <= 100000)
    result = 0
    for node in resultList:
        result += node.size

    print_tree(root, attr_list=["size"])

    print(result)



















    #     command = line.split(' ')
    #     if command[0] == "cd":
    #         if command[1] == "..":
    #             current_cwd.pop()
    #         elif command[1] == '/':
    #             filesizes["".join(current_cwd) + command[1]] = 0
    #         else:
    #             current_cwd.append(command[1])
    #     elif command[0] == "dir":
    #          filesizes["".join(current_cwd)+command[1]] = 0
    #     elif command[0].isnumeric():
    #         key = "".join(current_cwd)
    #         if key not in filesizes:
    #             filesizes[key] = int(command[0])
    #         else:
    #             filesizes[key] += int(command[0])
    #         if len(current_cwd) > 1:
    #             length = len(current_cwd)
    #             for i in range(length-1):
    #                 key2 = ''.join(current_cwd[:length-i-1])
    #                 if key2 in filesizes:
    #                     filesizes[key2] += int(command[0])
    # result = 0
    # for key in filesizes.keys():
    #     if filesizes[key] <= 100000:
    #         result += filesizes[key]
    #
    # print(result)



