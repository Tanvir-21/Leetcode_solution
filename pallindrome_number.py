class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            False
        
        else:
            reverse_result = 0
            temporary = x 
            
            while(temporary > 0):
                
                remainder = temporary % 10
                reverse_result = reverse_result*10 + remainder 
                
                temporary = temporary //10 
                
                
            
            if x == reverse_result:
                return True 
            else:
                return False
