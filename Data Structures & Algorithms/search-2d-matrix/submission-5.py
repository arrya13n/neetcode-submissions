class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        startRow = 0
        endRow = m - 1

        while startRow <= endRow:

            midRow = startRow + (endRow - startRow) // 2

            if target >= matrix[midRow][0] and target <= matrix[midRow][n - 1]:
                return self.searchInRow(matrix, target, midRow)

            elif target > matrix[midRow][n - 1]:
                startRow = midRow + 1

            else:
                endRow = midRow - 1

        return False
    
    def searchInRow(self, matrix, target, row):
        n = len(matrix[0])

        st = 0
        end = n - 1

        while st <= end:
            mid = st + (end - st) // 2

            if target == matrix[row][mid]:
                return True

            elif target > matrix[row][mid]:
                st = mid + 1

            else:
                end = mid - 1

        return False
