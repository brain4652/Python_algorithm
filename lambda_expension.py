# 기본형 
# (lambda <인자>: <함수>)(<입력값>)

# print((lambda x: x+1)(int(input())))

# 함수형
# func = lambda <인자>: <인자를 활용한 함수>
# func(입력값)

# func1 = lambda x: x**x
# print(func1(int(input())))

# dictionary와 연계

dict1 = {
    'a':1,
    'b':100,
    'c':1000}

dict2 = sorted(dict1.items(), key = lambda x:x[1], reverse=True)
print(dict2)

dict3 = sorted(dict1, key = lambda x:x[0], reverse=True)
print(dict3)

