#!/user/bin/python

'''
	Coding problems 1
	Two sum checker from array / list
	Complexity : O(n)
	
	Solution : Muhammad Ardivan Satrio Nugroho
'''

def two_sum_checker(arr, sum):
	
	# initialize flag
	left = 0;
	right = len(arr)-1
	get_two_number = []

	# sort the number first
	arr.sort()

	# do some check of number
	while(left < right):
		sum_of_two_number = arr[left] + arr[right] 

		if(sum_of_two_number == sum):
			get_two_number.append(arr[left])
			get_two_number.append(arr[right])
			break

		elif(sum_of_two_number < sum):
			left+=1

		else:
			right-=1

	# check if number not found
	if get_two_number == []:
		print("There's no number satisfied this question!")
		return

	print("Sorted list: "+str(arr))
	print("The two numbers arr: "+ str(get_two_number[0])+" "+str(get_two_number[1]))


if __name__ == '__main__':

	data = [11,21,33,100,31,6,7]
	sum_you_want = 13
	two_sum_checker(data,sum_you_want)

