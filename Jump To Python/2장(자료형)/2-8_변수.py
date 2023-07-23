a,b = ('python', 'life') #튜플 변수 대입
print(a,b)
(a,b)='python', 'life' #튜플 변수 대입
print(a,b)

[a,b]=['python','life'] #리스트 변수 대입
print(a,b)
a,b=['python','life'] #리스트 변수 대입
print(a,b)

a=b='python' #여러개 변수 같은 값 대입
print(a,b)

a=3
b=5
a,b=b,a #대입값 바꾸기
print(a,b)
del(a) #메모리에 생성된 변수 없애기
del(b)

a=[1,2,3]
b=a #a 와 b 는 이름만 다른 완전히 동일한 리스트(하나 값 변하면 다른것도 같이 변함)
a[1]=4
print(a,b)
print(a is b)

a=[1,2,3]
b=a[:] #a 와 b는 값만 같은 다른 리스트
a[1]=4
print(a,b)
print(a is b)

a=[1,2,3]
from copy import copy
b=copy(a)  #a 와 b는 값만 같은 다른 리스트
print(a is b)



