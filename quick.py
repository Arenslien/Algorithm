def quick_sort(d):
    if len(d) <= 1:
        return d
    pivot = d[len(d) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in d:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)