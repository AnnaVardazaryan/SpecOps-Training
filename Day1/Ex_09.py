def num_prod(num):
  prod = 1
  while num:
    prod *= num % 10
    num = num // 10
  return prod
def num_sum(num):
  sum = 0
  while num:
    sum += num % 10
    num = num //10
  return sum
num = 4637
print(num_prod(num) - num_sum(num))