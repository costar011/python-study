# (조건식) ? When True :  When False
# When True if 조건식 else When False

reult = "Hello WOrld" if False else "Bye"
print(reult)

data_list = [1, 2, 3, 4, 5, 6]
# 배열의 length - 1 => last index

for i in enumerate(data_list):
    if(i[0] % 2 != 0):
        print(i[1], "design")
    else:
        print(i[1])

    # range(startInt, LastInt)
    # startInt 부터 LastInt미만 까지 반복한다.

    for i in range(0, len(data_list)):
        print(data_list[i])


# 1 ~ 9 값
input_data = int(input("숫자 입력 : "))

print(f"입력한 데이터는 {input_data} 입니다")

for i in range(1, 10):
    print(f"{input_data} * {i} = {input_data * i }")
