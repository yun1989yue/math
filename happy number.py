'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
'''
Hashtable O(n) time O(n) space
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        used = {n:1}
        while n != 1:
            temp = 0
            while n != 0:
                temp += (n%10)**2
                n /= 10
            n = temp
            if n in used:
                return False
            else:
                used[n] = 1
        return True
        
'''
two pointers: O(n) time O(1) space
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        slow = n
        fast = self.squareSum(slow)
        while slow != fast:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)
        return slow == 1
        
    def squareSum(self, n):
        if n == 1:
            return n
        temp = 0
        while n != 0:
            temp += (n%10)**2
            n /= 10
        return temp
