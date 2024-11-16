C = int(input())
L1  = input().split()
L2  = input().split()

tape = 0

for i in range(C):
    if L1[i] == "1":
        tape += 3
        if i > 0 and L1[i-1] == "1":
            tape -= 2
    if L2[i] == "1":
        tape += 3
        if L1[i] == "1" and i % 2 == 0:
            tape -= 2
        if i > 0 and L2[i-1] == "1":
            tape -= 2

print(tape)