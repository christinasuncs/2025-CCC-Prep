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
X = int(input())
together = [input().split() for i in range(X)] # *** REMEMBER ARRAY COMPREHENSION!!!

Y = int(input())
apart = [input().split() for i in range(Y)] # *** REMEMBER

G = int(input())
groups = [input().split() for i in range(G)] # *** REMEMBER

# check violated X pairs
# check violated Y pairs
# keep running count