n = 5
print(id(n))
n='ABC'
print(id(n))

a, b, c = 1, 2, 3 # a,b,c에 1,2,3을 각각 대입하여 변숫값을 출력
print(a)
print(b)
print(c)

x = 6
y = 2
x, y = y + 2, x + 3 # x에 (y+2)를 대입하고, y에 (x + 3)을 대입

print(x)
print(y)

n = 12
print(id(n))
n += 1
print(id(n))

# 뮤터블 자료형: 리스트, 딕셔너리, 집합 등이 있으며 값을 변경할 수 있다.
# 이뮤터블 자료형 : 수, 문자열, 튜플 등이 있으며 값을 변경할 수 없다.