with open("input.txt", "r") as f:
    string = f.read().strip()

    for i in range(14, len(string)):
        last_4_chars = set(string[i-14:i])
        if len(last_4_chars) == 14:
            print(i)
            break
