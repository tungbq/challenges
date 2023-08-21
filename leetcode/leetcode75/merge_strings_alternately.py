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
      word1_len = len(word1)
      word2_len = len(word2)

      if word1_len == word2_len:
        merged_string = self.mergeTwoWords(word1, word2)
      elif word1_len > word2_len:
        w1_to_merge = word1[:(word2_len)]
        w1_remaining = word1[(word2_len):]
        merged_string = self.mergeTwoWords(w1_to_merge, word2) + w1_remaining
      elif word1_len < word2_len:
        w2_to_merge = word2[:(word1_len)]
        w2_remaining = word2[(word1_len):]
        merged_string = self.mergeTwoWords(word1, w2_to_merge) + w2_remaining
      return merged_string

    def mergeTwoWords(self, word1: str, word2: str) -> str:
      list_w1=list(word1)
      list_w2=list(word2)
      merged_words=[]
      for i in range(len(list_w1)):
        merged_words.append(list_w1[i])
        merged_words.append(list_w2[i])
      return "".join(merged_words)
