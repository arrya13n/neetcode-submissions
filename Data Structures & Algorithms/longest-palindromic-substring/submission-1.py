class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        max_length = 0

        for i in range(len(s)):
            #odd case we start from middle char and explore the outer char
            #initialize l,r at i
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                #check if current length is > then max length then update max length
                # add the substring to result
                #and decrement l and increment r

                if (r-l+1) > max_length:
                    result = s[l:r+1]
                    max_length = r - l + 1
                l -= 1
                r += 1

            #for even case we start l with i and r with I+1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_length:
                    result = s[l:r+1]
                    max_length = r-l+1
                l -= 1
                r += 1
        return result

