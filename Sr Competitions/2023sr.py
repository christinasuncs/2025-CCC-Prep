# question 1
# C = int(input())
# L1  = input().split()
# L2  = input().split()

# tape = 0

# for i in range(C):
#     if L1[i] == "1":
#         tape += 3
#         if i > 0 and L1[i-1] == "1":
#             tape -= 2
#     if L2[i] == "1":
#         tape += 3
#         if L1[i] == "1" and i % 2 == 0:
#             tape -= 2
#         if i > 0 and L2[i-1] == "1":
#             tape -= 2

# print(tape)

# question 2
N = int(input())
mountains = list(map(int, input().split()))

crops = [0]

def getMinCrop(len):
    lowestCrop = float('inf')
    for j in range(N - len + 1):
        runningCrop = 0
        arr = mountains[j: j + len]
        for l in range(len // 2):
            runningCrop += abs(arr[l] - arr[len-l-1])
            if runningCrop >= lowestCrop:
                break
        if runningCrop < lowestCrop:
            lowestCrop = runningCrop
    return lowestCrop

for i in range(2, N+1):
    crops.append(getMinCrop(i))

cropsString = ""
for i in range(N):
    cropsString += str(crops[i]) + ' '

print(cropsString[:-1])

# method 2: use for and while loop
# for loop to get starting index, moves slowly in sequence
# len (starts at 2)
# while loop in for loop, moves 2 indexs closer and closer, get min value