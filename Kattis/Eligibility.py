import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    inline = line.split()
    name = inline[0]
    post = inline[1]
    birth = inline[2]
    courses = inline[3]
    if int(post[:4]) >= 2010:
        print(name + " eligible")
    elif int(birth[:4]) >= 1991:
        print(name + " eligible")
    elif int(courses) >= 41:
        print(name + " ineligible")
    else:
        print(name + " coach petitions")
    
