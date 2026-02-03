class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_map = {}
        #store the last-seen of every charater
        for i in range (len(s)):
            char_map[s[i]] = i

        #then we traverse it again: everytime when we add a new character to the current string, we check the map to get the farest "last-seen" of the string. 
        # The new char will keep pushing the bound away. If we reach the bound, it means that it's the cut position.
        #it's like make a agreement between all the existing characters.
        cut_point = 0
        # 0 it self works as an index, so we need to add it for the first cut length.
        last_cut_point = -1
        ans = []
        for i in range(len(s)):
            cut_point = max(cut_point, char_map[s[i]])
            if i == cut_point:
                ans.append(i-last_cut_point)
                last_cut_point = i

        return ans