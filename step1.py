# # Part 1
# input1 = '36+4+10+2'
#
# sum = 0
#
# modules = input1.split('+')
#
# for module in modules:
#     sum = int(module) + sum
#
# print(sum)

# Part 1 - 2nd Approach
input1 = '36+4+10+2'

sum = 0

modules = input1.split('+')

for module in modules:
    module = ord(module) - ord(0)
    sum = module + sum

print(sum)
