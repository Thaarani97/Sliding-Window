#TC - O(n)
#SC - O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        global_max = 0
        temp = set()
      
        while r < len(s):
            if s[r] not in temp:
                temp.add(s[r])
                              
            else:
                global_max = max(global_max, r-l)
                l = l+1
                r = l
                temp = set()
                temp.add(s[l])     
                
            r = r+1
            
        global_max = max(global_max, r-l)
            
        return global_max