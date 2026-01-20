#time complexity: O(n²)
def two_sum(self, nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for index, num in enumerate(nums):
        for i in range (index+1, len(num)):
            num_dict[index+i] = [index, i]

    if target in num_dict:
        return numdict[target]

#time complexity: O(n) in the worst situation 
#We dont really have to "fill" a hashmap(Look ahead). Just Look-back. 
#The question mentioned that there would be EXACTLY one solution. So when we looked back and found the another half (target - num) in the hashmap, it must be the answer.
def better_two_sum(self, nums: List[int], target: int) -> List[int]:
    previous_dict = {}

    for index, num in enumerate(nums):
        diff = target-num

        if diff in previous_dict:
            return [previous_dict[diff],index]
        
        previous_dict[num]=index