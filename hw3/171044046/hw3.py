# Author : Esra Eryılmaz
# CSE 321
# HW3 - Question 4


import random
count = 0   # for counting swap

# Insertion Sort
def InsertionSort(arr):
    global count
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1
            count = count + 1
        arr[j+1] = key


# Quick Sort
def QuickSort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        QuickSort(arr, l, pivot-1)
        QuickSort(arr, pivot+1, h)


# partition for QuickSort
def partition(arr, l, h):
    global count
    pivot = arr[l]
    i = l + 1
    j = h
    flag = 1
    while flag:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while arr[j] >= pivot and j >= i:
            j = j - 1
        if j < i:
            flag = 0
        else:
            swap(arr, i ,j)
            count = count + 1 
    swap(arr, j, l)
    count = count + 1
    return j


# Swap function
def swap(arr, position1, position2):
    temp = arr[position1]
    arr[position1] = arr[position2]
    arr[position2] = temp


# Driver code
def main():
    global count
    list1 = [random.randint(i, i + 15) for i in range(50)]
    print("Insertion Sort")
    print("Unsorted : ", list1)
    InsertionSort(list1)
    print("Sorted : ", list1)
    print("Number of swaps: ", count)

    count = 0
    list2 = [random.randint(i, i + 15) for i in range(50)]
    print("\nQuick Sort")
    print("Unsorted : ", list2)
    QuickSort(list2, 0, len(list2) - 1)
    print("Sorted : ", list2)
    print("Number of swaps: ", count)


if __name__=="__main__": 
    main()