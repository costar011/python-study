print("----Ex----")

first_var = "Hello world"
print(first_var)

first_var = "What's Up?"
print(first_var)


print("----정수형 타입----")
# Intger Type (정수형 타입)
x = 6
y = 9
print(x*y)
print(x+y)

print("----문자열 타입----")
# String Type (문자열 타입)
x = "6"
y = "9"
print(x+y)

print("----Array----")
var1 = "오민형"
var2 = "오은하"
var3 = "박여원"
var4 = "정은진"
var5 = "정예림"

# 배열
students = ["오민형", "오은하", "박여원", "정은진", "정예림"]
print(students)

print(students[0])


print("----함수----")


def send_KaKao_msg():
    for stu in students:
        print(stu + "에게 메세지를 전송했습니다.")


send_KaKao_msg()

# 표기법
# snake Case
# He lived in Gong-ju
# he_lieved_in_gongju
# sned_kakao_msg

students2 = ["지소영", "김지언", "홍도기", "이지섭", "지민승", "최주환", "박여원", "김우진", "정은진",
             "오은하", "정근모", "지민수", "오동건", "이유겸", "정우민", "오민형", "정예림", "박준희", "신예림"]


def send_KaKao_msg2():
    for stu2 in students2:
        print(stu2 + "에게 메세지를 전송했습니다.")


send_KaKao_msg2()
