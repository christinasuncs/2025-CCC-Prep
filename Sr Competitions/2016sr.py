# question 1
# lineA = input()
# lineB = input()
# bCount = 0

# for i in range(len(lineB)):
#     if lineB[i] == "*":
#         bCount += 1
#     if lineB[i] in lineA:
#         # lineA[lineA.index(lineB[i])] = "~"
#         lineA = lineA.replace(lineB[i], "", 1)

# if len(lineA) == bCount:
#     print("A")
# else:
#     print("N")

# q1 method 2 (use dictionary to look up)
# create dictionary - to record freqency of each letter {key is letter: amount}
# go through second string, for whatever letter appears, remove from dictionary
# if any val is < 0, broken
# wildcards -> compare to sum in dictionary


# question 2
Q = int(input())
# if Q = 1 -> find min, if Q = 2 -> find max

N = int(input()) # number of people
countryD = input().split()
countryP = input().split()

for i in range(N):
    countryD[i] = int(countryD[i])
    countryP[i] = int(countryP[i])

sortedD = sorted(countryD) # small to big
sortedP = sorted(countryP)

total = 0
for i in range(N):
    if Q == 1:
        total += max(int(sortedD[i]), int(sortedP[i]))
    else:
        total += max(int(sortedD[i]), int(sortedP[N-1-i]))
print(total)

