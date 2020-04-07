import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()
nums = list(map(int, line))

def thanos_sort(nums, n):
    is_sort = True
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            is_sort = False
    if is_sort:
        return n
    else:
        l1 = thanos_sort(nums[:n//2], n // 2)
        l2 = thanos_sort(nums[n//2:], n // 2)
        return max(l1, l2)

print(thanos_sort(nums, n))
