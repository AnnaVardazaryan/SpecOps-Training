str1 = 'hello world'
str2 = ''
i = 0
while i < len(str1):
    str2 += str1[i:i+2]
    i = i + 3
print(str2)
