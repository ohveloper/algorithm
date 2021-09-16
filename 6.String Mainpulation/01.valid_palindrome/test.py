def isPalindrome(s):

    strs = []
    for char in s:
      if char.isalnum():
        strs.append(char.lower())

    # 영문자와 숫자만을 대상으로 한다는 조건을 처리가히 귀한 전처리
    # 대소문자를 구분하지 않기 때문에 모두 소문자로 변환
    # strs 가 비어있지 않았을때
    # 맨앞의 요소와 맨뒤의 요소를 비교해서 틀리면 false 를 리턴
    while len(strs) > 1:
      if strs.pop(0) != strs.pop():
        return False

    return True


# sol = Sol()
s = "hello"
print(isPalindrome(s))
