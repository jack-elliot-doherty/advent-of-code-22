def write_crt():
    if ((cycles - 1) % 40) in {xval - 1, xval, xval + 1}:
        current_line.append("#")
    else:
        current_line.append(".")

with open("input.txt") as f:
    lines = f.readlines()

    cycles = 0

    xval = 1
    screen_lines = []
    current_line = []
    for i, line in enumerate(lines):
        line = line.strip()

        cycles += 1


        write_crt()

        if cycles % 40 == 0:
            screen_lines.append(current_line)
            current_line = []

        if line != "noop":
            addx = int(line.split(" ")[1])


            cycles += 1
            write_crt()

            if cycles % 40 == 0:
                screen_lines.append(current_line)
                current_line = []

            xval += addx

for line in screen_lines:
    print("".join(line))