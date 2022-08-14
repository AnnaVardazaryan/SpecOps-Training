f = open("textfile.txt", "r")
count = 0
for lines in f:
    words = lines.strip().split(" ")
    for i in range(len(words)):
            count += len(words[i])
print(count)


