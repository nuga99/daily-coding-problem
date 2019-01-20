#!/user/bin/python

'''
	Coding problems 4
	Find the lowest positive integer that does not exist in the array. 
	The array can contain duplicates and negative numbers as well.

	Complexity : O(n) using Set
	
	Solution : Muhammad Ardivan Satrio Nugroho
'''


#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def find_missing_positive_num(arr):

	# because there's a duplicate make sure that each numbers are unique
	uniq_num_arr = list(set(arr))

	# filter just the positive number
	uniq_positive_number = list(filter(lambda x : x>0, uniq_num_arr))
	
	# sort the number list and the max
	max_number = sorted(uniq_positive_number)[-1]

	for i in range(1,max_number):
		if i not in uniq_positive_number:
			print(i)
			return

	print(max_number+1)


if __name__ == '__main__':

	data = [3,4,-1,1]
	find_missing_positive_num(data)
