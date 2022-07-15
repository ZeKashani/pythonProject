

# s = {1,2,3,4,6,7,7}
# print(s)
# print(len(s))
#
# s1 = s.add(10)
# print(s1)


with open("Exercise_4_Sample.txt") as txt:
    line = txt.readline().strip('\n')
    while line:
        print(line)
        line = txt.readline().strip('\n')

print(len(line))
