# question 1
# data structure: stacks (in python can just use array)
#   insert anything into stack, first in last out

# K = int(input())
# numbers = []
# sum = 0

# for i in range(K):
#     val = int(input())
#     if val == 0:
#         numbers.pop()
#     else:
#         numbers.append(val)

# for i in range(len(numbers)):
#     sum += numbers[i]

# print(sum)

# question 2
# use dictionary for jerseys
# efficiency !!! (avoid 2 for loops at all costs)
J = int(input())
A = int(input())
jerseys = {}
count = 0

for i in range(J):
    jerseys[i+1] = input()

for i in range(A):
    athletes = input()
    size, num = athletes.split()
    if jerseys[int(num)] <= size:
        count += 1
        jerseys[int(num)] = "z"

print(count)