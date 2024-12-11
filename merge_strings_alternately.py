word1 = "abcd"
word2 = "pq"

#  If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      merged_strings = ""
      removed_chars = ""
            
      if len(word1) != len(word2):
        larger_string = word1 if len(word1) > len(word2) else word2
        len_difference = abs(len(word1) - len(word2))
        if larger_string == word1:
            word1 = word1[:-len_difference]
        else:
            word2 = word2[:-len_difference]
        
        removed_chars = larger_string[-len_difference:]
        
      for i in range(len(word1)):
        merged_strings += word1[i] + word2[i]
      
      # char_list = list(word1 + word2)
      # random.shuffle(char_list)
      # merged_strings = ''.join(char_list)
      
      if removed_chars:
        merged_strings += removed_chars
      
      return merged_strings
      

result = Solution.mergeAlternately(Solution, word1, word2)
print(result)