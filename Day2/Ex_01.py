str1 = 'hello'
str2 = ''
def strmove(str1, num):
    if num == len(str1):
        return str1
    if num < len(str1):
        return str1[-num:] + str1[0:num + 1]
    else:
        return strmove(str1, num-len(str1))
print(strmove(str1, 2))

