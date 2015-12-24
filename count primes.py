'''
Count the number of prime numbers less than a non-negative number, n.
'''
'''
Arr: O((1/2+1/3+...+1/n)*n) time O(n) space
'''
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        bl = [1]*(n) # notice that count exclude n
        for i in xrange(2, int(math.sqrt(n))+1): # need to explore until sqrt(n) + 1 rather than sqrt(n)
            if bl[i] == 1:
                for j in xrange(i**2, n, i):
                    bl[j] = 0
        res = 0
        for i in xrange(2, len(bl)):
            if bl[i] == 1:
                res += 1
        return res
