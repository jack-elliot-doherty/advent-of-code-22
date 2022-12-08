def is_visible(tree_map, tree_row, i, j):

    right = True
    top = True
    bottom = True
    left = True
    k = j + 1

    while k < len(tree_row):
        if tree_row[k] >= tree_row[j]:
            print("invisible from right")
            right = False
            break
        k += 1

    k = j - 1
    while -1 != k:
        if tree_row[k] >= tree_row[j]:
            print("invisible from left")
            left = False
            break
        k -= 1

    k = i + 1
    while k < len(tree_map):
        if tree_map[k][j] >= tree_row[j]:
            print("invisible from bottom")
            bottom = False
            break
        k += 1
    
    k = i - 1
    while -1 != k:
        if tree_map[k][j] >= tree_row[j]:
            print("invisible from top")
            top = False
            break
        k -= 1

    return (right or left or top or bottom)



with open("input.txt", "r") as f:


    tree_map = []
    lines = f.readlines()
    for line in lines:
        row = []
        for ch in line.strip():
            row.append(int(ch))
        tree_map.append(row)

    print(tree_map)


    visible_trees = 0

    for i in range(len(tree_map)):
        tree_row = tree_map[i]
        for j in range(len(tree_row)):
            if i == 0 or i == len(tree_map) - 1:
                print("i: ", i, "j: ", j, "visible")
                visible_trees +=1
            elif j == 0 or j == len(tree_row) - 1:
                print("i: ", i, "j: ", j, "visible")
                visible_trees +=1
            elif is_visible(tree_map, tree_row, i, j):
                print("i: ", i, "j: ", j, "visible here")
                visible_trees +=1
            else:
                print("i: ", i, "j: ", j, "not visible")
        
    print(visible_trees)

