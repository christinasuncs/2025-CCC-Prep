# question 1
# method 1 - for loop
# N = int(input())
# ways = 0

# # is divisible by 4
# if N % 4 == 0:
#     ways += 1

# for i in range(N//4):
#     if (N - 4*i) % 5 == 0:
#         ways += 1

# print(ways)

# method 2 - while loop
# num = int(input())
# count = 0
# if num % 5 == 0:
#     count += 1
# while num > 0:
#     if num % 4 == 0:
#         count += 1
#     num -= 5

# print(count)

# question 2
# method 1 (too slow)
# X = int(input())
# together = [input().split() for i in range(X)] # *** REMEMBER ARRAY COMPREHENSION!!!

# Y = int(input())
# apart = [input().split() for i in range(Y)] # *** REMEMBER

# G = int(input())
# groups = [input().split() for i in range(G)] # *** REMEMBER

# violations = 0

# check violated X pairs
# find tgt[i, 0] in groups -> get groups[x] (whichever has tgt[i, 0])
# check if [i, 1] is in groups[x]
# yes -> do nothing
# no -> violations += 1

# check violated Y pairs
# find apart[i, 0] in groups -> get groups[x] (whichever has apart[i, 0])
# check if [i, 1] is in groups[x]
# yes -> violations += 1
# no -> do nothing

# keep running count

# OR
# look at groups and count violations

# OR
# make groups of 3 all possible groups of 2, compare to X and Y rules, count

# for i in range(X):
#     tgt1 = together[i][0]
#     tgt2 = together[i][1]
#     groupNum = 0
#     for j in range(G):
#         for k in range(3):
#             if tgt1 == groups[j][k] and tgt2 not in groups[j]:
#                     violations += 1

# for i in range(Y):
#     apart1 = apart[i][0]
#     apart2 = apart[i][1]
#     groupNum = 0
#     for j in range(G):
#         for k in range(3):
#             if apart1 == groups[j][k] and apart2 in groups[j]:
#                     violations += 1

# print(violations)


# method 2: use dictionary (so much faster)
X = int(input())
together = [input().split() for i in range(X)] # *** REMEMBER ARRAY COMPREHENSION!!!

Y = int(input())
apart = [input().split() for i in range(Y)] # *** REMEMBER

G = int(input())
groups = {}
for i in range(G):
    temp = input().split()
    groups[temp[0]] = i # person needs to be key, group # is value
    groups[temp[1]] = i
    groups[temp[2]] = i

violations = 0

for i in range(X):
    if groups[together[i][0]] != groups[together[i][1]]:
        violations += 1

for i in range(Y):
    if groups[apart[i][0]] == groups[apart[i][1]]:
        violations += 1

print(violations)
