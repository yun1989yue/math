'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        return num == 1
'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''
'''
Brute force: O(nlogn) time O(1) space TLE
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 7:
            return n
        cur = 6
        for i in xrange(n - 6):
            cur += 1
            find = 0
            while find == 0: # worst case logn time, 2^n
                explore = cur
                while explore % 5 == 0:
                    explore /= 5
                while explore % 3 == 0:
                    explore /= 3
                while explore % 2 == 0:
                    explore /= 2
                if explore == 1:
                    find = 1
                else:
                    cur += 1
        return cur
        
'''
D.P. O(n) time O(n) space
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        two = 0
        three = 0
        five = 0
        for i in xrange(n-1):
            nextNum = min(res[two]*2, res[three]*3, res[five]*5)
            res.append(nextNum)
            if nextNum == res[two]*2:
                two += 1
            if nextNum == res[three]*3:
                three += 1
            if nextNum == res[five]*5:
                five += 1
        return res[-1]
