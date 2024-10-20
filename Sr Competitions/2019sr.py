# question 1
# thing = input()
# vCount = 0
# hCount = 0

# for i in range(len(thing)):
#     if thing[i] == 'V':
#         vCount += 1
#     else:
#         hCount += 1

# if vCount % 2 == 0 and hCount % 2 == 0:
#     print('1 2')
#     print('3 4')
# elif vCount % 2 == 1 and hCount % 2 == 0:
#     print('2 1')
#     print('4 3')
# elif vCount % 2 == 0 and hCount % 2 == 1:
#     print('3 4')
#     print('1 2')
# else:
#     print('4 3')
#     print('2 1')

# question 2
T = int(input())

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): # sqrt + 1
        if num % i == 0:
            return False
    return True

def findPrimes(num):
    right = num
    left = num
    if num % 2 == 0:
        right = num + 1
        left = num - 1
    while not isPrime(right) or not isPrime(left):
        right += 2
        left -= 2
    print(str(right) + ' ' + str(left))

for i in range(T):
    findPrimes(int(input()))