# 선택 정렬 알고리즘 -> 끝에 거랑 바꿈

list1 = [8,2,0,4,5,1,6,3,7]

for i in range(len(list1)-1, -1, -1):
    max = list1[i]
    max_i = i
    for j in range(i):
        if max < list1[j]:
            max = list1[j]
            max_i = j
    list1[i], list1[max_i] = list1[max_i], list1[i]

print(list1)

# 선택 정렬 알고리즘 최소로

list1 = [8,2,0,4,5,1,6,3,7]

for i in range(len(list1)):
    min = list1[i]
    min_i = i
    for j in range(i, len(list1)):
        if min > list1[j]:
            min = list1[j]
            min_i = j
    list1[i], list1[min_i] = list1[min_i], list1[i]    

print(list1)
# 버블 정렬 알고리즘

list2 = [8,2,0,4,5,1,6,3,7]

for i in range(len(list2)-1, -1, -1):
    for j in range(i):
        if list2[j] > list2[j+1]:
            list2[j], list2[j+1] = list2[j+1], list2[j]

print(list2)

# 삽입 정렬 알고리즘 

list3 = [8,2,0,4,5,1,6,3,7]
#1 2 3  5 6 7 8 4 
            #  l i

for i in range(1, len(list3)):
    for j in range(i-1, -1, -1):
        if list3[j] > list3[j+1]: # i가 loc, i+1이 new
            list3[j], list3[j+1] = list3[j+1], list3[j]
        else:
            break

print(list3)

           