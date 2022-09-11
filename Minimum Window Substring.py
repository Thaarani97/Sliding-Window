#TC - O(s+t)
#SC - O(s+t)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        thmap = {}
        # hmap to keep track of all the unique char in t
        for ch in t:
            if ch in thmap:
                thmap[ch]+= 1
            else:
                thmap[ch]= 1
        shmap = {}
        start = 0
        minimum = len(s)+1
        min_substr = ""
        required = len(thmap)
        for end in range(len(s)):
            if s[end] not in shmap:
                shmap[s[end]]=1  
            else:
                shmap[s[end]]+=1
           
            if s[end] in thmap and shmap[s[end]] == thmap[s[end]]: # comparing the occurance of the char
                required-=1
                
            while start<=end and required == 0:
                if minimum > end-start+1:
                    minimum = end-start+1
                    min_substr = s[start:end+1]
                
                shmap[s[start]]-=1
                if s[start] in thmap and shmap[s[start]] < thmap[s[start]]:
                    required+=1
                
                start+=1
         
        return min_substr