def bubble_sort(d):
    list1 = d[:]
    for i in range(len(list1)-1, -1, -1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    return list1
    


