# def linear_search(sequences: list[int],target: int) -> int:
#     for index, value in enumerate(sequences):
#         if value == target:
#             return index
#
#
# numbers=[1,2,3,4,5,6,7,8,9,10]
# result=linear_search(numbers,10)
# print(result)

def binary_search(sequences: list[int],target: int) -> int:
    low=0
    high=len(sequences)-1
    steps=0


    while low<=high:
        steps+=1
        mid=(low+high)//2
        guess=sequences[mid]
        if guess==target:
            # print(f"Found {target} in {steps} steps")
            return mid
        elif guess>target:
            high=mid-1
        else:
            low=mid+1


sorted_numbers=[1,2,3,4,5,6,7,8,9,10]
result=binary_search(sorted_numbers,5)
# print(result)

#O(n^2)
def find_common(list1,list2):
    result=[]
    for element in list1:
        if element in list2:
            result.append(element)

    return result

# O(n)
def find_common_effective(list1,set_2):
    result=[]
    for element in list1:
        if element in set_2:
            result.append(element)

    return result


sorted_list=[1,2,3,4,5,6,7,8,9,10]
second_list=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
second_set={5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
# print(find_common(sorted_list,second_list))



# O(n^3)
def triple_iterations(number:int):
    for i in range(number):   #1
        for j in range(i+1,number):   #2
            for k in range(j+1,number):   #3
                print(i,j,k)


# O(2^n)
def fibonacci(number:int):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)


# O(n!)
def generate_permutations(input_list:list | str):
    if len(input_list)<=0:
        return [input_list[:]]

    permutations=[]
    for i in range(len(input_list)):
        current= input_list[i]
        rest=input_list[:i]+input_list[i+1:]
        for perm in generate_permutations(rest):
            permutations.append([current] + perm)
    return permutations

# for p in generate_permutations(["a","b","c",'d','e','f']):
#     print(p)







from time import perf_counter
import matplotlib.pyplot as plt


def measure_time(func, *args):
    start = perf_counter()
    func(*args)
    end = perf_counter()
    return end - start



times_linear = []
times_quadratic = []
sizes = []

for n in range(1, 501):
    data_list = list(range(n))
    data_set = set(data_list)

    sizes.append(n)

    times_quadratic.append(measure_time(find_common, data_list, data_set))
    times_linear.append(measure_time(find_common_effective, data_list, data_set))



fig, ax = plt.subplots()
ax.plot(sizes, times_linear, label="Linear")
ax.plot(sizes, times_quadratic, label="Quadratic")

ax.set_xlabel("Input size (n)")
ax.set_ylabel("Time (seconds)")
ax.set_title("Linear vs Quadratic Time")
ax.legend()

fig.savefig("linear.png")
plt.show()


# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n