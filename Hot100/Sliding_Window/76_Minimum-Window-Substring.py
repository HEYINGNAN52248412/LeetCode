class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_character_in_s_map = {} #window map: records the frequency of the characters in the current window
        t_character_map = {}      #targrt map: records the fixed frequency of each character in the target string t
        min_len = float('inf')    #the length of the minimum valid window 
        ans = ()                  #answer tuple, recording the indexes of the ans

        left = 0                  
        full_fill_char_nums = 0   #counter: record the number of certain characters within the window that have appeared and reached the required frequency in t

        #pretreat, constructing a hashmap: [character : frequency]
        for i in range (len(t)):
            if t[i] in t_character_map:
                t_character_map[t[i]] += 1 
            else:
                t_character_map[t[i]] = 1

        #expanding stage: move the right pointer untill it final has enough full_fill_chars
        for right in range (len(s)):
            if s[right] in t_character_map:
                if s[right] in t_character_in_s_map:
                    t_character_in_s_map[s[right]] += 1
                else:
                    t_character_in_s_map[s[right]] = 1

                #if a type of character reached the frequency in t, then full_fill_char_nums += 1.
                #we wont do more addings when: {t_character_in_s_map[s[right]] > t_character_map[s[right]]}
                if t_character_in_s_map[s[right]] == t_character_map[s[right]]:
                    full_fill_char_nums += 1

            #when all characters in t_character_map are fullfilled
            while full_fill_char_nums == len(t_character_map):
                #store the current string. It must be valid.
                if right-left < min_len:
                    ans = (left, right)
                    min_len = right-left+1

                #try to remove the left element to create a shorter string.
                remove_left = s[left]

                #if remove_left is not in t_character_map, just remove it.
                #if it is in the map, t_character_in_s_map[remove_left] must minus 1 after every removement.
                if remove_left in t_character_map:
                    # if removing it will result in the inability to meet the requirement: we need to stop. minus the full_full_char_nums by one, and while loop will stop.
                    if t_character_map[remove_left] == t_character_in_s_map[remove_left]:
                        full_fill_char_nums -= 1
                    t_character_in_s_map[remove_left] -= 1
                
                #remove the left
                left += 1


        return s[ans[0] : ans[1]+1] if ans else ""