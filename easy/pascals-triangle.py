class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        arr = []

        for row in range(0,numRows):
            
            temp = []

            for col in range(row+1):

                if col ==0 or col == row:
                    temp.append(1)
                else:
                    val = arr[-1][col-1] + arr[-1][col]
                    temp.append(val)

            arr.append(temp)   
            
        return arr
