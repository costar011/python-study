# list(Array,Tuple)
# list -> 변수와 같은 개념
# 리스트는 [] 를 사용하고
# 튜플은 () 를 사용한다.

test_list = ["프로도", "어피치", "콘", "무지", "춘식이", "라이언"]

test_tuple = ("프로도", "어피치", "콘", "무지", "춘식이", "라이언")

print(len(test_list))

# length -1은 last of index값과 동일함.

# append()
# append는 리스트에 값을 추가하는 함수이다.
# 단, 마지막에 추가한다.

test_list.append("김경민")
print(test_list)

# test_list에서 2번 ~ 4번까지 출력해보세요.
print(test_list[2:5])  # 2번부터 4번까지 출력

# test_list에서 3번 ~ 끝까지 출력해보세요.

# 이 방식이 가독성이 좋음
print(test_list[3:len(test_list)])  # 3번부터 끝까지 출력
print(test_list[3:])  # 또다른 방법

# remove() 특정 값을 찾아서 삭제한다.
# 특정한 값! 을 기준으로 데이터를 삭제하는 함수
# 주의! : index번호로 삭제하는게 아님.
test_list.remove("무지")
print(test_list)

# pop()
# 특정한 데이터를 추출해서 리턴하는 함수
# 파라미터는 index번호를 넣어준다.
point_data = test_list.pop(1)
print(point_data)

test_list.append("라이언")
test_list.append("라이언")
test_list.append("라이언")
test_list.append("라이언")
test_list.append("라이언")

# filter()
# 말그대로 필터링
# 파라미터, 첫번째 파라미터에 조건람다식, 두번째 파라미터에 리스트가 들어간다.
# filter함수는 객체로 리턴하기 때문에 list type으로 casting이 필요하다.

filter_data = list(filter(lambda x: x != "라이언", test_list))
print(filter_data)

exam = "재료: 밀가루, 호박, 계란, 떡, 대파, 고춧가루"
# 다음 문자열 데이터의 실제 재료들만 배열로 만들어 생성해라
# 단, "호박"은 제외 한다.


# 띄어쓰기로 쪼개준다.
result = exam.split(": ")  # 띄어쓰기
result2 = result[len(result) - 1].split(",")

temp_arr = []

for txt in result2:
    temp_arr.append(txt.strip())

real_result = list(filter(lambda x: x != "호박", temp_arr))  # "호박" 없앰

print(real_result)
