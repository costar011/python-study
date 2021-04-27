# 060
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시: [100, 130, 140, 150, 160, 170]
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 061
# 슬라이싱을 사용해서 홀수만 출력
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예: [1, 3, 5, 7, 9]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 062
# 슬라이싱을 사용해서 짝수만 출력
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예: [2, 4, 6, 8, 10]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 063
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력
# nums = [1, 2, 3, 4, 5]
# 실행 예: [5, 4, 3, 2, 1]
nums = [1, 2, 3, 4, 5]
print(nums[::-1])


# 064
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력
# 출력 예시: 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 065
# join 메소드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', '카카오', 'Apple']
# interest 리스트를 사용하여 아래와 같이 화면에 출력
# 출력 예시: 삼성전자 LG전자 Naver 카카오 Apple
interest = ['삼성전자', 'LG전자', 'Naver', '카카오', 'Apple']
print(" ".join(interest))


# 066
# join 메소드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', '카카오', 'Apple']
# interest 리스트를 사용하여 아래와 같이 화면에 출력
# 출력 예시: 삼성전자/LG전자/Naver/카카오/Apple
# 문자열의 join 메서드를 사용하면 리스트를 문자열로 붙일 수 있다.
interest = ['삼성전자', 'LG전자', 'Naver', '카카오', 'Apple']
print("/".join(interest))

# 067
# join 메소드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', '카카오', 'Apple']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# 카카오
# Apple
interest = ['삼성전자', 'LG전자', 'Naver', '카카오', 'Apple']
print("\n".join(interest))

# 068
# 문자열 split 메소드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장
# string = "Apple/카카오/Naver"
# 이를 interest 이름의 리스트로 분리 저장
# 실행 예시 >> print(interest)
# ['Apple', '카카오', 'Naver']
string = "Apple/카카오/Naver"
interest = string.split("/")
print(interest)
