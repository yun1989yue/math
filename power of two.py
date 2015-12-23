'''
Given an integer, write a function to determine if it is a power of two.
'''
'''
Brute Force: O(logn) time O(1) space
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n % 2 == 0: # 1 is 2**0
            n /= 2
        return n == 1
        
'''
bit manipulation O(1) time O(1) space
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >0 and not n&(n-1)
