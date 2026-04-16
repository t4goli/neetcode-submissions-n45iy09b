class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = int(len(matrix))
        cols = int(len(matrix[0]))

        if rows == 0:
            return -1
        index = int((rows * cols - 1) /2)
        high = rows*cols - 1
        low = 0
        if matrix[int(index / cols)][index % cols] == target:
            return True
        if matrix[int(high / cols)][high % cols] == target:
            return True
        if matrix[int(low / cols)][low % cols] == target:
            return True
        else:
            while low != index and high != index:
                if target > matrix[int(index / cols)][index % cols]:
                    low = index
                    index = int((high - low) /2) + low
                else:
                    high = index
                    index = int((high - low) /2) + low
                print(high)
                print(low)
                print(index)
                if matrix[int(index / cols)][index % cols] == target:
                    return True
        return False