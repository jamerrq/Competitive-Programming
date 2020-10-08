from os import ctermid
import sys
from sys import version


filename = sys.stdin.readline().strip()
program  = sys.stdin.readline().strip().split('\\')


if program[-1] != filename + '.c' and program[-1] != filename + '.cpp' and \
    program[-1] != filename + '.java' and program[-1] != filename + '.py':
    print('Compile Error')

elif len(program) > 1:
    print('Compile Error')

else:
    r, d, e = map(int, sys.stdin.readline().split())
    if r != 0:
        print('Run-Time Error')
    elif e > d:
        print('Time Limit Exceeded')
    else:
        c = int(sys.stdin.readline())
        answer = [None] * c
        for i in range(c):
            answer[i] = sys.stdin.readline()

        t = int(sys.stdin.readline())
        if  t != c:
            print('Wrong Answer')
        else:
            veredict = 'Correct'
            response = [None] * t
            for i in range(t):
                response[i] = sys.stdin.readline()
                if response[i] != answer[i]:
                    veredict = 'Wrong Answer'
                    break

            print(veredict)
