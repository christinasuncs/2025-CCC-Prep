# # question 1
# N = int(input())
# villages = []

# for i in range(N):
#     villages.append(int(input()))

# villages.sort()
# midpoints = []

# for i in range(N-1):
#     midpoints.append((villages[i]+villages[i+1])/2)

# smallest = float('inf')
# for i in range(len(midpoints)-1):
#     temp = midpoints[i+1] - midpoints[i]
#     if temp < smallest:
#         smallest = temp

# print(round(smallest,1))

# question 2
N = int(input())
heights = []

for i in range(N):
    temp = input().split()
    temp = [int(i) for i in temp]
    heights.append(temp)

def findRotations(heights):
    rowDiff = heights[0][1] - heights[0][0]
    colDiff = heights[1][0] - heights[0][0]

    # assuming clockwise (r,c), # of rotations we need to do
    # no rotations -> +, +
    # 1 rotation -> +, - 
    # 2 roations -> -, -
    # 3 rotations -> -, +

    if rowDiff > 0 and colDiff > 0:
        return 0
    elif rowDiff > 0 and colDiff < 0:
        return 1
    elif rowDiff < 0 and colDiff < 0:
        return 2
    else:
        return 3
    
numRotations = findRotations(heights)

for i in range(numRotations):
    heights = list(zip(*heights[::-1]))

for i in range(N):
    temp = ''
    for j in range(N):
        temp += str(heights[i][j]) + ' '
    print(temp[:-1])