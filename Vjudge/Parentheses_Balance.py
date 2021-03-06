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
    ans = 'Yes'
    for char in s:
        if char == '(' or char == '[':
            q.put(char)
        else:
            last = q.pop()
            if last is None:
                ans = 'No'
                break
            if char == ')':
                if last != '(':
                    ans = 'No'
                    break

            else:
                if last != '[':
                    ans = 'No'
                    break

    if len(q.queue) > 0:
        ans = 'No'

    print(ans)
