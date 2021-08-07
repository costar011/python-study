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
# 문자열의 split() 메서드를 사용하면 문자열에서 공백을 기준으로 분리해준다.

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

# 6
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.\
# data = "039490     "
# rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환된다.
# 그 값을 data라는 변수가 새로 바인딩합니다. 기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제된다.
data = "039490     "
data = data.rstrip()


# 7
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
# 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 영화 제목은 문자열로 표현 가능
# 여러 개의 값을 저장하기 위해 파이썬 리스트 자료형을 사용한다.
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 8
# movie_rank 리스트에 "아이언맨" 을 추가하라.
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("아이언맨")
print(movie_rank)
