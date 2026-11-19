class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = 0 
        b = 0
        n = len(needle)

        while a < n:
            if b >= len(haystack):
                return -1
            if haystack[b] == needle[a]:
                a += 1
            else:
                b = b - a
                a = 0
            
            b += 1

        if a == n:
            return b - n
        else:
            return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna