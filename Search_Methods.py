# Alex Bello
# 4/13/2020
# Methods used for Exam 2's question


# This method defines how the bubble sort works
def bubble_sort(Sorting_List):
    for i in range(len(Sorting_List)):
        for j in range(len(Sorting_List) - 1):
            if Sorting_List[j] > Sorting_List[j+1]:
                Sorting_List[j], Sorting_List[j+1] = Sorting_List[j+1], Sorting_List[j]


# Defines the selection sort method
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Thi selects the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Places the smallest value at the front
        # of the sorted part of the list
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


# Defines the insert sort method
def insertion_sort(arr):

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Moves the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = cursor

    return arr


# defines how the merge_sort methods works
def merge_sort(arr):
    # splits the last array
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # recurisvely merge_sorts on both halfs of the array
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merges both sides together
    return merge(left, right, arr.copy())


# This will define how the merge works
def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sorts each and places them into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            array[pivot_idx], array[begin] = array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

        return quick_sort_recursion(array, begin, end)
