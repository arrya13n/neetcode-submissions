class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        t_count = Counter(t)

        l = r = matches = 0
        req_match = len(t_count)

        curr_window_count = defaultdict(int)

        result = (float('inf'), 0, 0)

        while r < len(s):
            curr_char = s[r]

            curr_window_count[curr_char] += 1

            if curr_char in t_count and t_count[curr_char] == curr_window_count[curr_char]:
                matches += 1
            
            while l<=r and matches == req_match:
                remove_char = s[l]

                if (r-l+1) < result[0]:
                    result = (r-l+1,l,r)
                
                curr_window_count[remove_char] -=1
            
                if remove_char in t_count and curr_window_count[remove_char] < t_count[remove_char]:
                    matches -= 1
                l += 1
            r += 1
        return s[result[1]:result[2]+ 1] if result[0] != float('inf') else ""
