# print 탭과 줄바꿈

# \t와 \n의 역할
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \t는 탭을 의미하고 \n 은 줄바꿈을 의미

# print 여러 데이터 출력
print("오늘은", "일요일")
# 여러 값을 출력하려면 print 함수에서 쉼표로 구분해주면 된다. 따라서 오늘은 다음에 공백이 하나 있고 일요일이 출력된다.

# print 기초

# naver;kakao;sk;samsung
# print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력
print("naver", "kakao", "samsung", sep=";")

# naver/kakao/sk/samsung
print("naver", "kakao", "samsung", sep="/")

# print 줄바꿈

# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용한다.
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용한다.
print("first")
print("second")

# 정답
print("first", end="")
print("second")

# 연산 결과 출력
# 5/3의 결과를 화면에 출력
# 출력하고 싶은 값을 print 함수의 인자로 적어주면된다.
print(5/3)

# 변수 사용하기
# 삼성전자 라는 변수로 50,000원을, 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
