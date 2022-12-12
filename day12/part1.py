import sys
from collections import deque
infile = sys.argv[1]
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

G = []
for line in lines:
    G.append(line)
rows = len(G)
cols = len(G[0])

elevations = [[0 for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        if G[row][col]=='S':
            elevations[row][col] = 1
        elif G[row][col] == 'E':
            elevations[row][col] = 26
        else:
            elevations[row][col] = ord(G[row][col])-ord('a')+1

def bfs():
    Q = deque()
    for r in range(rows):
        for c in range(cols):
            if G[r][c]=='S':
                Q.append(((r,c), 0))

    visited = set()
    while Q:
        (r,c),d = Q.popleft()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        if G[r][c]=='E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<rows and 0<=cc<cols and elevations[rr][cc]<=1+elevations[r][c]:
                Q.append(((rr,cc),d+1))
print(bfs())