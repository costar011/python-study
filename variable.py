# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.
# print는 정수, 실수, 문자열 등을 화면에 출력합니다. 문자열은 큰따옴표 또는 작은따옴표로 표현 가능
print("Hello World")

# 002
# 화면에 Mary's cosmetics을 출력
# 문자열은 큰따옴표나 작은따옴표로 표현 가능 표현하고 싶은 문자열에 작은따옴표가 있으므로 문자열을 큰따옴표로 만들어주면된다.
print("Mary's cosmetics")

# 003
# 화면에 아래 문장을 출력
# 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야"')

# 004
# 화면에 "C:\Windows"를 출력
# print("C:\Windows")

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \t는 탭을 의미하고 \n'은 줄바꿈을 의미

# 006 print 여러 데이터 출력
print("오늘은", "일요일")
# 여러 값을 출력하려면 print 함수에서 쉼표로 구분해주면된다. 오늘은 다음에 공백이 하나 있고 일요일이 출력

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력
# naver;kakao;sk;samsung
# print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력
print("naver", "kakao", "samsung", sep=";")
