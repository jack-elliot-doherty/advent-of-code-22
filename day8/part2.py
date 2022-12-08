def get_scenic_score(tree_map, tree_row, i, j):

    right = 0
    top = 0
    bottom = 0
    left = 0
    k = j + 1

    while k < len(tree_row):
        right += 1
        if tree_row[k] >= tree_row[j]:
            break
        k += 1

    k = j - 1
    while -1 != k:
        left += 1
        if tree_row[k] >= tree_row[j]:
            break
        k -= 1


    k = i + 1
    while k < len(tree_map):
        bottom += 1
        if tree_map[k][j] >= tree_row[j]:
            break
        k += 1
    
    k = i - 1
    while -1 != k:
        top += 1
        if tree_map[k][j] >= tree_row[j]:
            break
        k -= 1

    return (right * left * top * bottom)



with open("input.txt", "r") as f:


    tree_map = []
    lines = f.readlines()
    for line in lines:
        row = []
        for ch in line.strip():
            row.append(int(ch))
        tree_map.append(row)

    print(tree_map)


    scenic_scores = []

    for i in range(len(tree_map)):
        tree_row = tree_map[i]
        for j in range(len(tree_row)):
            
            scenic_scores.append(get_scenic_score(tree_map, tree_row, i, j))
        
    print(max(scenic_scores))

