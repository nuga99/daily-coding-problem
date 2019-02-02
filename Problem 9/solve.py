#!/usr/bin/python
'''
Problem #9

Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

'''    

def solve(arr):
    include= 0
    exclude= 0
    top_ans = 0
    
    for i in range(len(arr)):
        if(include < exclude): top_ans = exclude
        else:  top_ans = include
        
        # print("top ans: "+str(top_ans)+"\n=======")
        include = exclude+arr[i]
        exclude = top_ans

        # print("include: "+str(include))
        # print("exclude: "+str(exclude))
        # print("=======")

    return "Ans:"+str(max(include,exclude))
        


if __name__ == "__main__":

    data = [5,1,1,5]
    print(solve(data))