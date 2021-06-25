# 2단 ~ 9단 까지 출력하세요.
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}")

# for 문
# for 변수 in 리스트(또는 튜플, 문자열):
#    수행할 문장1
#    수행할 문장2 . . .


# 전형적인 for문
test_list = ["one", "two", "three"]

for i in test_list:
    print(i)

# ['one', 'two', 'three'] 리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 print(i) 문장을 수행.
# 다음 두 번째 요소 'two'가 i 변수에 대입된 후 print(i) 문장을 수행하고 리스트의 마지막 요소까지 반복.


# 다양한 for문 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)

# 위 예는 a 리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입.
# 이 예는 사용한 변수값 대입 방법과 매우 비슷한 경우임.
# >>> (first, last) = (1, 2)
