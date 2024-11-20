# question 1
# N = int(input())
# table = []

# output = 0

# for i in range(N):
#     table.append(int(input()))

# for i in range(N // 2):
#     if table[i] == table[i+(N//2)]:
#         output += 2

# print(output)


# question 2
# temp = input().split()
# T = int(temp[0])
# N = int(temp[1])

# def determine(line):
#     prevWeight = ""
#     for i in range(N):
#         tempLine = line[:i] + line[i+1:] # line without current letter
#         if line[i] in tempLine:
#             if prevWeight == "H":
#                 return "F"
#             prevWeight = "H"
#         else:
#             if prevWeight == "L":
#                 return "F"
#             prevWeight = "L"
#     return "T"

# for i in range(T):
#     line = input()
#     print(determine(line))


# question 3
N = int(input())
A = input().split()
B = input().split()

# for i in range(N):
#     if A[i] != B[i]:
#         if i == 0: # swipe was left
#             temp = A.index(B[i]) # where left swipe started
#             if 

# if B != A:
#     for i in range(2):
#         if B[i] != A[i]:


# # 2 points:
# if B == A:
#     print("YES")
#     print("0")
# elif B[0] == A[0] and B[1] == A[0]:
#     print("YES")
#     print("R 0 1")
# elif B[0] == A[1] and B[1] == A[1]:
#     print("YES")
#     print("L 0 1")
# else:
#     print("NO")

# 4 points:
if A == B:
    print("YES")
    print("0")
else:
    # swipes cannot overlap
    # use characteristics to organize
    # once you swipes a certain range, no need to swipe again in that range
    # once numbers have been swiped over (overwritten), cannot show up again in arr unless already present elsewhere in arr