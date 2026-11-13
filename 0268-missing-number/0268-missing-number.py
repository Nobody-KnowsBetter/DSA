class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # left, right = 0, len(nums)

        # while left < right:

        #     mid = (left + right) // 2

        #     if nums[mid] > mid:
        #         right = mid

        #     else:
        #         left = mid + 1

        # return left


        n = len(nums)
        a = n * (n + 1) // 2
        
        return a - sum(nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna