import collections


def move_tail(head, tail):
    """If the head is ever two steps directly up, down, left, or right from the tail,
    the tail must also move one step in that direction so it remains close enough
    Otherwise, if the head and tail aren't touching and aren't in the same row or column,
    the tail always moves one step diagonally to keep up"""


    if not check_if_on_same_row_and_column(head, tail):
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1

        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
        print("tail moving diagonally", tail)

    elif head[0] - tail[0] == 2:
        tail[0] += 1
        print("tail moving right", tail)
    elif head[0] - tail[0] == -2:
        tail[0] -= 1
        print("tail moving left", tail)
    elif head[1] - tail[1] == 2:
        tail[1] += 1
        print("tail moving up", tail)
    elif head[1] - tail[1] == -2:
        tail[1] -= 1
        print("tail moving down", tail)

    return tail

def check_if_on_same_row_and_column(head, tail):
    return head[0] == tail[0] or head[1] == tail[1]


def calculate_moves(direction, steps, knots, tail_position_count):

    head = knots[0]

    for i in range(steps):
    
        if direction == "R":
            knots[0][0] += 1
        elif direction == "L":
            knots[0][0] -= 1
        elif direction == "U":
            knots[0][1] += 1
        elif direction == "D":
            knots[0][1] -= 1
        
        for i in range(9):
            head = knots[i]
            tail = knots[i + 1]


            if not is_touching(head, tail):
                tail = move_tail(head, tail)
                print(tail)
                tail_position_count[i + 1].append(tuple(tail))

def is_touching(head,tail):
    """returns true if the tail and head are touching (diagonally adjacent and even overlapping both count as touching)"""
    return abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1

with open("input.txt", "r") as f:

    lines = f.readlines()

    knots = {
        0: [0,0],
        1: [0,0],
        2: [0,0],
        3: [0,0],
        4: [0,0],
        5: [0,0],
        6: [0,0],
        7: [0,0],
        8: [0,0],
        9: [0,0],
    }
    tail_position_count = collections.defaultdict(list)
    # x x x x
    # x x T x
    # x H x x
    # x x x x
    for line in lines:
        line = line.strip().split()
        direction, steps = line[0], int(line[1])
        print(direction, steps)
        
        calculate_moves(direction, steps, knots, tail_position_count)

print(len(set(tail_position_count[9])) + 1)

# pos = 3
# 4 x x x x x
# 3 x x x x x  
# 2 x x x x x
# 1 x x x x x
# 0 x T H x x
#   0 1 2 3 4
# r = 2

# H = [2,0]
# T = [0,1]