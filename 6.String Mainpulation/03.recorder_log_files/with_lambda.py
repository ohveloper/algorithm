from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # 1. 로그를 letters와 digits 으로 구분하여 나눈다
        letters, digits = [], [] 
        
        for log in logs:
            if (log.split()[1].isdigit()):
                digits.append(log)
            else:
                letters.append(log)
                
        # 2. 문자열인 로그만 정령하고 순서대로 놓고, 숫자인 로그는 그대로 뒤에 붙인다
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

s = Solution()
print(s.reorderLogFiles(["hel1 sdf", "gig3 124 4"]))