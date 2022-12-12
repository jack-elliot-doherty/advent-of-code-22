with open("input.txt", "r") as f:
    string = f.read().strip()

    for i in range(4, len(string)):
        last_4_chars = set(string[i-4:i])
        if len(last_4_chars) == 4:
            print(i)
            break
