#!/usr/bin/python
'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
'''

recordId = {}
def solve(order_id,i):
    record(order_id)
    get_last(i)

# using set
def record(order_id_list):
    orderBuy = 0
    for orderBuy,order_id in enumerate(order_id_list):
        recordId[orderBuy] = order_id.rstrip() # remove trailing whitespace and tabs \n \t
    

def get_last(i):
    print recordId.get(i,"There's no id")
    

if __name__ == "__main__":
    logsRecord = open('logs.txt','r')
    solve(logsRecord,11)