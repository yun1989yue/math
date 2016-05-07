'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # negative nums are False
            return False
        res = 0
        temp = x
        while temp != 0:
            res *= 10
            res += temp % 10
            temp /= 10
        return res == x
