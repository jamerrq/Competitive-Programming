def is_palindrome(n):
    strn = str(n)
    return strn == strn[::-1]

max_prd = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        ij = i * j
        if is_palindrome(ij) and ij > max_prd:
            max_prd = ij

print(max_prd)
