# 정수          123, -345, 0
# 실수          123.45, -1234.5, 3.4e10
# 8진수         0o34, 0o25
# 16진수        0x2A, oxFF

# 정수형
# 정수형(lnteger) 이란 말 그대로 정수를 뜻하는 자료형을 말한다. 다음 예는 양의 정수와 음의 정수, 숫자0을 변수 a에 대입하는 예이다.

# a = 123
# a = -178
# a = 0

# 실수형
# 파이썬에서 실수형(Floating-point)은 소수점이 포함된 숫자를 말한다.다음은 실수를 변수 a에 대입하는 예이다.

# a = 1.2
# a = -3.45
# 위 방식은 우리가 일반적으로 볼 수 있는 실수형의 소수점 표현 방식이다.

# a = 4.24E10
# a = 4.24e-10
# 위 방식은 "컴퓨터식 지수 표현 방식"으로 파이썬에서는 4.24e10 또는 4.24E10처럼 표현한다.(e와 E 둘 중 어느 것을 사용해도 무방하다)
# 여기서 4.24E10은 4.24∗1010 , 4.24e-10은 4.24∗10−10을 의미한다.

# 8진수와 16진수
# 8진수(Octal)를 만들기 위해서는 숫자가 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)로 시작하면 된다.
# a = 0o177

# 16진수(Hexadecimal)를 만들기 위해서는 0x로 시작하면 된다.
# a = 0x8ff
# b = 0xABC
# 8 진수나 16진수는 파이썬에서 잘 사용하지 않는 형태의 숫자 자료형이나 간단히 눈으로 익힘

# 숫자형을 활용하기 위한 연산자

# 사칙연산
# 파이썬 역시 계산기와 마찬가지로 다음처럼 연산자를 사용해 사칙연산을 수행한다.

a = 3
b = 4
print(a + b)
print(a * b)
print(a / b)
