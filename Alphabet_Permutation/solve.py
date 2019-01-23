'''
Coding Problems #7

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. 
For example, '001' is not allowed.

'''

import itertools

def solve(encoded_message):

	# create list/arr for all alphabet
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	length_string = len(str(encoded_message))

	if(length_string == 1 ): 

		if(int(encoded_message[0])!=0): return 1
		else: return 0

	if(length_string == 2):

		counter = 0
		if(int(encoded_message[0]!=0) and int(encoded_message[1])!=0):
			counter+=1
		if chr(97+int(''.join(encoded_message))) in alphabet:
			counter+=1
		return counter

	if(length_string > 2):
		counter = 0
		if(int(encoded_message[0]!=0)):
			counter+=solve(encoded_message[1:])

		# strings starts from [0,1]
		if chr(97+int(''.join(encoded_message[0:2]))) in alphabet:
			counter+=solve(encoded_message[2:])
		return counter



	
if __name__ == '__main__':
	print(solve('111'))
