s1=set([1,2,3]) #집합 리스트
print(s1)
s2=set("hello") #집합 문자열
print(s2)
 
l1=list(s1) #집합을 리스트로
print(l1)
print(l1[0])

t1=tuple(s1) #집합을 튜플로
print(t1)
print(t1[0])

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2) #교집합
print(s1.intersection(s2)) #교집합

print(s1|s2) #합집합
print(s1.union(s2)) #합집합

print(s1-s2) #차집합
print(s1.difference(s2)) #차집합
print(s2-s1)
print(s2.difference(s1))

s1=set("abc") 
s1.add("h") #값 1개 추가하기
print(s1)

s1=set([1,2,3])
s1.add(4) #값 1개 추가하기
print(s1)

s1=set([1,2,3])
s1.update([4,5,6]) #값 여러개 추가하기
print(s1)

s1=set([1,2,3])
s1.remove(2) #특정 값 제거하기
print(s1)
