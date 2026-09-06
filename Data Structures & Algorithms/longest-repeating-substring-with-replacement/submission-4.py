class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        word_freq = [0] * 26
        l = 0
        window_length = 0
        max_freq = 0

        for r in range(len(s)):
            i = ord(s[r]) - ord('A')
            word_freq[i] += 1

            max_freq = max(max_freq,word_freq[i])

            curr_length = r -l + 1

            if curr_length - max_freq > k:
                word_freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            window_length = max(window_length, r-l+1)
        return window_length
