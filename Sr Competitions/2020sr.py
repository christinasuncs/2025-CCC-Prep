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

M = int(input())
N = int(input())

# M = 3
# N = 4

room = []
end = M*N
visited = [[ False for i in range(N)] for i in range(M)]

for i in range(M):
    temp = input().split()
    temp = [int(i) for i in temp]
    room.append(temp)

factorsMemo = {}

# # find all factors of curr
# def factor(curr):
#     if curr in factorsMemo:
#         return factorsMemo[curr]

#     factors = []
#     for i in range(1, int(curr**0.5)+1):
#         if curr % i == 0:
#             factors.append([i, int(curr/i)])
#             if i != int(curr/i):
#                 factors.append([int(curr/i), i])

#     factorsMemo[curr] = factors
#     return factors

# # find valid coords
# def findValidCoords(curr):
#     factors = factor(curr)
#     validFactors = []
#     for f in factors:
#         if f[0] <= M and f[1] <= N:
#             validFactors.append(f)
#     return validFactors

def factorAndFindValid(curr):
    if curr in factorsMemo:
        return factorsMemo[curr]

    factors = []
    for i in range(1, int(curr**0.5)+1):
        if curr % i == 0:
            r1, c1 = i, curr // i
            if i != curr // i:
                r2, c2 = curr // i, i
                if r2 <= M and c2 <= N:
                    factors.append((r2-1, c2-1))

            if r1 <= M and c1 <= N:
                factors.append((r1-1, c1-1))

    factorsMemo[curr] = factors
    return factors

def bfs(room, visited): 
    q = []

    q.append((0, 0))
    visited[0][0] = True

    while (len(q) > 0):
        r, c = q.pop(0)
        val = room[r][c]
        if val == end:
            print("yes")
            return
        coords = factorAndFindValid(val)

        for coord in coords:
            new_r, new_c = coord[0], coord[1]
            if not visited[new_r][new_c]:
                q.append((new_r, new_c))
                visited[new_r][new_c] = True
    
    print("no")

bfs(room, visited)

# to improve:
# remove duplicated factors

# version 2:
# store factors - memoization = avoid repetition
# empty dictionary (factorMemo) store factors that have been computed

# 13/15 max score :/ --> need different approach