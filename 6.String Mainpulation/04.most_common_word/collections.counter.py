import collections, re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 쉼표나 느낌표 등등 문자가 아닌것을 필터링
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        # 모아진 문자를 객체 형태로 정리 {a:1, b:3...}
        counts = collections.Counter(words)

        # 가장 많이 등장한 단어의 첫번째 인덱스 리턴 [(a, 1),,,]
        return counts.most_common(1)[0][0]

    # most_common(n) n의 입력값에 따라 몇개를 리턴할지 정해준다
    # 튜플 형태로 리턴

    ## collections.Counter(words) 는 {} 객체의 형태로 리턴하고
    ## most_common(1) 는 (a, 1) 튜플의 형태로 리턴

    ### collections.Counter(words).most_common(1)[0][0] 과 같이 이어서 사용할수 있다

    #### from collections import Counter 를 페이지 최상단에 사용할 경우
    #### Counter(words).most_common(1)[0][0] 과 같이 불러와서 사용할수 있다


sss = Solution()
print(sss.mostCommonWord("hello, world",[]))