# question 3

# instructions = []
# notEnd = True
# direction = ''

# while (notEnd):
#     number = input()
#     if number == '99999':
#         notEnd = False
#     else:
#         instructions.append(number)

# # print(instructions)

# for i in range(len(instructions)):
#     sum = int(instructions[i][0]) + int(instructions[i][1])
#     if sum == 0:
#         direction = direction
#     elif sum % 2 == 1:
#         direction = 'left'
#     elif sum % 2 == 0:
#         direction = 'right'
#     print(direction + " " + instructions[i][2:])


# question 4
books = input()
newBooks = ''
wrongBooks = ''
swaps = 0

L = 0
M = 0
S = 0

for i in range(len(books)):
    if books[i] == 'L':
        L += 1
    elif books[i] == 'M':
        M += 1
    else:
        S += 1

# old slow vers
# for i in range(L):
#     newBooks += 'L'
# for i in range(M):
#     newBooks += 'M'
# for i in range(S):
#     newBooks += 'S'

# new fast vers
newBooks = 'L'*L + 'M'*M + 'S'*S

sectionL = [0, 0, 0]
sectionM = [0, 0, 0]
sectionS = [0, 0, 0]

for i in range(len(books)):
    if newBooks[i] == 'L':
        if books[i] == 'L':
            sectionL[0] += 1
        elif books[i] =='M':
            sectionL[1] += 1
        else:
            sectionL[2] += 1
    elif newBooks[i] == "M":
        if books[i] == 'L':
            sectionM[0] += 1
        elif books[i] =='M':
            sectionM[1] += 1
        else:
            sectionM[2] += 1
    else:
        if books[i] == 'L':
            sectionS[0] += 1
        elif books[i] =='M':
            sectionS[1] += 1
        else:
            sectionS[2] += 1

# double swaps
swaps += min(sectionL[1],sectionM[0]) +  min(sectionM[2],sectionS[1]) + min(sectionL[2],sectionS[0])

# doings swaps btwn L and M
minLM = min(sectionL[1],sectionM[0])

sectionL[0] += minLM
sectionL[1] -= minLM
sectionM[1] += minLM
sectionM[0] -= minLM

# doings swaps btwn L and S
minLS = min(sectionL[2],sectionS[0])

sectionL[0] += minLS
sectionL[2] -= minLS
sectionS[2] += minLS
sectionS[0] -= minLS

# doings swaps btwn M and S
minMS = min(sectionM[2],sectionS[1])

sectionM[1] += minMS
sectionM[2] -= minMS
sectionS[2] += minMS
sectionS[1] -= minMS

# single swaps
swaps += (sectionL[1] + sectionL[2])*2

print(swaps)