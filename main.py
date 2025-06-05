import timeit


def merge(num):

    if len(num) <= 1:
        return num
    left, right = num[: len(num) // 2], num[len(num) // 2 :]

    def sort(left, right):
        leftIndex, rightIndex = 0, 0
        sortedList = []
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                sortedList.append(left[leftIndex])
                leftIndex += 1
            else:
                sortedList.append(right[rightIndex])
                rightIndex += 1
        while leftIndex < len(left):
            sortedList.append(left[leftIndex])
            leftIndex += 1

        while rightIndex < len(right):
            sortedList.append(right[rightIndex])
            rightIndex += 1
        return sortedList

    return sort(merge(left), merge(right))


def insert(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and key < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    return num


print(timeit.timeit(lambda: merge([5, 2, 9, 1, 5, 6]), number=100))
print(timeit.timeit(lambda: insert([5, 2, 9, 1, 5, 6]), number=100))
print(timeit.timeit(lambda: sorted([5, 2, 9, 1, 5, 6]), number=100))
