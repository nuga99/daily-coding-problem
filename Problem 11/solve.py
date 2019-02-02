#!usr/bin/python

'''
Problems #11
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
'''

def solve(givenQuery,arr):
    arrSamePrefix = []
    setOfStrings = set(arr)
    for string in setOfStrings:
        if(givenQuery in string[0:len(givenQuery)]):
            arrSamePrefix.append(string)

    if(arrSamePrefix != []): return arrSamePrefix
    return "There's no data with it"

if __name__ == "__main__":
    queryString = input()
    data = ['dog', 'deer', 'deal', 'lede','desqueen']
    print(solve(queryString,data))