# 리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val):
    """lst[idx]의 값을 val로 없데이트"""
    lst[idx] = val
    
x = [11,22,33,44,55]
print('x = ', x)

index = int(input('업데이트할 인덱스를 선택하세요.: '))
value = int(input('새로운 값을 입력하세요.: '))

change(x, index, value)
print(f'x = {x}')

# 인수가 뮤터블일 때: 함수 안에서 매개변수의 값을 변경하면 객체 자체를 업데이트합니다. 
# 따라서 매개변수의 값을 변경하면 호출하는 쪽의 실제 인수는 값이 변경됩니다.