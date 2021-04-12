# 050 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 리스트에 저장  (순위 정보는 저장하지 않는다.)
# 순위                      영화
# 1                        닥터 스트레인지
# 2                        스플릿
# 3                        럭키
# 영화 제목은 문자열로 표현 가능 여러 개의 값을 저장하기 위해 파이썬 리스트 자료형을 사용
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 051 리스트에 원소 추가
# 050의 movie_rank 리스트에 "배트맨"을 추가.
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

# 052
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# 리스트의 insert(인덱스, 원소) 메소드를 사용하면 특정 위치에 값을 끼어넣기 할 수 있다.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 053
# movie_rank 리스트에서 '럭키'를 삭제
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 054
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del을 이용하여 리스트에서 원소를 삭제할 수 있습니다. 리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱 된다.
# 따라서 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 한다.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 055
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만ㄷ는ㄴ다.
# >> lang1 = ["C", "C++", "JAVA"]
# >> lang2 = ["Python", "Go", "C#"]
# 실행 예: langs ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
# 두 리스트를 더하면 새로운 리스트가 생성.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 056
# 다음 리스트에서 최댓값과 최솟값을 출력. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예
# max:  7
# min:  1
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))
