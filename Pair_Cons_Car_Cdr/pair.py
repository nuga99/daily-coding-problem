
#!usr/bin/python

'''
Coding problems #5
Serialize and Deserialize Binary Tree
	
Solution : Muhammad Ardivan Satrio Nugroho

Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
returns the first and last element of that pair. 

For example, 
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(left_pair):
	def de_pair(a,b):
		return a
	return left_pair(de_pair)

def cdr(right_pair):
	def de_pair(a,b):
		return b
	return right_pair(de_pair)

if __name__ == '__main__':
	print(car(cons(3, 4)))
	print(cdr(cons(3, 4)))