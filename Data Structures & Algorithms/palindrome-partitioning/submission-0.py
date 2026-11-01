class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def isPalindrome(word):
            return word == word[::-1]
        def backtrace(start):
            if start == len(s):
                result.append(path.copy())
                return 
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrace(end + 1)
                    path.pop()
        backtrace(0)
        return result
        