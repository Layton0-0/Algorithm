# 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1: http://부분은 제외 -> naver.com
# 규칙 2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예: 생성된 비밀번호 : nav51!

# 윤정 작성 코드
domain = "http://daum.net"
pw = domain.replace("http://", "")
pw = pw[: pw.index(".")]  # 처음 .을 만나는 지점 전까지 자름
pw = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
print(f"{domain}의 비밀번호는 {pw}이다")
print("{domain}의 비밀번호는 {pw}이다".format(domain=domain, pw=pw))
