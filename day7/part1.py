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

    ans = 0
    for k,v in dir_sizes.items():
        if v <= 100000:
            ans += v
    print(ans)
