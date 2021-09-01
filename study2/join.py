# 1
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시: 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 2
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시: 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
# 문자열의 join 메서드를 사용하면 리스트를 문자열로 붙일 수 있습니다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 3
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

# 출력 예시
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 4
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장
# 실행 예시
# print(interest)
# ['삼성전자', 'LG전자', 'Naver']
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 5
# 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)

# 6
# my_variable 이름의 비어있는 튜플을 만들어라.
# 괄호는 튜플을 정의하는 기호
my_variable = ()
# 정말 튜플이 생성됐는지 확인해 봅시다. type() 함수는 변수에 바인딩된 데이터의 타입을 반환
print(type(my_variable))
# 실행을 시키면 <class 'tuple'> 이 나온다.

# 7
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위      영화

#   1      닥터 스트레인지
#   2	   스플릿
#   3	   럭키
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 8
# 숫자 1 이 저장된 튜플을 생성
# 아래와 같이 괄호와 함께 하나의 정숫값을 저장하면 튜플이 정의 될 것같지만 그렇지 않다.
# type()을 출력해보면 파이썬은 튜플이 아닌 정수로 인식
my_tuple = (1)
type(my_tuple)
# 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해만 한다.
my_tuple = (1, )
