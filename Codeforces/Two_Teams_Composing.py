import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    skills = list(map(int, line))
    freq = [0] * n
    max_freq = 0
    skill_fq = 0

    for i in range(n):
        freq[skills[i] - 1] += 1
        if freq[skills[i] - 1] > max_freq:
            max_freq = freq[skills[i] - 1]
            skill_fq = skills[i]

    sum_freqs = 0
    for i in range(n):
        if i != skill_fq - 1:
            sum_freqs += min(1, freq[i])

    #print(max_freq, sum_freqs)

    if max_freq > sum_freqs + 1:
        print(sum_freqs + 1)
    else:
        print(min(sum_freqs, max_freq))
