f = open("textfile.txt", "r")
d = {}
count = 0
for lines in f:
    words = lines.strip().split(" ")
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
print(d)
