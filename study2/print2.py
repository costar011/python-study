# 1
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
a = "hello"
a = a.capitalize()

# 2
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# endswith 메소드 활용
# file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
file_name.endswith("xlsx")

# 3
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"
a = "hello world"
a.split()
# 문자열의 split() 메서드를 사용하면 문자열에서 공백을 기준으로 분리해줍니다.

# 4
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
# 문자열에서 split() 메서드는 문자열을 분리할 때 사용합니다.
# 이때 어떤 값을 넘겨주면 그 값을 기준으로 문자열을 분리해줍니다.
ticker = "btc_krw"
ticker.split("_")

# 5
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2021-07-20"
date = "2021-07-20"
date.split("-")
