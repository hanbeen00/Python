print("hello world")
print('python is fun')
print("""life is too short, you need python""")
print('''life is too short, you need python''') #문자열 만들기 3가지 방법

print("python's favorite food is perl")
print('python\'s favorite food is perl')
print('"python is very easy." he says.')
print("\"python is very easy.\" he says.") #따옴표 안에 따옴표 출력하기

print("life is too short\nyou need python") #줄바꾸기
print("life is too short\tyou need python") #탭 간격 넣기
print("life is too short\\you need python") # \문자 넣기
print("life is too short\'you need python") # '문자 넣기
print("life is too short\"you need python") # "문자 넣기

multiline = '''
life is too short
you need python
'''
print(multiline) #줄바꾸기

head="python"
tail=" is fun"
print(head+tail) #문자열 연결
print(head*3) #문자열 반복
print(head[2]) #문자열 인덱싱
print(head[-2])
print(head[0])
print(head[-0])
print(head[0:4]) #문자열 슬라이싱
print(head[4:])
print(head[:4])
print(head[:]) #전체 출력
print(head[1:-2])

#포매팅
print("I eat %d apples" %5) #숫자 대입
print("I eat %s apples" %"five") #문자열 대입
print("I eat %c apples" %'c') #문자 대입
print("I eat %10.1f apples" %3.2) #부동 소수 대입
print("I eat %d%% apples" %20) #숫자 대입 + %문자 사용
number=5
print("I eat %d apples" %number)
day="three"
print("I ate %d apples. so I was sick for %s days" %(number,day)) #숫자, 문자열 동시 대입
print("%10s"%"hi") #전체 길이 10 + 오른쪽 정렬
print("%-10sjane."%"hi") #전체 길이 10 + 왼쪽 정렬

a="hobby"
print(a.count('b')) #문자열에서 해당 문자 개수 세기
a="Python is best choice"
print(a.find('b')) #해당 문자 몇번째 있는지 출력
print(a.find('k')) #문자열에 해당 문자가 없을 경우 -1 출력
print(a.index('t')) #해당 문자 몇번째 있는지 출력 + 해당 문자 없을 경우 오류 출력
a=","
print(a.join("happy")) #각각 문자 사이에 문자열 삽입

a="happy"
print(a.upper()) 
print("hAppy".upper()) #문자 대문자로
print("HaPPY".lower()) #문자 소문자로

a=" hi "
print(a.rstrip()) #오른쪽 공백 없앰
print(a.lstrip()) #왼쪽 공백 없앰
print(a.strip()) #양쪽 공백 없앰

a="life is too short"
print(a.replace("life","your leg")) #문자열 바꾸기
print(a.split()) #공백 기준으로 문자열 나누기
print(a.split('i')) #문자'i' 기준으로 문자열 나누기

#고급 포매팅
number=10
day="three"
print("I ate {0} apples. so I was sick for {0} days.".format(number,day)) #인덱스 {0}은 number로 포매팅
print("I ate {0} apples. so I was sick for {1} days.".format(number,day)) #인덱스 {1}은 day로 포매팅
print("I ate {n} apples. so I was sick for {d} days.".format(n=10,d="three")) #직접 이름을 넣어 포매팅
print("{0:<10}".format("hi")) #왼쪽정렬 + 총 문자열 자릿수 10
print("{0:>10}".format("hi")) #오른쪽정렬 + 총 문자열 자릿수 10
print("{0:^10}".format("hi")) #가운데정렬 + 총 문자열 자릿수 10
print("{0:=^10}".format("hi")) #공백을 '='으로 채움 + 가운데정렬 + 총 문자열 자릿수 10
print("{0:10.4f}".format(3.42134234)) #총 자릿수 10 + 부동소수 소수점 4자리까지 출력
print("{{and}}".format()) #중괄호 출력하고 싶으면 연속으로 입력
