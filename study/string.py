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