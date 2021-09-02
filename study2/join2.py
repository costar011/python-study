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
