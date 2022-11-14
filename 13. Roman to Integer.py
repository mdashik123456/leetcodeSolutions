#Solution 1:
        
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
             
        i = len(s) - 1
        while i >= 0:
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
            
            i -= 1
            
        return result

#Solution 2:

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0
#         d = {
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000
#         }
        
#         i = 0
#         while (i < len(s)):
#             try:
#                 if d[s[i]] >= d[s[i+1]]:
#                     result += d[s[i]]
#                 else:
#                     r = d[s[i+1]] - d[s[i]]
#                     result += r
#                     i += 1
#             except:
#                 result += d[s[i]]
#             i += 1
             
         
#         return result
        
