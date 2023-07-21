#abs - 절댓값 반환
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#all - x가 모두 참이면 true, 거짓이 하나라도 있으면 false
print(all([1,2,3]))
print(all([1,2,3,0]))

#any - x중 하나라도 참이 있으면 true, 모두 거짓이면 false
print(any([1,2,3,0]))
print(any([0,""]))

#chr - 아스키 코드값 입력받아 해당 문자 출력
print(chr(97))
print(chr(48))

#dir - 객체가 자체적으로 가지고 있는 변수나 함수 보여줌.
print(dir([1,2,3]))
print(dir({'1':'a'}))

#divmod - 2개 숫자 입력받아 몫과 나머지를 튜플형태로 리턴
print(divmod(7,3))
print(divmod(1.3,0.2))

#enumerate - 순서가 있는 자료형(리스트,튜플,문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

#eval - 실행가능한 문자열을 입력받아 실행 결과값을 리턴
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))

#filter - 두번째 인수를 첫번째 인수에 입력되었을 때 리턴값이 참인 것 리턴
def positive(x):
    return x>0
print(list(filter(positive,[1,-3,2,0,-5,6])))
print(list(filter(lambda x:x>0,[1,-3,2,0,-5,6])))

#hex - 정수값 입력받아 16진수 변환후 리턴
print(hex(234))
print(hex(3))

#id - 객체를 입력받아 객체 고유 주소값 리턴
a=3 # 3,a,b 모두 같은 객체 가리킴
b=a
print(id(3))
print(id(a))
print(id(b))
print(id(4))

#input - 입력받는 함수
a=input()
print(a)
b=input("Enter: ")
print(b)
