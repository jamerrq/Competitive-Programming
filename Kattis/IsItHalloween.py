import sys

line = sys.stdin.readline().split()

if (line[0] == 'OCT' and line[1] == '31') or (line[0] == 'DEC' and line[1] == '25'):
    print('yup')
else:
    print('nope')
