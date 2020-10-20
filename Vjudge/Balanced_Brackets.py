import sys


class Queue(object):

    def __init__(self):
        self.queue = []

    def put(self, data):
        self.queue.append(data)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop()


t = int(sys.stdin.readline())


for _ in range(t):
    s = sys.stdin.readline().strip()
    q = Queue()
    ans = 'YES'
    for char in s:
        if char == '(' or char == '[' or char == '{':
            q.put(char)
        else:
            last = q.pop()
            if last is None:
                ans = 'NO'
                break
            if char == ')':
                if last != '(':
                    ans = 'NO'
                    break

            elif char == ']':
                if last != '[':
                    ans = 'NO'
                    break

            else:
                if last != '{':
                    ans = 'NO'
                    break

    if len(q.queue) > 0:
        ans = 'NO'

    print(ans)
