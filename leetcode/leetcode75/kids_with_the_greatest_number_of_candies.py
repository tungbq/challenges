"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = self.determineMaxCandies(candies)
        result = []
        for candy in candies:
          if candy + extraCandies >= maxCandies:
            result.append(True)
          else:
            result.append(False)
        return result

    def determineMaxCandies(self, candies: list[int]) -> int:
      maxCandies = candies[0]
      for candy in candies:
         if candy > maxCandies:
            maxCandies = candy
      return maxCandies