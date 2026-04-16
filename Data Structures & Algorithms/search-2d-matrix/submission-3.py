class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = int(len(matrix))
        cols = int(len(matrix[0]))

        if rows == 0:
            return False
        high = rows*cols - 1
        low = 0
        while low <= high:
            mid = int((low + high) / 2)
            if matrix[int(mid / cols)][mid % cols] == target:
                return True
            elif target > matrix[int(mid / cols)][mid % cols]:
                low = mid +1
            else:
                high = mid -1
        return False