a=[1,2,3]
print(a)
print(a[0])
print(a[-1])
print(a[0]+a[2])

a=[1,2,3,['a','b','c']] #이중리스트
print(a[0]) #리스트 맨 처음 자료
print(a[-1]) #리스트 맨 마지막 자료
print(a[3])
print(a[-1][0]) #리스트 맨 마지막 자료 중 첫번째 자료

a=[1,2,['a','b',['life','is']]] #삼중 리스트
print(a[2][2][0])

a=[1,2,3,4,5]
b=a[:2] #리스트 슬라이싱
c=a[2:]
print(a[0:2])
print(b)
print(c)
a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3) #리스트 반복
print(str(a[2])+"hi")  #str()  숫자를 문자로

a[2]=4
print(a)
a[1]=['a','b','c']
print(a)

a=[1,2,3] #리스트에서 연속된 범위의 값 수정
a[1:2]=['a','b','c']
print(a)

a[1:3]=[] #[] 이용하여 리스트 요소 삭제
print(a)

del a[1] #del 함수 이용하여 리스트 요소 삭제
print(a)

a=[1,2,3]
a.append(4) #append 함수 이용하여 리스트 요소 추가
a.append([5,6])
print(a)

a=[1,4,3,2]
a.sort() #리스트 정렬
print(a)

a=['a','c','b']
a.sort()
print(a)

a.reverse() #리스트 뒤집기
print(a)

print(a.index('c')) #리스트 위치값 출력
a.insert(0,'d') #리스트 요소값 삽입
print(a)

a=a*2
print(a)

a.remove('a') #리스트 요소 제거
print(a)

print(a.pop(2)) #리스트 요소 뽑은 후 삭제
print(a)

print(a.count('b')) #리스트 요소 개수 세기
a.extend([1,2]) #리스트 확장
print(a)

a=[2,3,1,4]
print( 1 in a) #리스트 안에 요소 있는지 
print( 5 not in a)



