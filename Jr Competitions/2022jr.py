# question 3
# be able to tell where numbers ending and when to start next instructions start
# input = input()
# inputArr = []
# num = '1234567890'

# tuning = {
#     "+": " tighten ",
#     "-": " loosen "
# }

# final = ''

# inputArr = input.split('+')
# for i in range(len(inputArr)):
#     final += inputArr[i] + " tighten "
# final = final[:len(inputArr)-11]

# inputArr = final.split('-')
# final = ''

# for i in range(len(inputArr)):
#     final += inputArr[i] + " loosen "
# final = final[:len(inputArr)-10]

# for i in range(len(final)-1):
#     if final[i+1] not in num and final[i] in num:
#         final = final[:i+1] + '~' + final[i+1:]

# final = final.split('~')

# for i in range(len(final)):
#     print(final[i])


input = input()
final = ''
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '1234567890'

for i in range(len(input)):
    if input[i] in letters or input[i] in nums:
        final += input[i]
    elif input[i] == '+':
        final += ' tighten '
    elif input[i] == '-':
        final += ' loosen '
    if i < len(input)-1 and input[i] in nums and input[i+1] in letters: # decide split
        final += '\n' # \n is new line character
        # print(final)
        # final = ''
print(final)