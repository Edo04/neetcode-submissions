class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_comp = {}
        t_comp = {}
        for s_word in s:
            if s_word in s_comp:
                s_comp[s_word] += 1
            else:
                s_comp[s_word] = 1
        for t_word in t:
            if t_word in t_comp:
                t_comp[t_word] += 1
            else:
                t_comp[t_word] = 1
        if s_comp == t_comp:
            return True
        else:
            return False