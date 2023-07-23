dic={'name':'pey', 'phone':'123456789', 'birth':'1118'} #딕셔너리는 키와 값으로 구성
print(dic)
a={1:'hi'}
b={'a':[1,2,3]} #값에는 리스트가 가능하나 키에는 리스트 불가
print(a)
print(b)

a={1:'a'}
a[2]='b' #대괄호 안에있는 것은 인덱스가 아닌 키값이고 등호 옆은 값임
print(a)
a['name']='pey' #name 은 키, pey는 값
print(a)
a[3]=[1,2,3] #숫자 3은 키, 리스트는 값
print(a)

del a[1] #해당 키 값을 통해 del함수 실행하면 키, 값 쌍으로 없어짐
print(a)

grade={'pey':10, 'julliet':99}  #딕셔너리는 인덱싱 불가
print(grade['pey']) #대괄호 안은 키값임
print(grade['julliet'])

a={1:'a',1:'b'} #키 값이 중복될 경우 하나를 제외한 나머지 모두 무시됨
print(a)

a={(1,2):'hi'} #튜플(불변값)은 딕셔너리의 키로 사용 가능하나
print(a[(1,2)])  #리스트(변하는값)는 딕셔너리의 키로 사용 불가

a={'name':'pey','phone':'0123456789','birth':'1118'}
print(a.keys()) # a.keys()는 해당 딕셔너리의 키값 모두 반환

for k in a.keys():
    print(k)

print(list(a.keys())) #키값들을 리스트로 반환

print(a.values()) #a.values() 값들 반환

print(list(a.items())) #a.items() 키,값 동시에 반환

print(a.get('name')) #a.get() 키값으로 값 얻기
print(a.get('ddddd', 'none')) #키값 뒤에 입력된것은 디폴트값(존재하지 않을경우 출력)

print('name' in a) #딕셔너리 내에 해당 키 값이 있는지 조사
print('email' in a)

print(a.clear()) #딕셔너리 모든 요소 삭제




      

