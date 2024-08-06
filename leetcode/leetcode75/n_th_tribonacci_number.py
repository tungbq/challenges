"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
"""

class Solution:
    def tribonacci(self, n: int, calculated = {}) -> int:
        if n == 0:
          calculated[n] = 0
          return calculated[n]
        elif n == 1:
          calculated[n] = 1
          return calculated[n]
        elif n == 2:
          calculated[n] = 1
          return calculated[n]
        else:
          if n in calculated:
            return calculated[n]
          else:
            calculated[n] = self.tribonacci(n-1, calculated) + self.tribonacci(n-2, calculated) + self.tribonacci(n-3, calculated)
            return calculated[n]
