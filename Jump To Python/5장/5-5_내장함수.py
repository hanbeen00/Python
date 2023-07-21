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

#int - 문자열 형태의 숫자나 소수점 있는 숫자를 정수 형태로 리턴
#int(x, radix) - radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴
print(int('3'))
print(int(3.4))
print(int('11',2))
print(int('1A',16))

#isinstance - 첫번째 인수 인스턴스, 두번째 인수 클래스 / 인스턴스가 클래스의 인스턴스인지 판단
class Person: pass
a=Person()
print(isinstance(a,Person))
b=3
print(isinstance(b,Person))

#lambda - 함수 생성시 사용하는 예약어
sum=lambda a,b:a+b
print(sum(3,4))
myList=[lambda a,b:a+b, lambda a,b:a*b]
print(myList[0](3,4))
print(myList[1](3,4))

#len - 입력값의 길이 리턴
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

#list - 반복가능한 자료형 입력받아 리스트로 만들어 리턴
print(list("python"))
print(list((1,2,3)))

#map - 함수와 반복가능한 자료형 입력받아 함수에 의해 수행된 결과 리턴
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)

def two_times(x): return x*2
print(list(map(two_times,[1,2,3,4])))

print(list(map(lambda a:a*2,[1,2,3,4,])))

def plus_one(x):
    return x+1
print(list(map(plus_one,[1,2,3,4,5])))

#max - 반복가능한 자료형 입력받아 최대값 리턴
print(max([1,2,3]))
print(max("python"))

#min - 반복가능한 자료형 입력받아 최소값 리턴
print(min([1,2,3]))
print(min("python"))

#oct - 정수 형태의 숫자를 8진수 문자열로 리턴
print(oct(34))
print(oct(12345))

#ord - 문자의 아스키 코드값 리턴
print(ord('a'))
print(ord('0'))

#pow - x의 y 제곱한 결과값 리턴
print(pow(2,4))
print(pow(3,3))

#range - 입력받은 숫자에 해당되는 범위값 반복가능한 객체로 리턴
print(list(range(5)))
print(list(range(5,10)))
print(list(range(0,-10,-1)))

#str - 문자열 형태로 객체 변환
print(str(3))
print(str('hi'.upper()))

#tuple - 반복가능한 자료형 입력받아 튜플 형태로 바꾸어 리턴
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#type - 입력값의 자료형이 무엇인지 알려줌
print(type('abc'))
print(type([]))
print(type(open("test",'w')))

#zip - 동일한 개수로 이루어진 자료형 묶어줌
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc","def")))

#open - 파일읽기, 읽기방법 입력하여 파일 객체 리턴
f=open("binary_file","rb") #바이너리 읽기모드
fread = open("read_mode.txt","r")
fread2=open("read_mode.txt")
fappend = open("append_mode.txt",a) #추가모드로 파일 열기


