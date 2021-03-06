import collections
from typing import Deque


class Solution:

    def isPanlindrom(self, s:str) -> bool:

        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


sol = Solution()
print(sol.isPanlindrom("A man, a plan, a canal: Panama"))
