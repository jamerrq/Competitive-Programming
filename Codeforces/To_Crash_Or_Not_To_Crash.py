import sys

lines = sys.stdin.readlines()

crash = 'You shall pass!!!'

for line in lines:
    car = False
    for char in line[:-1]:
        if car:
            if char != '.':
                crash = char
                break
        if char == '=':
            car = True

print(crash)
