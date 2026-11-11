class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n = str(n)
        # a = set(n)
        # total = 0
        # for i in a:
        #     m = 0
        #     l = 0
        #     for j in n:
        #         if i == j:
        #             m += 1
        #     l = int(i)*m
        #     total += l
        # return total
        total = 0
        n = str(n)
        for i in n:
            total += int(i)
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna