def does_overlap(first_elf_start, first_elf_end, second_elf_start, second_elf_end):
    
    first_elf = set(range(first_elf_start, first_elf_end + 1))
    second_elf = set(range(second_elf_start, second_elf_end + 1))

    overlaps = first_elf.intersection(second_elf)

    if len(overlaps) > 0:
        return True
    return False

# 2-8,2,6

with open("input.txt", "r") as f:
    lines = f.readlines()


    total_contained = 0
    for line in lines:
        elf_pair = line.strip().split(",")
        first_elf_start, first_elf_end = elf_pair[0].split("-")
        second_elf_start, second_elf_end = elf_pair[1].split("-")

        if does_overlap(int(first_elf_start), int(first_elf_end), int(second_elf_start), int(second_elf_end)):
            total_contained += 1
        

print(total_contained)

