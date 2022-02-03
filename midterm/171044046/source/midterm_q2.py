# Midterm - Q2
# I write integer array but in the function I consider array elements 
# like they are binary numbers.
# I am stuck while finding most significant bit of the numbers.
# So actual python code doesn't work for that reason.

def FindAbsentInteger(arr ,bits):
	if (bits==0):
		return 0

	# Stuck here !!
	for i in range(0, bits) :
		left_partition = [i for i in len(arr) if BitAt(arr[i], n) == 1]
		right_partition = [i for i in len(arr) if BitAt(arr[i], n) == 0]

	if(len(left_partition) <= len(right_partition)):
		return(FindAbsentInteger(right_partition, bits -1)) << 1|0;
	else:
		return(FindAbsentInteger(left_partition, bits -1)) << 1|1; 


def BitAt(n, bit):
	return (n>>bit) & 1

# Driver code 
arr = [ 1, 2, 3, 4, 5, 7, 8 ]
FindAbsentInteger(arr, 4)
