"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not). 
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr_s=list(s)
        arr_t=list(t)
        i, j = 0, 0
        arr_mid = []
        while i < len(arr_s) and j < len(arr_t):
            if arr_s[i] == arr_t[j]:
                arr_mid.append(arr_s[i])
                i += 1
                j += 1
            else:
                j += 1

        if arr_mid == arr_s:
            return True
        else:
            return False
