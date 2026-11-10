class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a = None
        # b = 0

        # for i in nums:
        #     if b == 0:
        #         a = i
        #     if i == a:
        #         b += 1
        #     b -= 1
        # return a

class Solution(object):

  def majorityElement(self, nums):
    a = None
    b = 0

    for i in nums:
      if b == 0:
        a = i

      if i == a:
        b += 1
      else:
        b -= 1  # <--- Indented under `else`

    return a

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna