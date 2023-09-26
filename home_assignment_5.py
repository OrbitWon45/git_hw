
# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

def selection_sort(arr: list):
    for i in range(len(arr)):
        max = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max]:
                max = j
        arr[i], arr[max] = arr[max], arr[i]
    return arr
arr_1 = [7, 2, 8, 3, 5, 9]
print(selection_sort(arr_1))

# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr_2 = [7, 2, 8, 3, 5, 9]
print(bubble_sort(arr_2))

# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr_3 = [7, 2, 8, 3, 5, 9]
print(insertion_sort(arr_3))