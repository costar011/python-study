# print 탭과 줄바꿈

# \t와 \n의 역할
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \t는 탭을 의미하고 \n 은 줄바꿈을 의미

# print 여러 데이터 출력
print("오늘은", "일요일")
# 여러 값을 출력하려면 print 함수에서 쉼표로 구분해주면 된다. 따라서 오늘은 다음에 공백이 하나 있고 일요일이 출력된다.

# print 기초

# naver;kakao;sk;samsung
# print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력
print("naver", "kakao", "samsung", sep=";")

# naver/kakao/sk/samsung
print("naver", "kakao", "samsung", sep="/")
