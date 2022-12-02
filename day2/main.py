
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
        my_throw = ord(throws[1]) - 23

        if elf_throw == my_throw:
            # draw
            print("draw", mappings[elf_throw], mappings[my_throw], my_throw)
            tot_score += 3 + (my_throw - 64)

        elif my_throw - elf_throw == 1 or my_throw - elf_throw == -2:
            # win
            print("win", mappings[elf_throw], mappings[my_throw], my_throw)
            tot_score += 6 + (my_throw - 64)


        else:
            # lose 
            print("lose", mappings[elf_throw], mappings[my_throw], my_throw)
            tot_score += (my_throw - 64)

print(tot_score)