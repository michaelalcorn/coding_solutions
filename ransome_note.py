"""
RANSOM LETTER

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False
        return True