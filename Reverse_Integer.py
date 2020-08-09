class Solution:
    def reverse(self, x: int) -> int:
        reverse_result = 0
        
        if x > 0:
            while(x>0):
                remainder = x % 10
                reverse_result = reverse_result*10 + remainder 
                
                x = x//10
                
            if reverse_result < 2**31-1:
                return reverse_result 
            else:
                return 0
        if x < 0:
            while(abs(x) > 0):
                remainder_new = abs(x) % 10
                reverse_result = reverse_result * 10 + remainder_new 
                x = abs(x) // 10
            
            if -reverse_result > -2**31:
                return -reverse_result
            else:
                return 0
        if x == 0:
            return x
