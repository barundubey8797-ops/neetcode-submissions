class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_freq = 0
        count = {}
        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
            max_freq = max(max_freq, count[ch])
            length = right - left + 1
            if length - max_freq > k:
                count[s[left]] -= 1
                left += 1
            length = right - left + 1
            max_length = max(max_length, length)
        return max_length