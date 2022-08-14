def palindrome(num):
    if num < 0:
      return False
    num1 = num
    num2 = 0
    while num:
        num2 = num2*10 + num % 10
        num //= 10
    return num2 == num1

print(palindrome(121))
