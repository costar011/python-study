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

print('신씨가 소리질렀다. "도둑이야"')
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

# 13
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
str1 = "15.79"
str1 = float(str1)
print(str1, type(str1))

# 14
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
# year = "2020"
year = "2020"

print(int(year)-1)  # 2019
print(int(year)-2)  # 2018
print(int(year)-3)  # 2017

# 15
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

month = 48584
count = month * 36
print(count)

# 16
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
# 실행 예 : p t

# 파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부릅니다. 파이썬 인덱싱은 0부터 시작합니다.
lang = 'python'
print(lang[0], lang[2])

# 17
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# license_plate = "24가 2210"
# 실행 예: 2210
# 문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 부릅니다. 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다.
# 슬라이싱에서 시작 인덱스를 생락혀면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미합니다.
license_plate = "24가 2210"
print(license_plate[-4:])

# 18
# 아래의 문자열에서 '홀' 만 출력하세요.
# string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.
string = "홀짝홀짝홀짝"
print(string[::2])

# 문자열을 작성하게되면, 각 문자마다 고유의 번호가 매겨지는데 이 번호를 오프셋이라 하고,
# ​ 오프셋을 이용하여 문자열에서 문자를 추출하는 것을 인덱싱이라 한다.

data = "0123456789"

data1 = data[::2]
print(data1[::-1])  # 거꾸로 출력 86420

# 19
# 문자열을 거꾸로 뒤집어 출력하세요.
# string = "PYTHON"
string = "PYTHON"
print(string[::-1])

# 20
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# phone_number = "010-1111-2222"
# 파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다.
# 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 21
# 20번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예 : 01011112222
num = "010-1111-2222"
result = num.replace("-", " ")
print(result)

# 22
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# url = "http://sharebook.kr"
# 실행 예: kr
# 문자열로 표현된 url에서 .을 기준으로 분리합니다.
# 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.
url = "http://sharebook.kr"
result = url.split(".")
print(result[-1])

# 23
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 24
# 화면에 '-'를 80개 출력하세요.
# 실행 예: --------------------------------------------------------------------------------
print("-" * 80)

# 25
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# t1 = 'python'
# t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예: python java python java python java python java
t1 = "python"
t2 = "java"
result = t1 + ' ' + t2 + ' '
print(result * 4)

# 26
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

# print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미합니다.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 27
# 삼성전자의 상장주식수가 다음과 같습니다.
# 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"

# 정수형으로 타입을 변환하려면 int( ) 함수를 사용하면 됩니다.
# 이때 숫자 형태의 문자열에 컴마가 있는 경우 바로 변환된지 않습니다.
# 먼저 문자열의 replace 메서드로 컴마를 제거한 후 변환해야합니다.
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

# 28
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
# 문자열에서 슬라이싱을 사용하면 여러 글자를 접근할 수 있습니다.
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 29
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"
# upper 메서드를 호출하면 문자열을 대문자로 만들 수 있습니다.
# 다만 이 경우에도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환되는 겁니다.
# 반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로 출력하면 됩니다.
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
