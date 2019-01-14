#!/usr/bin/python
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        for index,item in enumerate(nums):
            if target-item in dict:
                return [dict[target-item], index]
            else:
                dict[item] = index
    
sol = Solution()
numbers, target = [2, 7, 11, 15], 9
result = sol.twoSum(numbers, target)
print "index1 = %d, index2 = %d" %(result[0],result[1])