with open("input.txt") as f:

    monkeys = f.read().split("\n\n")

    Items = []
    Ops = []
    Tests = []
    Trues = []
    Falses = []

    for monkey in monkeys:
        _id, items, ops, test, true, false = monkey.split("\n")

        # print(test, true, false)

        Items.append([int(item) for item in items.split(": ")[1].split(", ")])
        ops = ops.split("=")[1]

        Ops.append(lambda old,ops=ops:eval(ops))
        Tests.append(int(test.split(" ")[-1]))
        Trues.append(int(true.split(" ")[-1]))
        Falses.append(int(false.split(" ")[-1]))
    
    lcm = 1
    for i in range(len(Items)):
        lcm *= Tests[i]
    print(lcm)



    inspects = [0 for _ in range(len(Items))]
    for _ in range(10000):

        for i in range(len(Items)):
            while len(Items[i]) > 0:
                Items[i][0] = (Ops[i](Items[i][0])) % lcm
                inspects[i] += 1
                if Items[i][0] % (Tests[i]) == 0:
                    Items[Trues[i]].append(Items[i].pop(0))
                else:
                    Items[Falses[i]].append(Items[i].pop(0))




    inspects = sorted(inspects, reverse=True)
    print(inspects[0] * inspects[1])
