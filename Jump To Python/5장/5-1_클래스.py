class Calculator:
    def __init__(self):
        self.result=0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


class Simple:
    pass

a= Simple()


class Service:
    secret = "안녕하세요"
    def __init__(self,name):
        self.name =name
    
    def setname(self,name):
        self.name=name
    
    def sum(self, a,b): #첫 인수 self 무조건 필요, self 사용해야 인스턴스의 함수로 사용 가
        result = a+b
        print("%s님 %s+%s = %s입니다." %(self.name, a, b, result))

pey = Service("홍길동")
print(pey.secret)
pey.setname("ㅇㅇㅇ")
pey.sum(1,1)

babo=Service("홍길동")
print(babo.secret)
babo.sum(1,1)



class FourCal:
    def setdata(self, first, second):
        self.first =first
        self.second =second
    def sum(self):
        result= self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
    
    
a=FourCal()     
print(type(a))
a.setdata(4,2)  #FourCal.setdata(a,4,2)
print(a.first)
print(a.second)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())

b= FourCal()
b.setdata(3,7)
print(b.first)
print(b.second)


class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def setname(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." %(self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))
    def __add__(self,other):
        print("%s, %s 결혼했네" %(self.fullname ,other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" %(self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" %(self.fullname, other.fullname))

class HouseKim(HousePark): #클래스 상속
    lastname="김"
    def travel(self, where, day):
        print("%s, %s여행을 %d일 가다." %(self.fullname, where,day))

pey = HousePark("응용") #pey 객체 생성
pey.setname("응응")
pey.travel("부산")
print(pey.lastname)
print(pey.fullname)

pes = HousePark("응용") 
print(pes.lastname)
print(pes.fullname)

juliet = HouseKim("줄리엣") #juliet 객체 생성
juliet.travel("독도",3)

pey.love(juliet) #love 메서드 호출
pey + juliet # +연산자 객체에 사용시 __add__함수 호출됨
pey.fight(juliet)
pey - juliet

