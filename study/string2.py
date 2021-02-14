# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상
# a = "3"
# b = "4"
# print(a + b)
# 두 문자열에 대해 덧셈 기호는 문자열의 연결을 의미  따라서 "34"라는 새로운 문자열이 생성 그 값이 print 함수에 의해 화면에 출력

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상
# print("Hi" * 3)
# 문자열에 대한 곱셈은 문자열의 반복을 의미 따라서 다음과 같이 문자열이 출력된다.
# HiHiHi

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력
# 실행 예: --------------------------------------------------------------------------------
print("-" * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있다
# t1 = 'python'
# t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력
# 실행 예: python java python java python java python java
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력
# name1 = "라이언"
# age1 = 10
# name2 = "어피치"
# age2 = 13
# 이름: 라이언 나이: 10
# 이름: 어피치 나이: 13
# print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미
name1 = "라이언"
age1 = 10
name2 = "어피치"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시풀기
# 문자열의 포맷 메서드는 타입과 상관없이 값이 출력될 위치에 { }를 적어주면 된다
name1 = "라이언"
age1 = 10
name2 = "어피치"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 037 문자열 출력2
# f-string은 문자열 앞에 f가 붙은 형태다. f-string을 사용하면 {변수}와 같은 형태로 문자열 사이에 타입과 상관없이 값을 출력할 수 있다.
name1 = "라이언"
age1 = 10
name2 = "어피치"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")


# 038 , 제거하기
# 삼성전자의 상장주식수를 이용하여 콤마 제거한 후 이를 정수 타입으로 변환
# 상장주식수 = "5,969,782,550"
# 정수형으로 타입을 변환하려면 int( ) 함수를 사용 숫자 형태의 문자열에 콤마가 있는 경우 바로 변환된지 않는다 먼저 문자열의 replace 메서드로 콤마를 제거한 후 변환
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2021/02'만 출력
# 분기 = "2021/02(E) (IFRS연결)"
# 문자열에서 슬라이싱을 사용하면 여러 글자를 접근할 수 있다
분기 = "2021/02(E) (IFRS연결)"
print(분기[:7])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거
# data = "   삼성전자    "
# 문자열에서 strip( ) 메서드를 사용하면 좌우의 공백을 제거할 수 있다 이때 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환
data = "   삼성전자    "
data1 = data.strip()
print(data1)
