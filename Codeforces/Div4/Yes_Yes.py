import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):

    s = read(str)
    # print(s)
    answer = 'YES'

    for i in range(len(s)):
        if s[i] == 'Y':
            try:
                if i and s[i - 1] != 's':
                    answer = 'NO'
                    break
            except:
                pass

            try:
                if s[i + 1] != 'e':
                    answer = 'NO'
                    break
            except:
                pass

        elif s[i] == 'e':
            try:
                if i and s[i - 1] != 'Y':
                    answer = 'NO'
                    # print('here', i)
                    break
            except:
                pass

            try:
                if s[i + 1] != 's':
                    # print('here 2', i)
                    answer = 'NO'
                    break
            except:
                pass

        elif s[i] == 's':
            try:
                if i and s[i - 1] != 'e':
                    answer = 'NO'
                    break
            except:
                pass

            try:
                if s[i + 1] != 'Y':
                    answer = 'NO'
                    break
            except:
                pass

        else:
            answer = 'NO'
            break


    print(answer)
