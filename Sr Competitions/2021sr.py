# question 1

# N = int(input())
# sum = 0

# heights = list(map(int, input().split()))
# widths = list(map(int, input().split()))

# for i in range(N):
#     sum += ((heights[i]+heights[i+1])/2)*widths[i]

# print(sum)


# question 2
# M = int(input()) # row
# N = int(input()) # col
# K = int(input()) # line of instructions
# instructions = []
# grid = []

# for i in range(K):
#     instructions.append(input())

# # method 1 - true/false / 1/-1 grid
# # brute force way - not optimal

# # array comprehension
# grid = [[False]*N for i in range(M)]

# for instruction in instructions:
#     direction, num = instruction[0], int(instruction[2:])-1
#     if direction == "R":
#         for i in range(N):
#             grid[num][i] = not grid[num][i]
#     else:
#         for i in range(M):
#             grid[i][num] = not grid[i][num]
#     # print(grid)

# gold = 0
# for i in range(M):
#     for j in range(N):
#         if grid[i][j] == True:
#             gold += 1

# print(gold)

################################################
# method 2
# process queries first, before changing grid
# shove all rows and cols to front/first -> count

# M = int(input()) # row
# N = int(input()) # col
# K = int(input()) # line of instructions
# grid = []

# rows = [False]*M
# cols = [False]*N

# for i in range(K):
#     instruction = input().split()
#     direction, num = instruction[0], int(instruction[1])-1
#     if direction == "R":
#         rows[num] = not rows[num]
#     else:
#         cols[num] = not cols[num]

# # array comprehension
# grid = [[False]*N for i in range(M)]

# trueRow = sum(rows)
# trueCol = sum(cols)

# for i in range(trueRow):
#     grid[i] = [True]*N

# for i in range(trueCol):
#     for j in range(M):
#         grid[j][i] = not grid[j][i]

# gold = 0
# for i in range(M):
#     for j in range(N):
#         if grid[i][j] == True:
#             gold += 1

# print(gold)

################################################
# method 3
# process queries first, apply formula

M = int(input()) # row
N = int(input()) # col
K = int(input()) # line of instructions

rows = [False]*M
cols = [False]*N

for i in range(K):
    instruction = input().split()
    direction, num = instruction[0], int(instruction[1])-1
    if direction == "R":
        rows[num] = not rows[num]
    else:
        cols[num] = not cols[num]

trueRow = sum(rows)
trueCol = sum(cols)

gold = M*trueCol + N*trueRow - 2*trueRow*trueCol

print(gold)