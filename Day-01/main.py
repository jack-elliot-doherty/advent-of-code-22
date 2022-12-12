with open("input.txt", "r") as f:

    fattest_elf = 0
    all_elves_cals = []
    sub_total = 0
    for line in f.readlines():
        print(line)
        if line.strip() == "":
            print('new elf')
            all_elves_cals.append(sub_total)
            sub_total = 0    
            
        else:
            sub_total += int(line.strip())

all_elves_cals.append(sub_total)

fattest = max(all_elves_cals)
all_elves_cals.remove(fattest)
fatter = max(all_elves_cals)
all_elves_cals.remove(fatter)
fat = max(all_elves_cals)

print(fattest + fatter + fat)