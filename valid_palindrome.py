class Solution:
    def isPalindrome(self, s: str) -> bool:
        char=""
        for a in s:
            if a.isalnum():
                char+=a.lower()
        if  char==char[::-1]:
            return True
        return False
      
        
  

