import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


signs = {
    'Aries'       : [21,  3, 20,  4],
    'Taurus'      : [21,  4, 20,  5],
    'Gemini'      : [21,  5, 21,  6],
    'Cancer'      : [22,  6, 22,  7],
    'Leo'         : [23,  7, 22,  8],
    'Virgo'       : [23,  8, 21,  9],
    'Libra'       : [22,  9, 22, 10],
    'Scorpio'     : [23, 10, 22, 11],
    'Sagittarius' : [23, 11, 21, 12],
    'Capricorn'   : [22, 12, 20,  1],
    'Aquarius'    : [21,  1, 19,  2],
    'Pisces'      : [20,  2, 20,  3]
}

months = {
    'Jan' :  1,
    'Feb' :  2,
    'Mar' :  3,
    'Apr' :  4,
    'May' :  5,
    'Jun' :  6,
    'Jul' :  7,
    'Aug' :  8,
    'Sep' :  9,
    'Oct' : 10,
    'Nov' : 11,
    'Dec' : 12
}

t = read()

for _ in range(t):
    d, m = readList(str)
    d, m = int(d), months[m]
    for key in signs.keys():
        sd, sm, fd, fm = signs[key]
        if m == sm:
            if d >= sd:
                print(key)
        if m == fm:
            if d <= fd:
                print(key)
