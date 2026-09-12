class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        word_freq = [0] * 26
        l = 0
        window_length = 0
        max_freq = 0

        for r in range(len(s)):
            #increment word frequenct
            i = ord(s[r]) - ord('A')
            word_freq[i] += 1

            #increase max frequency
            max_freq = max(max_freq,word_freq[i])

            #calculate current length of the string
            curr_length = r -l + 1

            #compare current_length - max_frequency with given k 
            if curr_length - max_freq > k:
                word_freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            #update window length
            window_length = max(window_length, r-l+1)
        return window_length
