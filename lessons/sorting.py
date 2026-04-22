# unsorted_list = [4,2,2,1,5,6]
# sorted_list = sorted(unsorted_list)
# print(sorted_list)
#
# print(unsorted_list.sort())
from numpy.ma.core import equal


def buble_sort(unsorted_list:list[int]) -> list[int]:
        n=len(unsorted_list)
        for i in range(n):
            for j in range(0,n-i-1):
                if unsorted_list[j]>unsorted_list[j+1]:
                    unsorted_list[j], unsorted_list[j+1]=unsorted_list[j+1], unsorted_list[j]

        return unsorted_list

print(buble_sort([5,4,3,2,1]))
# [5,4,3,2,1] -> [4,5,3,2,1]
# [4,5,3,2,1] -> [4,3,5,2,1]
# [4,3,5,2,1] -> [4,3,2,5,1]
# [4,3,2,5,1] -> [4,3,2,1,5]
# ...
# [2,1,3,4,5,] -> [1,2,3,4,5]

def selection_sort(unsorted_list:list[int]) -> list[int]:
    n=len(unsorted_list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if unsorted_list[j]<unsorted_list[min_index]:
                min_index=j

        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    return unsorted_list

print('*'*80)
print(selection_sort([5,6,3,4,1]))

# [5,4,3,2,1] -> [1,4,3,2,5]
# [1,4,3,2,5] -> [1,3,2,4,5]
# [1,3,2,4,5] -> [1,2,3,4,5]

def insertion_sort(unsorted_list:list[int]) -> list[int]:
    for i in range(1,len(unsorted_list)):
        current=unsorted_list[i]
        j=i-1
        while j>=0 and current<unsorted_list[j]:
            unsorted_list[j+1]=unsorted_list[j]
            j-=1
        unsorted_list[j+1]=current

    return unsorted_list

print('*'*80)
print(insertion_sort([5,2,6,3,4,1]))


def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


print('*'*80)
print(merge([1,4,7],[2,3,8]))

def merge_sort(unsorted_list:list[int]) -> list[int]:
    if len(unsorted_list)<=1:
        return unsorted_list
    else:
        middle=len(unsorted_list)//2
        left=merge_sort(unsorted_list[:middle])
        right=merge_sort(unsorted_list[middle:])
        return merge(left,right)


print('*'*80)
print(merge_sort([5,2,8,1,9,3,7,4]))

#           [5,2,8,1,9,3,7,4]
#               /        \
#       [5,2,8,1]       [9,3,7,4]
#        /     \        /       \
#     [5,2] + [8,1]   [9,3] + [7,4]
#       |       |       |       |
#     [2,5] + [1,8]   [3,9] + [4,7]
#       \      /        \       /
#       [1,2,5,8]          [3,4,7,9]
#           \               /
#        [1, 2, 3, 4, 5, 7, 8, 9]
#


def quick_sort(unsorted_list:list[int]) -> list[int]:
    if len(unsorted_list)<=1:
        return unsorted_list

    pivot=unsorted_list[len(unsorted_list)//2]
    left= [i for i in unsorted_list if i < pivot]
    equal=[i for i in unsorted_list if i==pivot]
    right=[i for i in unsorted_list if i>pivot]
    return quick_sort(left)+equal+quick_sort(right)

print('*'*80)
print(quick_sort([5,10,2,7,6,9,3,8,4]))

# pivot== 6
#                            [5,10,2,7,6,9,3,8,4]
#                           /          |        \
#                   [5,2,3,4,1]       [6]      [10,7,9,8]
#                   /    |    \        |      /     |    \
#               [2,1]   [3]    [5,4]   |     [7,8] [9]  [10]
#                 |      |       |     |       |    |     |
#               [1,2]   [3]    [4,5]  [6]    [7,8] [9]   [10]
#                 \       \      |     |      /    /      /
#                  \       \     |     |     /    /      /
#                   \       \    |     |    /    /      /
#                            [5,10,2,7,6,9,3,8,4]


#  A - B
#  |   |
#  C - D

#   A --5--> B --8--> C


friends={
    'Alex': {'Olga','Vitalik'},
    'Anton': {'Valeriy','Vlad'},
    'Olga': {'Alex','Valerij'}
    }

roads={
    'Kyiv':{'Zhytomyr':100,'Poltava':250},
    'Zhytomyr': {'Kyiv':250,'Poltava':350},
    'Poltava': {'Kyiv':250,'Zhytomyr':350}
}

from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    profession: str


def find_closest_person(network,start,profession):
    queue=deque([start])
    visited=set()


    while queue:
        person=queue.popleft()

        if person in visited:
            continue

        visited.add(person)

        if person != start and person.profession == profession:
            return person

        queue.extend(network[person])

    return None


alex=Person('Alex','Developer')
olga=Person('Olga','Student')
anton=Person('Anton','Athlete')
valeriy=Person('Valeriy','Professor')
vlad=Person('Vlad','Developer')


network={
    alex: {olga,anton},
    olga: {alex,valeriy},
    anton: {olga,valeriy},
    valeriy: {olga,vlad},
}

print(find_closest_person(network,alex,'Developer'))

