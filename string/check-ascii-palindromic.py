def charToBinary(value):
    result=""
    value=ord(value)
    for i in range(8):
        if value & 1:
            result='1'+result
        else:
            result='0'+result
        value=value >> 1
    return result
class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_string=""
        for i in range(len(s)):
            binary_string+=charToBinary(s[i])
        #palindrom or not
        l=0
        h=len(binary_string)-1
        while l <= h :
            if binary_string[l]!=binary_string[h]:
                return False
            l+=1
            h-=1
        return True
                
        