def selection_sort(d):
    list1 = d[:]
    for i in range(len(list1)):
        min = list1[i]
        min_i = i
        for j in range(i, len(list1)):
            if min > list1[j]:
                min = list1[j]
                min_i = j
        list1[i], list1[min_i] = list1[min_i], list1[i]
    return list1