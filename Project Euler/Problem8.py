file = open('in')

num = ''
for line in file:
    for char in line:
        if char.isalnum():
            num += char


file.close()


maxi = 0
for i in range(len(num) - 13):
    curr = 1
    for j in range(i, i + 13):
        curr *= int(num[j])
        maxi = max(maxi, curr)


print(maxi)
