money=1 # 1 은 true
if money:
    print("택시")
    print("타기")

else:
    print("걷기")
    
a=3
b=5
print(a==b) #같으면
print(a!=b) #다르면

print(1 in [1,2,3]) #숫자 1이 리스트 안에 있으면
print(1 not in [1,2,3])

print('a' in ('a','b','c')) #문자 a 가 튜플안에 있으면
print('j' not in 'python') #문자 j가 문자열안에 있으면

pocket=['paper','cellphone','money']
if 'money' in pocket: #pocket 리스트 안에 money 가 있으면
    print("택시")
else:
    print("걷기")
    
pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass #아무일도 일어나지 않음
else:
    print("걷기")

pocket=['paper','cellphone','money', 'card']
if 'money' in pocket:
    print("택시")
elif 'card' in pocket: # if / elif / else
    print("택시")
else:
    print("걷기")
