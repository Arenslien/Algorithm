def merge_sort(d):
    if len(d) < 2:
        return d

    mid = len(d) // 2
    low_arr = merge_sort(d[:mid])
    high_arr = merge_sort(d[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr