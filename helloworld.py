def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    base = arr[0]
    left = []
    right = []

    index = 1
    while index < len(arr):
        if arr[index] < base:
            left.append(arr[index])
        else:
            right.append(arr[index])

        index += 1

    left = quick_sort(left)
    right = quick_sort(right)

    res = []
    res.extend(left)
    res.append(base)
    res.extend(right)

    return res

arr = [1,2,4,-100,0,1,6,-40]

print (quick_sort(arr))