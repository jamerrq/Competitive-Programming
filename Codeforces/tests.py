def binary_search(arr, x):

    beg = 0
    end = len(arr) - 1

    while beg < end:

        if beg == end - 1:
            if arr[end] > x:
                return beg
            return end

        mid = (beg + end) // 2

        if arr[mid] <= x:
            beg = mid

        else:
            end = mid - 1

    return beg


mA = [1, 2, 2, 5, 9]
print(binary_search(mA, 7))