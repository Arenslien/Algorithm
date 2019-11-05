def insertion_sort(d):
    list1 = d[:]
    for i in range(1, len(list1)):
        for j in range(i-1, -1, -1):
            if list1[j] > list1[j+1]: # i가 loc, i+1이 new
                list1[j], list1[j+1] = list1[j+1], list1[j]
            else:
                break

    return list1