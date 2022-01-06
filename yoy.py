def Yoy(T:int):
    for _ in range(T):
        N = int(input())
        dic = {}
        for _ in range(N):
            uni, drink = input().split()
            dic[uni] = int(drink)
        print(sorted(dic.items(), key = lambda x:x[1], reverse=True)[0][0])
        
if __name__ == '__main__':
    T = int(input())
    Yoy(T)