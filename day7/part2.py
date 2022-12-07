import collections


with open("input.txt", "r") as f:

    commands = f.readlines()
    dir_sizes = collections.defaultdict(int)
    path = []
    for command in commands:
        command_parts = command.strip().split()
        if command_parts[1] == "cd":
            if command_parts[2] == "..":
                path.pop()
            else:
                path.append(command_parts[2])
        elif command_parts[1] == "ls":
            continue
        else:
            try:
                size = int(command_parts[0])
                for i in range(len(path) + 1):
                    dir_sizes["/".join(path[:i])] += size
            except:
                pass


    total_space = 70000000
    space_needed = 30000000
    unused_space = total_space - dir_sizes["/"]
    space_to_delete = space_needed - unused_space

    dir_that_could_make_the_space = []
    for k,v in dir_sizes.items():
        if v > space_to_delete:
            dir_that_could_make_the_space.append(v)

    print(min(dir_that_could_make_the_space))

