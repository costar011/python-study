# 071 tuple
# my_variable 이름의 비어있는 튜플을 만들어라.
# 괄호는 튜플을 정의하는 기호
my_variable = ()
# type() 함수는 변수에 바인딩된 데이터의 타입을 반환
print(type(my_variable))

# 072
# 영화 제목을 movie_rank 이름의 튜플에 저장 (순위 정보는 저장하지 않는다.)
# 순위	 영화
#  1	닥터 스트레인지
#  2	스플릿
#  3	럭키
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 073
# 숫자 1 이 저장된 튜플을 생성
# 아래와 같이 괄호와 함께 하나의 정숫값을 저장하면 튜플이 정의 될 것같지만 그렇지 않다.
# type()을 출력해보면 파이썬은 튜플이 아닌 정수로 인식
my_tuple = (1)
type(my_tuple)
int
# 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력
my_tuple = (1, )
