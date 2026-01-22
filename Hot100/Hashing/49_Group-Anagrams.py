class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict={}

        for string in strs:
            key = "".join(sorted(string))

            if key not in string_dict:
                string_dict[key] = []
            
            #append anyway
            string_dict[key].append(string)

        return list(string_dict.values())
                