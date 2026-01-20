class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1 or numRows> len(s):
            return s

        row_list=[""]*numRows
        current_row=0
        step=1

        for index, character in enumerate(s):
            row_list[current_row]+=character

            #reach top
            if current_row == 0:
                step=1
            
            #reach bottom
            elif current_row == numRows-1:
                step=-1

            current_row+=step

        return "".join(row_list)