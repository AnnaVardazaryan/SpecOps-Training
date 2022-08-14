file1 = open("numbers.txt", "r")
lines  = file1.read().splitlines()
lst = []
for i in range(len(lines)):
    lst.append(lines[i].split(" "))
lst1 = [[int(num) for num in l]  for l in lst]
summ = 0
for i in lst1:
    summ += sum(i)
print(summ)

