
mappings = {
    65: "rock",
    66: "paper",
    67: "scissors"
}

with open("input.txt", "r") as f:

    tot_score = 0
    for line in f.readlines():

        throws = line.strip().split()

        elf_throw = ord(throws[0])
        outcome = ord(throws[1]) - 23

        if outcome == 65:
            # lose
            my_throw = elf_throw + 2
            if elf_throw == 66:
                my_throw = 65
            elif elf_throw == 67:
                my_throw = 66
            print("lose", mappings[elf_throw], mappings[my_throw])
            tot_score += ((my_throw) - 64)

        elif outcome == 66:
            # draw
            print("draw", mappings[elf_throw], mappings[elf_throw])
            tot_score += 3 + (elf_throw - 64)


        else:
            # win 
            my_throw = elf_throw + 1
            if elf_throw == 67:
                my_throw = 65
            print("win", mappings[elf_throw], mappings[my_throw])
            tot_score += + 6  + (my_throw - 64)

print(tot_score)
