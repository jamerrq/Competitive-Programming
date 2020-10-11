import sys


n, d = map(int, sys.stdin.readline().split())
stri = sys.stdin.readline().strip()

def bfs():
    ds = [-1] * n
    ds[0] = 0
    #
    queue = [0]
    #
    while queue:
        #print(queue)
        front = queue.pop(0)
        for i in range(front + 1, min(n, front + d + 1)):
            if int(stri[i]) and ds[i] == -1:
                ds[i] = ds[front] + 1
                queue.append(i)

    return ds[-1]


print(bfs())
