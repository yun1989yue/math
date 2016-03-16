'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''
'''
Idea: O(n) time O(1) space
randomly removes two different elements in pairs
* notice that the title said there must be a solution, otherwise this method can not be used, e.g. 1,2,1,2,1,2,3 then 3 will be returned
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        count = 1
        for i in xrange(1,len(nums)):
            if count == 0:
                count = 1
                res = nums[i]
            else:
                if res == nums[i]:
                    count += 1
                else:
                    count -= 1
        return res
'''
straight forward ideas:
1) use hash table to count every element O(n) time O(n) space
2) for each element, count its numbers
'''
