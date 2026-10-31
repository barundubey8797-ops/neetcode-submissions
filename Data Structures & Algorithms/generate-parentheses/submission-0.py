class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []
        def backtrace(open_count, close_count):
            if len(current) == 2 * n:
                result.append("".join(current))
                return 
            if open_count < n:
                current.append("(")
                backtrace(open_count + 1, close_count)
                current.pop()
            if close_count < open_count:
                current.append(")")
                backtrace(open_count, close_count + 1)
                current.pop()
        backtrace(0,0)
        return result