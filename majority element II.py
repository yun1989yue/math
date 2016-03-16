'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

'''
'''
Idea:
randomly remove 3 different numbers, if a number appears more than n/3 times, it must be left, while a number left does not mean it is 
majority, need to check whether the result is correct (e.g. 1,2,3,1,2,3,4 notice that there maybe no solution at all)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        first = nums[0]
        second = -1
        count1 = 1
        count2 = 0
        for i in xrange(1, len(nums)):
            if count1 == 0:
                if count2 != 0 and nums[i] == second:
                    count2 += 1
                else:
                    first = nums[i]
                    count1 = 1
            elif count2 == 0:
                if count1 != 0 and nums[i] == first:
                    count1 += 1
                else:
                    second = nums[i]
                    count2 = 1
            else:
                if nums[i] == first:
                    count1 += 1
                elif nums[i] == second:
                    count2 += 1
                else:
                    count1 -= 1
                    count2 -= 1
        res = []
        if count1 != 0:
            count1 = 0
            for i in xrange(len(nums)):
                if nums[i] == first:
                    count1 += 1
            if count1 > len(nums)/3:
                res.append(first)
        if count2 != 0:
            count2 = 0
            for i in xrange(len(nums)):
                if nums[i] == second:
                    count2 += 1
            if count2 > len(nums)/3:
                res.append(second)
        return res
        
'''
The code above is a little redundant, we can make it more concise
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        first = 0
        second = 1 # just need to make sure that first != second
        count1 = 0
        count2 = 0
        for i in xrange(len(nums)):
            if nums[i] == first: 
                count1 += 1
            elif nums[i] == second:
                count2 += 1
            elif count1 == 0: # new value will be changed only when it is neither first or second, hence first will never == second 
                first = nums[i] 
                count1 += 1
            elif count2 == 0:
                second = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        count1 = 0
        count2 = 0
        for i in xrange(len(nums)):
            if nums[i] == first:
                count1 += 1
            elif nums[i] == second:
                count2 += 1
        if count1 > len(nums)/3:
            res.append(first)
        if count2 > len(nums)/3:
            res.append(second)
        return res
