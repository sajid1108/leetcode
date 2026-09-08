class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left , right = 0 , len(numbers) - 1

        while left < right:
            sumi = numbers[left] + numbers[right]
            if sumi == target:
                return [left+1,right+1]
            elif sumi < target:
                left += 1 
            else:
                right -= 1
        return [-1,-1]