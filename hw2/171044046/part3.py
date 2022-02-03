# Author : Esra Eryılmaz
# CSE 321
# HW2 - Question 3


def QuickSort(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pivot = Partition(arr, low, high)
		QuickSort(arr, low, pivot-1)
		QuickSort(arr, pivot+1, high)


# This function takes last element as pivot
def Partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]

	for j in range(low, high):

		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


def FindProductPair(arr,size,numb):
    begin = 0
    end = 5

    while begin<end :
        product = arr[begin]*arr[end]
    
        if product == numb:
            print(arr[begin],arr[end])
        if product < numb:
            begin +=1
        else:
            end -=1

# Driver code
def main():
    arr = [1,2,3,6,5,4]
    size = len(arr)
    desiredNumb = 6

    QuickSort(arr, 0, size-1)
    print(arr)
    FindProductPair(arr,size,desiredNumb)


if __name__=="__main__": 
    main()