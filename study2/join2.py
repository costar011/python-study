# 1
# 다음 튜플을 리스트로 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)

# 2
# 다음 리스트를 튜플로 변경
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)

# 3
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성
# (2, 4, 6, 8 ... 98)
data = tuple(range(2, 100, 2))
print(data)

# 별 표현식
# 4
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있다.
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없다.
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)
