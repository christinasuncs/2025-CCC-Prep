# # question 1
# N = int(input())
# K = 0

# team1 = input().split()
# team2 = input().split()

# for i in range(N):
#     team1[i] = int(team1[i])
#     team2[i] = int(team2[i])

# sum1 = sum(team1)
# sum2 = sum(team2)

# for i in range(N, 0, -1):
#     # sum1 += team1[i]
#     # sum2 += team2[i]
#     if sum1 == sum2:
#         K = i
#         break
#     sum1 -= team1[i-1]
#     sum2 -= team2[i-1]

# print(K)

# question 2
N = int(input())
tides = input().split()
newTides = []

# arr = [int(i) for i in arr] // list comprehension
tides = [int(i) for i in tides]

sortedTides = sorted(tides)

if N % 2 == 0:
    lowTides = sortedTides[:N//2]
    highTides = sortedTides[N//2:]
    for i in range(N//2):
        newTides.append(lowTides[N//2-1-i])
        newTides.append(highTides[i])
else:
    lowTides = sortedTides[:N//2]
    highTides = sortedTides[N//2+1:]
    newTides.append(sortedTides[N//2])
    for i in range(N//2):
        newTides.append(highTides[i])
        newTides.append(lowTides[N//2-1-i])

stringTides = ''
for num in newTides:
    stringTides += str(num) + " "

print(stringTides[:-1])