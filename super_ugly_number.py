'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13,
14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
'''
'''
Basic Idea: 
1) every ugly number is a multiple of smaller ugly number and some prime
2) set a pointer for each prime starting at 0, if res[i]*current_prime is chosen to be next ugly number, the smallest ugly number that have 
not added to the res is res[i+1]*current_prime
'''
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # N pointers 
        # O(n*len(primes)) time O(len(primes)) space
        if n == 1:
            return 1
        pointers = [0]*len(primes) # set a pointer for each prime
        res = [1]
        for i in xrange(n-1):
            temp = 2 ** 31 - 1 # next smallest ugly number
            for j in xrange(len(primes)):
                if res[pointers[j]]*primes[j] < temp:
                    temp = res[pointers[j]]*primes[j]
            for j in xrange(len(primes)): # notice that there may be more than one primes that can contribute to next ugly number, need # to avoid abundance
                if res[pointers[j]]*primes[j] == temp:
                    pointers[j] += 1
            res.append(temp)
        return res[-1]
