import collections

def print_stacks(stack_dict):
    for k,v in sorted(stack_dict.items(), key=lambda x: x):
        print("Stack {}: {}".format(k, v))

with open("input.txt") as f:
    lines = f.read()

    stacks, moves = lines.split("\n\n")

    stacks_dict = collections.defaultdict(list)

    stacks = stacks.split("\n")[::-1]
    stacks = stacks[1:]
    for line in stacks:
        index = 9
        line = line.strip("\n")

        for i in range(len(line) -2, 0, -4):
            if line[i] != " ":
                stacks_dict[index].append(line[i])
            index -= 1

    for move in moves.split("\n"):
        move = move.split()

        print(move)

        moved = stacks_dict[int(move[3])][-int(move[1]):]
        stacks_dict[int(move[3])] = stacks_dict[int(move[3])][:-int(move[1])]
        stacks_dict[int(move[-1])] += moved

        print_stacks(stacks_dict)



items = (sorted(stacks_dict.items(), key=lambda x: x))

print("".join([x[1][-1] for x in items]))
