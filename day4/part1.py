def is_contained(first_elf_start, first_elf_end, second_elf_start, second_elf_end):
    if first_elf_start in range(second_elf_start, second_elf_end + 1) and first_elf_end in range(second_elf_start, second_elf_end + 1):
            return True
    elif second_elf_start in range(first_elf_start, first_elf_end + 1) and second_elf_end in range(first_elf_start, first_elf_end + 1):
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

        if is_contained(int(first_elf_start), int(first_elf_end), int(second_elf_start), int(second_elf_end)):
            total_contained += 1
        

print(total_contained)

