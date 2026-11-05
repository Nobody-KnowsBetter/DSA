class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        a = 0
        arr1.sort()
        arr2.sort()
        j = 0
        l = len(arr2)

        for i in arr1:
            
            while j < l and arr2[j] < i - d:
                j += 1

            
            if j < l and arr2[j] <= i + d:
                continue

            a += 1
        return a


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna