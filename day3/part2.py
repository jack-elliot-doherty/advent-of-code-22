with open("input.txt") as f:
    lines = f.readlines()
    common_elements = []
    for i in range(2,len(lines),3):
        badge = set(lines[i].strip()).intersection(set(lines[i-1].strip())).intersection(set(lines[i-2].strip()))
        common_elements += list(badge)

total = 0
for element in common_elements:
    if element.isupper():
        print(element, "added", ord(element) - 64)
        total += ord(element) - 38
    else:
        print(element, "added", ord(element) - 96)
        total += ord(element) - 96
    
print(total)