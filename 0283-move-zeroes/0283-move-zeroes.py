class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        a, b = 0, len(nums)-1

        while a < b:
            if nums[a] == 0:
                nums.pop(a)
                nums.append(0)
                a -= 1
                b -= 1
            a += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna