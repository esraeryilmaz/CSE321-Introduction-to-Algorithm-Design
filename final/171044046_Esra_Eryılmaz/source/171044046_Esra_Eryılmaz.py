# Author : Esra Eryılmaz - 171044046
# CSE 321
# Final


################### Question 1 ###################
# This function finds the longest palindromic substring using dynamic programming.
def MaxLengthSubarray(string) :
    n = len(string)
    begins = 0
    ends = 1

    # Creating 2D boolean table.
    table = [False] * n
    for i in range (n):
        table[i] = [False] * n

    # Base case: Every character in a string is a palindrome.
    for i in range (0,n):
        for j in range (0,n):
            if i == j:
                table[i][j] = True

    # Base case: Same adjacent characters in a string make a palindrome.
    for i in range (n-1):
        if (string[i] == string[i+1]):
            table[i][i+1] = True

    # Loop from string length of size 3 upto the n.
    for length in range (3, n+1):
        for i in range (0, n - length + 1):
            j = i + length - 1
            if (string[i] == string[j] and table[i+1][j-1] == 1):
                table[i][j] = True
                if (length > ends):
                    begins = i
                    ends = length

    return string[begins : begins + ends]


################### Question 2 ###################
# Quick Sort
def QuickSort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        QuickSort(arr, l, pivot-1)
        QuickSort(arr, pivot+1, h)

# partition for QuickSort
def partition(arr, l, h):
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
    swap(arr, j, l)
    return j

# Swap function
def swap(arr, position1, position2):
    temp = arr[position1]
    arr[position1] = arr[position2]
    arr[position2] = temp


################### Question 3 ###################
# This function makes the advertisement placement such that you maximize your total money earned.
def MaxEarnedMoney(M, x, r, n, restriction) :
    # To store maximum money earned at each km. 
    maxEarned = [0] * (M + 1) 
    line = 0;

    for i in range(1, M + 1) :
        # Checking the all advertisements are already placed or not.
        if (line < n) :
            if (x[line] != i) :
                maxEarned[i] = maxEarned[i - 1]

            # Either take current ad or ignore current ad.
            else :
                if (i <= restriction) :
                    maxEarned[i] = max(maxEarned[i - 1], r[line])
                else :
                    maxEarned[i] = max(maxEarned[i - restriction - 1] + r[line], maxEarned[i - 1]);
                line = line + 1
        else :
            maxEarned[i] = maxEarned[i - 1]

    return maxEarned[M]


################### Question 4 ###################



################### Question 5 ###################
# This functions finds number of inversions with specific case
def NumberOfInversions(arr):
    if(len(arr) <= 1):
        return arr, 0
    else:
        mid = int(len(arr)/2)
        left, a = NumberOfInversions(arr[:mid])
        right, b = NumberOfInversions(arr[mid:])
        res, c = UsingMerge(left, right)
        return res, (a + b + c)

# Uses divide and conquer algorithm
def UsingMerge(left, right):
    result = []
    count = 0
    i,j = 0,0

    # First pass to count number of inversions
    while(i < len(left) and j < len(right)):
        if(left[i] > 2*right[j]):	#special case
            count += len(left)-i
            j = j + 1
        else:
            i = i + 1

    i,j = 0,0
    # Merge two sorted arrays
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    while(left[i:] or right[j:]):
        if(left[i:]):
            result.append(left[i])
            i = i + 1
        if(right[j:]):
            result.append(right[j])
            j = j + 1
    return result, count


# Driver code
def main():
    print("***********  Question 1  ***********:")
    q1_arr = ["sekabakn", "yaya"]
    for string in (q1_arr):
        print("Longest Substring : " + MaxLengthSubarray(string))

    print("\n***********  Question 2  ***********:")
    q2_arr = [10, 7, 8, 4] 
    n = len(q2_arr) 
    QuickSort(q2_arr, 0, n-1) 
    intervals = [[1,2],[2,2],[3,3],[3,4]]
    for i in (intervals):
        print(q2_arr[i[0]])

    print("\n***********  Question 3  ***********:")
    M = 22
    q3_x = [5, 8, 10, 12, 16]
    r = [5, 4, 2, 6, 1]
    restriction = 4
    print("Max earned money is : ", MaxEarnedMoney(M, q3_x, r, len(q3_x), restriction))

    print("\n***********  Question 4  ***********:")


    print("\n***********  Question 5  ***********:")
    q5_arr = [10, 5, 4, 1, 8]
    print("Number of inversions : " ,NumberOfInversions(q5_arr)[1]) 


if __name__=="__main__": 
    main()
