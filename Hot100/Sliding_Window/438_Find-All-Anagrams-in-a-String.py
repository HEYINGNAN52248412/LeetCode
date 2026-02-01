#maintaining a sliding window whose length is len(p), and its char frequency map
#always check if two frequency map are equal to each other
#if so, add it to the answer
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_map = {}
        p_map = {}
        ans = []

        for i in range(len(p)):
            if p[i] not in p_map:
                p_map[p[i]] = 1
                continue
            p_map[p[i]] += 1


        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1
            
            if i >= len(p):
                s_map[s[i-len(p)]] -= 1
                if s_map[s[i-len(p)]] == 0:
                    del s_map[s[i-len(p)]]
            

            if s_map == p_map:
                ans.append(i-len(p)+1)

        return ans

#wrong solution: anagrams need to be as long as the origin string.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_map = {}
        p_map = {}
        satisfied_char = 0
        left = 0
        ans = []

        for i in range(len(p)):
            if p[i] not in p_map:
                p_map[p[i]] = 1
                continue
            p_map[p[i]] += 1

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1

            if s[i] in p_map and s_map[s[i]] == p_map[s[i]]:
                satisfied_char += 1

            while satisfied_char == len(p_map):
                if s[left] in p_map:
                    if p_map[s[left]] == s_map[s[left]]:
                        satisfied_char -= 1
                        ans.append(left)
                    s_map[s[left]] -= 1
                left += 1


        return ans
"""