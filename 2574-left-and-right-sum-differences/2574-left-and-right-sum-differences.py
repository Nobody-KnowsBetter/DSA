class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # left = [0]*n

        # for i in range(1,n):
        #     left[i] = left[i-1] + nums[i-1]

        # right = [0]*n

        # for j in range(n-2, -1, -1):
        #     right[j] = right[j+1] + nums[j+1]
        
        # result = []

        # for z in range(n):
        #     result.append(abs(left[z] - right[z]))
        
        # return result


        left = 0
        right = sum(nums)
        result = []

        for num in nums:
            right -= num
            result.append(abs(left - right))
            left += num

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna