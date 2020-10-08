import sys


n = int(sys.stdin.readline())
videos = [None] * n

for i in range(n):
    video = list(map(int, sys.stdin.readline().split()))
    t = video.pop(0)
    videos[i] = video


videos.sort(key=lambda x:len(x))
ocupped = set()
answer = 0
for i in range(n):
    for j in range(len(videos[i])):
        if not videos[i][j] in ocupped:
            answer = videos[i][j] + 1
            ocupped.add(answer - 1)
            break


print(answer)
