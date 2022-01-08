# lst1과 lst2는 다르다.

lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5] #같은 리스트를 생성한 것 처럼 보이지만 이는 literal 값이 아니다.
print(lst1 is lst2)



lst1 = [1,2,3,4,5]
lst2 = lst1         #lst2 는 lst1을 참조
print(lst1 is lst2)



lst1[2] = 9         # lst1의 원소값을 바꾸면 lst2도 바뀐다. (10번째 줄의 식때문에)
print(lst1)
print(lst2)
