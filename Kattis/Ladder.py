def stair():
    from math import sin
    from math import radians
    line = input()
    l = ""
    a = ""
    f = False
    for i in range(len(line)):
        if not f and line[i] != " ": l += line[i]
        else: a += line[i]
        if line[i] == " ": f = True
    l = int(l)
    a = int(a)
    s = l / sin(radians(a))
    return int(s + 1)

print(stair())
    
