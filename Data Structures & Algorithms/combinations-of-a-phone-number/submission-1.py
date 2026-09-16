class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = [""]
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        for d in digits:
            temp_list = []
            
            for curr_str in result:
                for c in digits_map[d]:
                    temp_list.append(curr_str + c)
                result = temp_list
    
        return result