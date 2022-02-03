# Author : Esra Eryılmaz
# CSE 321
# HW5


# Question 1
def SubsetSum(set, n, sum):
    subset =([[False for i in range(sum + 1)]
            for i in range(n + 1)])

    for i in range(n + 1):
        subset[i][0] = True

    for i in range(1, sum + 1):
        subset[0][i]= False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-set[i-1]])

    return subset[n][sum]


# Question 2
def SmallestSumPath(A):
    arr = [None] * len(A)
    n = len(A) - 1

    for i in range(len(A[n])):
        arr[i] = A[n][i]

    for i in range(len(A) - 2, -1,-1):
        for j in range( len(A[i])):
            arr[j] = A[i][j] + min(arr[j], arr[j + 1]);

    print("Smallest sum path from the triangle : " ,arr[0])


# Question 3
def KnapsackProblem(n, W, weight, values):
    dummy = [0] * (W + 1)
    arr = [dummy.copy() for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif weight[i - 1] <= j:
                arr[i][j] = max(values[i - 1] + arr[i - 1][j - weight[i - 1]], arr[i - 1][j])
            else:
                arr[i][j] = arr[i - 1][j]

    res = arr[n][W]
    w = W

    print("Elements of the Knapsack : ")
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == arr[i - 1][w]:
            continue
        else:
            print (weight[i - 1], end = " ")

            res = res - values[i - 1]
            w = w - weight[i - 1]


# Driver code
def main():
    A = [2, 3, -5, -8, 6, -1]
    sum = 0
    if (SubsetSum(A, len(A), sum) == True):
        print("Found a subset")
    else:
        print("No subset")

    B = [[2 ],
         [5, 4 ],
         [1, 4, 7 ],
         [8, 6, 9, 6]]
    SmallestSumPath(B)

    values = [ 10, 4, 3 ]
    weight = [ 5, 4, 2 ]
    W = 9
    KnapsackProblem(len(values), W, weight, values)


if __name__=="__main__": 
    main()
