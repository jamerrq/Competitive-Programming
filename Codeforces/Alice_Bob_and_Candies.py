import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    alice = A[0]
    bob = 0
    i = 1
    j = n - 1
    turn = True
    count = 1
    prev = alice
    while i <= j:
        acc = 0
        if turn:
            while acc <= prev and i <= j:
                acc += A[j]
                j -= 1
            bob += acc
        else:
            while acc <= prev and i <= j:
                acc += A[i]
                i += 1
            alice += acc
        prev = acc
        count += 1
        turn = not turn
        #print(count, alice, bob)

    print(count, alice, bob)
