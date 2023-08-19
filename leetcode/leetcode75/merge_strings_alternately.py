"""
  You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
  If a string is longer than the other, append the additional letters onto the end of the merged string.
  Return the merged string.

  E.g:
  Input: word1 = "abcd", word2 = "pq"
  Output: "apbqcd"
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      merged_string = None
      if len(word1) == len(word2) or len(word1) < len(word2):
        merged_string = word1 + word2
      else:
        merged_string = word1[:(len(word2))] + word2 + word1[(len(word2)):]
        print("Test")
        print(merged_string)
      return merged_string

    def mergeTwoWord(self, word1: str, word2: str) -> str:
      w1=list(word1)
      w2=list(word2)
      for char in word1:
        print(char)
