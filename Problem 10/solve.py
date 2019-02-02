#!/usr/bin/python

'''
Problems #10

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

'''

import schedule
import time

def setTime(second):
    return second/1000

def worker():
    print("I love you")

# cron calling Method
def cronScheduler(second):
    schedule.every(setTime(second)).minutes.do(worker)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    timeWork = int(input())
    cronScheduler(timeWork)