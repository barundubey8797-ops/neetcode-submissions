class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean = ""
        # for ch in s:
        #     if ch.isalnum():
        #         clean += ch.lower()
        # return clean == clean[::-1]
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]





        