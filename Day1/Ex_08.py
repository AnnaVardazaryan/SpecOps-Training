num = 4637
summ = 0
while num:
  summ += num % 10
  num = num //10
print(summ)