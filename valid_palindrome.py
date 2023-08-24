"""
VALID PALINDROME

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

# NEED TO IMPROVE THIS 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        s.replace(" ", "")
        print(s)

        if len(s) < 2:
            return True
        # even
        elif len(s) % 2 == 0:
            right = len(s) - 1
            left = 0
            while left < right:
                if s[right] != s[left]:
                    return False
                left+=1
                right-=1
        # odd 
        else: 
            pivot = ((len(s) + 1) / 2)-1
            left_string = s[0:pivot]
            right_string = s[pivot+1:len(s)]
            right_string = right_string[::-1]
            print(left_string)
            print(right_string)

            if left_string != right_string:
                return False
        return True
