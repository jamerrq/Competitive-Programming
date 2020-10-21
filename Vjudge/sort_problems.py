import os

file = open('0-Problems.txt')

problems = []
for line in file:
    complete = line.split()
    #print(complete)
    link = file.readline()
    #print(link)
    file.readline()
    problems.append((' '.join(complete[1:]), link))


file.close()
problems.sort()

file2 = open('1-Problems.txt', 'w')
count = 1
for problem in problems:
    file2.write(f'{count}. {problem[0]}\n')
    file2.write(f'{problem[1]}\n')
    count += 1

file2.close()

os.system('mv 1-Problems.txt 0-Problems.txt')
