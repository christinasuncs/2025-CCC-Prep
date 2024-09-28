# question 1
# score = 0

# delivered = int(input())
# collisions = int(input())

# score = delivered*50 - collisions*10
# if delivered > collisions:
#     score += 500

# print(score)

# question 2
# use dictionary/hashmap, keys must be unique, to search -> lookup
# N = int(input())
# T = 0

# peppers = {
#     "Poblano": 1500,
#     "Mirasol": 6000,
#     "Serrano": 15500,
#     "Cayenne": 40000,
#     "Thai": 75000,
#     "Habanero": 125000
# }

# for i in range(N):
#     T += peppers[input()]

# print(T)

# question 3
# N = int(input())
# schedule = []

# for i in range(N):
#     week = input()
#     weekArr = []
#     for j in range(5):
#         weekArr.append(week[j])
#     schedule.append(weekArr)

# score = 0
# maxScore = 0
# bestDay = ''

# for i in range(5):
#     score = 0
#     for j in range(N):
#         if schedule[j][i] == "Y":
#             score += 1
#     if score > maxScore:
#         maxScore = score
#         bestDay = str(i+1)
#     elif score == maxScore:
#         bestDay += "," + str(i+1)

# print(bestDay)

# question 3 version 2
# N = int(input())
# days = [0,0,0,0,0]
# bestDay = ''

# for i in range(N):
#     week = input()
#     for j in range(5):
#         if week[j] == "Y":
#             days[j] += 1

# max = max(days)
# for i in range(5):
#     if days[i] == max:
#         bestDay += "," + str(i+1)

# print(bestDay[1:])

# question 4
# N = int(input())
# road = []
# tape = 0

# for i in range(2):
#     row = input()
#     rowArr = row.split()
#     road.append(rowArr)

# for i in range(2):
#     for j in range(N):
#         if road[i][j] == '1':
#             tape += 3
#         if j < N-1 and road[i][j] == road[i][j+1] and road[i][j] == '1':
#             tape -= 2
#         if i == 0 and j%2 == 0 and road[i][j] == '1' and road[1][j] == road[i][j]:
#             tape -= 2

# print(tape)

# question 5
# needs recursion - calls itself, needs a base case to stop:
# search function
# look around, if good, keep looking
# base case 1: next letter wrong
# base case 2: found entire word/found last letter
# base case 3: out of bounds

# use negtive reciprocal slope for diagonal corners (generalization)
W = input()
R = int(input())
C = int(input())

letters = [input().split() for _ in range(R)]
total = 0

directions = [(0, 1), (0, -1), # keep r, change c -> horizontal
              (1, 0), (-1, 0), # keep c, change r -> vertical
              (-1, -1), (-1, 1), # left diagonals
              (1, -1), (1, 1)] # right diagonals

# for i in range(R):
#     letters.append(input())

# for i in range(R):
#     letters[i] = letters[i].split()

# search function - takes x and y, take word, take letters
def search(r, c, i, dirRow, dirCol, hasTurned): # r = x, c = y, i(ndex) = 1
    
    # vertical and horizonal
    if not (0 <= r < R and 0 <= c < C): # check if not in range
        return 0
    if letters[r][c] != W[i]: # check for not match
        return 0
    if i == len(W)-1: # check length/if at last letter
        return 1
    
    # if you reach here keep searching

    count = search(r + dirRow, c + dirCol, i+1, dirRow, dirCol, hasTurned) # check in same direction

    if not hasTurned: # check perpendicular directions
        count += search(r + (dirCol*-1), c + dirRow, i+1, dirCol*-1, dirRow, True) 
        count += search(r + dirCol, c + (dirRow*-1), i+1, dirCol, (dirRow*-1), True)
    
    return count
   
for i in range(R):
    for j in range(C):
        # first letter found
        if letters[i][j] == W[0]:
            for dirRow, dirCol in directions:
                # recursion part here, call search function
                total += search(i + dirRow, j + dirCol, 1, dirRow, dirCol, False)
            
print(total)