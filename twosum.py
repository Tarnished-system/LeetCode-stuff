class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return  # Return value if no solution is found

# Create an instance of the class
sol = Solution()

# Test the function with some values
result = sol.twoSum([2, 7, 11, 15], 9)

# Print the result
print(result)
 
        