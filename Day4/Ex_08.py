s = "A man, a plan, a canal: Panama"
def palindrome_str(s):
    new_s =""
    for i in s:
        if i.isalpha() == True or i.isnumeric() == True:
            new_s += i
    new_s = new_s.lower()
    if new_s == new_s[::-1]:
        return True
    return False
print(palindrome_str(s))