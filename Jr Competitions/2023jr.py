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
N = int(input())
road = []
tape = 0

for i in range(2):
    row = input()
    rowArr = row.split()
    road.append(rowArr)

for i in range(2):
    for j in range(N):
        if road[i][j] == '1':
            tape += 3
        if j < N-1 and road[i][j] == road[i][j+1] and road[i][j] == '1':
            tape -= 2
        if i == 0 and j%2 == 0 and road[i][j] == '1' and road[1][j] == road[i][j]:
            tape -= 2

print(tape)