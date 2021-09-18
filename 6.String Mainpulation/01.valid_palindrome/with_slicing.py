import re


class Solution:

    def isPanlindrom(self, s: str) -> bool:

        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


sol = Solution()
print(sol.isPanlindrom("A man, a plan, a canal: Panama"))