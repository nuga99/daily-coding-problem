#!/user/bin/python

'''
	Coding problems 2
	Two sum checker from array / list
	Complexity : O(n)
	
	Solution : Muhammad Ardivan Satrio Nugroho
'''


# Unefficient Solution using division O(n)

def solve_multiply_by_div(arr):

	new_list = []
	multiply = 1
	counter = 0
	for i in arr:
		multiply*=i

	for i in range(1,len(arr)+1):
		new_list.append(multiply//i)

	print(new_list)


# Most efficient solution
# def solve_multiply_by_index(arr):

# 	# initialize new list to append new dat
# 	new_list = []
# 	multiply_left = 1
# 	multiply_right = 1
# 	total = 1
# 	idx_left = 0
# 	idx_right = len(arr)-1
# 	counter_flag_L = 0
# 	counter_flag_R = 0

# 	if arr == [] : 
# 		print("There's no data")

# 	else:

# 		for i in range(len(arr)):
# 			if(i == counter):
# 				multiply_right *= arr[i] 




if __name__ == '__main__':

	data = [11,5,7,13,21]
	#solve_multiply_by_index(data)
	solve_multiply_by_div(data)