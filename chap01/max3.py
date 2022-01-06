# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))


# 8 ~ 10 행 = 순차구조
maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c
# 순차구조 : 조건식으로 평가한 결과에 따라 프로그램의 실행 흐림이 변경되는 구조


print(f'최댓값은 {maximum}입니다.')