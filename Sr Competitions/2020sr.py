# # question 1
# N = int(input())
# data = []

# for i in range(N):
#     temp = input().split()
#     temp[0] = int(temp[0])
#     temp[1] = int(temp[1])
#     data.append(temp)

# data.sort()

# fastest = float('-inf')

# for i in range(N-1):
#     diffT = data[i+1][0] - data[i][0]
#     diffD = data[i+1][1] - data[i][1]
#     if abs(diffD/diffT) > fastest:
#         fastest = abs(diffD/diffT)

# print(fastest)

# question 2
# use breadth first search for adjacency

# steps
# 1. set up - take inputs, convert to ints, make grid (2d arr)
# 2. do bfs from top left corner and if we arrive at bottom right corner in any instance, output yes
# if bfs is done and bottom right corner never reached, output no

# deciding "neighbours"
# factors of curr are (r,c) for neighbours
# check if in bounds/ is valid
# use 2D arr to store neighbours of each cell

# M = int(input())
# N = int(input())

room = []
# end = M*N

# for i in range(M):
#     temp = input().split()
#     temp = [int(i) for i in temp]
#     room.append(temp)

def findNeighbours(curr):
    isFactor(curr)

def isFactor(curr):
    factors = []
    for i in range(1, int(curr**0.5)+1):
        if curr % i == 0:
            factors.append([i, int(curr/i)])
            factors.append([int(curr/i), i])
    return factors

print(isFactor(8))
print(findNeighbours(8))

def bfs(adj, s): # s = room[0][0]
    q = []
    visited = [False] * len