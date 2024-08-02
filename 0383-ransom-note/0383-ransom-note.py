class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
#         if len(ransomNote) > len(magazine):
#             return False
        
#         dictionary = {}
        
#         for i in magazine:
#             if i not in dictionary:
#                 dictionary[i] = 1
#             else:
#                 dictionary[i] += 1
        
#         for i in ransomNote:
#             if i in dictionary and dictionary[i] > 0:
#                 dictionary[i] -= 1
#             else:
#                 return False
            
#         return True

# 2nd ...

        if len(ransomNote) > len(magazine):
            return False
        
        for character in magazine:
            ransomNote = ransomNote.replace(character,'',1)
        
        return ransomNote == ''
            