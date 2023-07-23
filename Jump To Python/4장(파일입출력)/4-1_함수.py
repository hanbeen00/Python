def sum(a,b):
    return a+b
a=3
b=4
c=sum(a,b)
print(c)

def say():
    return "Hi"
a=say()
print(a)

def sum(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))
c=sum(3,4)
print(c)

def say():
    print("hi")
print(say())


def sum_many(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
result=sum_many(1,2,3)
print(result)

def sum_mul(choice, *args):
    if choice=="sum":
        result =0
        for i in args:
            result = result +i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
    return result
result=sum_mul('sum',1,2,3,4,5)
print(result)


def sum_and_mul(a,b):
    return a+b,a*b
result=(sum_and_mul(3,4))
print(result)
sum,mul=sum_and_mul(3,4)
print(sum,mul)

def say_myself(name,old,man=True):
    print("%s"%name)
    print("%d"%old)
    if man:
        print("남자")
    else:
        print("여자")
    return ""
print(say_myself("abcd",27))
print(say_myself("abcd",27,False))


#def say_myself(name,man=True,old):
#    print("%s"%name)
#    print("%d"%old)
#    if man:
#        print("남자")
#    else:
#        print("여자")
#    return ""
#print(say_myself("abcd",27))



a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)

