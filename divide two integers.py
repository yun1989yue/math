'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1: # MIN_INT = -2**31 but MAX_INT = 2**31-1, it can be overflowed
            return 2**31-1
        if divisor == 0: # divisor may be 0
            return 2**31-1 if dividend >=0 else -2**31
        flag = 1 # pole of res
        if dividend < 0: # transform dividend and divisor to positive
            dividend = -dividend
            flag = -1
        if divisor < 0:
            divisor = -divisor
            flag *= -1
        res = 0
        while dividend != 0: # bit manipulation, for remain dividend, find max(divisor*(2*i*)) < dividend and extract it from dividend
            if dividend < divisor:
                break
            temp = divisor
            times = -1
            while temp <= dividend:
                times += 1
                temp <<= 1
            res += 2**times
            dividend -= temp/2
        return res*flag
