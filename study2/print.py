# 01 화면에 Hello World 문자열을 출력하세요.

from typing import Type


print("Hello World")

# 02 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)

print("Mary's cosmetics")

# 문자열은 큰따옴표나 작은따옴표로 표현 가능합니다.
# 표현하고 싶은 문자열에 작은따옴표가 있으므로 문자열을 큰따옴표로 만들어주면 됩니다.

# 03
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 신씨가 소리질렀다. "도둑이야".

print('신씨가 소리질렀다. "도둑이야')
# 표현하고 싶은 문자열에 큰따옴표가 포함되어 있습니다. 따라서 작은따옴표로 문자열을 만들어주면 됩니다.

# 04
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;apple
# print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.
print("naver", "kakao", "apple", sep=";")

# 05
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/apple
print("naver", "kakao", "apple", sep="/")

# 06
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다.
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("first");print("second")
print("first", end='')
print("second")

# 07
# 5/3의 결과를 화면에 출력하세요.
# 출력하고 싶은 값을 print 함수의 인자로 적어주면 됩니다.
print(5/3)

# 08
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 09
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
#   항목	    값
#   시가총액	298조
#   현재가      50,000원
#   PER	      15.79

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 10
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
print(f"{s}! {t}")

# 11
# 문자열 '720'를 정수형으로 변환해보세요.
# num_str = "720"
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))

# 12
# 정수 100을 문자열 '100'으로 변환해보세요.
# num = 100
num = 100
num2 = str(num)
print(num2, type(num2))
