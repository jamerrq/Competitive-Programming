import sys
from typing import Tuple


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


mirror = {
    'A' : 'A',
    'E' : '3',
    'H' : 'H',
    'I' : 'I',
    'J' : 'L',
    'L' : 'J',
    'M' : 'M',
    'O' : 'O',
    'S' : '2',
    'T' : 'T',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    'Z' : '5',
    '1' : '1',
    '2' : 'S',
    '3' : 'E',
    '5' : 'Z',
    '8' : '8'
}


def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True


def isMirrored(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] != mirror.get(string[j], ''):
            return False

        i += 1
        j -= 1

    return True


for line in sys.stdin:
    string = line.strip()
    isPali = isPalindrome(string)
    isMirr = isMirrored(string)

    if isPali:
        if isMirr:
            print(f'{string} -- is a mirrored palindrome.')
        else:
            print(f'{string} -- is a regular palindrome.')
    else:
        if isMirr:
            print(f'{string} -- is a mirrored string.')
        else:
            print(f'{string} -- is not a palindrome.')

    print()
