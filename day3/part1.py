with open("input.txt") as f:
    lines = f.readlines()
    common_elements = []
    for line in lines:
        line = line.strip()
        compartment1 = line[:(len(line)//2)]
        compartment2 = line[(len(line)//2):]
        common_elements += list(set(compartment1).intersection(compartment2))

total = 0
for element in common_elements:
    if element.isupper():
        print(element, "added", ord(element) - 64)
        total += ord(element) - 38
    else:
        print(element, "added", ord(element) - 96)
        total += ord(element) - 96
    
print(total)