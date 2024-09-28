# question 1
lineA = input()
lineB = input()
bCount = 0

for i in range(len(lineB)):
    if lineB[i] == "*":
        bCount += 1
    if lineB[i] in lineA:
        # lineA[lineA.index(lineB[i])] = "~"
        lineA = lineA.replace(lineB[i], "", 1)

if len(lineA) == bCount:
    print("A")
else:
    print("N")

# q1 method 2 (use dictionary to look up)
# create dictionary - to record freqency of each letter {key is letter: amount}
# go through second string, for whatever letter appears, remove from dictionary
# if any val is < 0, broken
# wildcards -> compare to sum in dictionary