#!/usr/bin/python

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.

Upgrade to premium and get in-depth solutions to every problem. 
Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! 
As always, shoot us an email if there's anything we can help with!
'''
import random

# using uniform probability
# Credits : https://www.dailycodingproblem.com/blog/how-to-pick-a-random-element-from-an-infinite-stream/
def solve(streamElements):
    random_element = None
    line = 0
    # enumerate each line so with number
    for strings in streamElements:
        line+=1
        if line == 0 : 
            random_element = strings
        elif random.randint(1, line+1) == 1:
            random_element = strings

    return random_element

if __name__ == "__main__":
    # some stream data like file.txt or using terminal input
    streamInput = open('file.txt','r')
    try:
        #solver
        print(solve(streamInput))
    except:
        "No stream data"
