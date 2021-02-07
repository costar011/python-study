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
print("C:\Windows")

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

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력
# naver/kakao/sk/samsung
print("naver", "kakao", "samsung", sep="/")

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력 (힌트: end='') print 함수는 두 번 사용 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용
# print("first");print("second")
print("first", end="")
print("second")

# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력
# 출력하고 싶은 값을 print 함수로 적으면 됨
print(5/3)

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보기 , 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보이다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보기
# 항목	    값
# 시가총액	 298조
# 현재가	50,000원
# PER	  15.79
시가총액 = 298000000000000
현재가 = 5000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있다.
# s = "hello"
# t = "python"
# 두 변수를 이용하여 아래와 같이 출력
# 실행 예: hello! python
s = "hello"
t = "python"
print(s+"!", t)

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보기
2 + 2 * 3
8

# 015 type 함수
# type() 함수는 데이터 타입을 판별 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임
a = 128
print(type(a))
# < class 'int' >

# 아래 변수에 바인딩된 값의 타입을 판별
a = "132"
print(type(a))

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환
# num_str = "720"
num_str = "720"  # 형변환
num_int = int(num_str)
print(num_int+1, type(num_int))

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환
# num = 100
num = 100

result = str(num)
print(result, type(result))

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환
data = "15.79"
data(float(data))
print(data, type(data))

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있다. 정수로 변환한 후 최근 3년의 연도를 화면에 출력
# year = "2021"
year = "2021"
print(int(year)-3)  # 2018
print(int(year)-2)  # 2019
print(int(year)-1)  # 2020
