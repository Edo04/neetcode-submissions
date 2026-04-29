class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_comp = {}
        t_comp = {}
        for i in range(len(s)):
            if s[i] in s_comp:
                s_comp[s[i]] += 1
            else:
                s_comp[s[i]] = 1
            if t[i] in t_comp:
                t_comp[t[i]] += 1
            else:
                t_comp[t[i]] = 1
        if s_comp == t_comp:
            return True
        else:
            return False