x = ['John', 'George', 'Paul', 'Ringo']

x.reverse()   #리스트 x의 원소를 역순으로 정렬
# 튜플은 이뮤터블하므로 자기 자신을 역순으로 정렬할 수 없습니다.

y = list(reversed(x))   #리스트 x의 원소를 역순으로 정렬하여 y에 대입
print(x,y)