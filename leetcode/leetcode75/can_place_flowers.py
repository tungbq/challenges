"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        skip_next_slot = False
        for i in range(len(flowerbed)):
          # reset the skip_next_slot
          if skip_next_slot:
            skip_next_slot = False
            continue

          # exit if there is n is empty
          if n == 0:
            return True

          # skip next slot if current valid slot is 0
          if flowerbed[i] == 0:
            n -= 1
            skip_next_slot = True
          else:
            continue
        return False
