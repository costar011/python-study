# 040 strip 메소드
# 문자열의 좌우의 공백이 있을 때 이를 제거
# data = "   삼성전자    "
# 문자열에서 strip( ) 메소드를 사용하면 좌우의 공백을 제거할 수 있다 이때 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환
data = "   삼성전자    "
data1 = data.strip()
print(data1)

# 041 upper 메소드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경
# ticker = "btc_krw"
# upper 메소드를 호출하면 문자열을 대문자로 만들 수 있다. 다만 이 경우에도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환
# 반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로 출력
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

# 042 lower 메소드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경
# ticker = "BTC_KRW"
# lower 메서드
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 043 capitalize 메소드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경
a = "hello"
a = a.capitalize()
