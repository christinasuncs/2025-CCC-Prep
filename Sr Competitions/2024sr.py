# question 1
N = int(input())
table = []

output = 0

for i in range(N):
    table.append(int(input()))

for i in range(N // 2):
    if table[i] == table[i+(N//2)]:
        output += 2

print(output)