class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        b = n[::-1]
        a = abs(int(n) - int(b))
        return a

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna