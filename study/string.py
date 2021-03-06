# 020 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매 , 총 금액은 계산한 후 이를 화면에 출력 (변수사용하기)
월 = 48584
총금액 = 월 * 36
print(총금액)

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력
# letters = 'python'
# 실행 예
# p t
# 문자열에서 한 글자를 가져오는 것을 인덱싱
lang = 'python'
print(lang[0], lang[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력
# license_plate = "24가 2210"
# 실행 예: 2210
# 문자열에서 여러 글자를 가져오는 것을 슬라이싱 이라고 부른다. 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미
# 슬라이싱에서 시작 인덱스를 생락혀면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미
license_plate = "24가 2210"
print(license_plate[-4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력
# string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있다.
string = "홀짝홀짝홀짝"
print(string[::2])

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력
# string = "PYTHON"
# 실행 예: NOHTYP
string = "PYTHON"
print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력
# phone_number = "010-1111-2222"
# 실행 예 010 1111 2222
# 파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있다 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴 된다
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력
# 실행 예 01011112222
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')
print(phone_number1)

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력
# https://www.naver.com
# 문자열로 표현된 url에서 .을 기준으로 분리. 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있다
url = "https://naver.com"
url_split = url.split('.')
print(url_split[-1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 문자열은 수정할 수 없다. 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있다.
# TypeError                                 Traceback (most recent call last)
# <ipython-input-22-a0f3d05b669c> in <module>
#      1 lang = "python"
# ----> 2 lang[0]= "P"
#      3 print(lang)
# TypeError: 'str' object does not support item assignment

# 029 replace 메소드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경
# string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 030 replace 메소드
# 아래 코드의 실행 결과를 예상
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# abcd가 그대로 출력. 문자열은 변경할 수 없는 자료형이기 때문이다. replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해준다.
