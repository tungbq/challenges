"""
# Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        result=""
        vowels = ['a', 'e', 'i', 'o', 'u']
        # convert string to array
        str_arr = [c for c in s]
        str_arr_sort = [c for c in s]
        i=0
        j=len(str_arr) - 1
        while i < j:
            # check if elemenet is not in vowels, move to the next item
            if str_arr[i] not in vowels:
                i += 1
            if str_arr[j] not in vowels:
                j -= 1
            # if both are vowels, swap them.
            if str_arr[i] in vowels and str_arr[j] in vowels:
                tmp = str_arr_sort[i]
                str_arr_sort[i] = str_arr_sort[j]
                str_arr_sort[j] = tmp
                i += 1
                j -= 1
        # convert back to string (in sort)
        for cs in str_arr_sort:
          result += cs
        return result