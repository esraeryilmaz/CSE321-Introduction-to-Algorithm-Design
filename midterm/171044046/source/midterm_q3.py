# Midterm - Q3
# Improved QuickSort with using InsertionSort.

def QuickInsertionSort(arr, low, high):
	while high>low:
		if high-low <10:
			InsertionSort(arr, low, high)
			break
		else:
			pivot = Partition(arr, low, high)
			if pivot-low<high-pivot:
				QuickInsertionSort(arr, low, pivot-1)
				low = pivot + 1
			else:
				QuickInsertionSort(arr, pivot + 1, high)
				high = pivot-1

def Partition(arr, low, high):
	pivot = arr[high]
	i = j = low
	for i in range(low, high):
		if arr[i]<pivot:
			arr[i], arr[j]= arr[j], arr[i]
			j=j+1
	arr[j], arr[high]= arr[high], arr[j]
	pivot = j
	return pivot

def InsertionSort(arr, low, n):
	for i in range(low + 1, n + 1):
		current = arr[i]
		pos = i
		while pos>low and arr[pos-1]>current:
			arr[pos]= arr[pos-1]
			pos = pos-1
		arr[pos] = current


# Driver code
arr = [ 10, 23, 17, 72, 18, 49, 55, 44, 15, 32, 29, 41, 39, 65, 2, 99, 200, 1 ]
QuickInsertionSort(arr, 0, 17)
print(arr)
