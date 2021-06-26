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


# for문의 응용
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여 주시오."

# 우선 학생 5명의 시험 점수를 리스트로 표현해 본다.
# marks = [90, 25, 67, 45, 80]
# 1번 학생은 90점이고 5번 학생은 80점이다.
# 이런 점수를 차례로 검사해서 합격했는지 불합격했는지 통보해 주는 프로그램을 만들어 보자.
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# 각각의 학생에게 번호를 붙여 주기 위해 number 변수를 사용하였다. 점수 리스트 marks에서 차례로 점수를 꺼내어 mark라는 변수에 대입하고 for문 안의 문장들을 수행한다.
# 우선 for문이 한 번씩 수행될 때마다 number는 1씩 증가한다.
