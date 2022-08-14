haystack = 'hello'
needle = 'll'
if needle in haystack:
    print(haystack.index(needle[0]))
else:
    print(-1)