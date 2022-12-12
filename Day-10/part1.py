def is_instersting_cycle(cycles, interesting_cycles):
    if cycles in interesting_cycles:
        signal_strenghts.append(cycles * xval)

with open("input.txt") as f:
    lines = f.readlines()

    cycles = 0
    interesting_cycles = {20,60,100,140,180,220}

    signal_strenghts = []

    xval = 1

    for line in lines:
        line = line.strip()

        cycles += 1

        if line != "noop":
            addx = int(line.split(" ")[1])

            is_instersting_cycle(cycles, interesting_cycles)

            cycles += 1
            is_instersting_cycle(cycles, interesting_cycles)

            xval += addx
        else:
            is_instersting_cycle(cycles, interesting_cycles)

print(sum(signal_strenghts))