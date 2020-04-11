import sys

class Activity(object):

    def __init__(self, start, end, number):
        self.start = start
        self.end = end
        self.assigned = None
        self.number = number
    
    def assing(self, parent):
        self.assigned = parent


t = int(sys.stdin.readline())
for k in range(t):
    n = int(sys.stdin.readline())
    activities = []
    for i in range(n):
        line = sys.stdin.readline().split()
        s, e = int(line[0]), int(line[1])
        acti = Activity(s, e, i)
        activities.append(acti)

    activities.sort(key=lambda x:x.start)
    C = 0
    J = 0
    P = True
    for i in range(n):
        activity = activities[i]
        if activity.start >= C:
            activity.assing('C')
            C = activity.end
        else:
            if activity.start >= J:
                activity.assing('J')
                J = activity.end
            else:
                P = False
        if not P:
            break

    activities.sort(key=lambda x:x.number)
    schedule = ''
    if not P:
        print('Case #{}: IMPOSSIBLE'.format(k + 1))
    else:
        for i in range(n):
            schedule += activities[i].assigned
        print('Case #{}: {}'.format(k + 1, schedule))
