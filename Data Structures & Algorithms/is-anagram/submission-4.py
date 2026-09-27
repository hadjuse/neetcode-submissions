class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for char1 in s:
            dict_s.update({char1:0})

        for char2 in t:
            dict_t.update({char2:0})
        
        for char1 in s:
            dict_s[char1] += 1 
        for char2 in t:
            dict_t[char2] += 1
        print(dict_s, dict_t)
        if dict_s == dict_t:
            return True
        return False