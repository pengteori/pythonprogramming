def read_single_digit():
    global a,b,c
    if a==1:a='일'
    elif a==2:a='이'
    elif a==3:a='삼'
    elif a==4:a='사'
    elif a==5:a='오'
    elif a==6:a='육'
    elif a==7:a='칠'
    elif a==8:a='팔'
    else: a='구'
    if b==1:b='일'
    elif b==2:b='이'
    elif b==3:b='삼'
    elif b==4:b='사'
    elif b==5:b='오'
    elif b==6:b='육'
    elif b==7:b='칠'
    elif b==8:b='팔'
    elif b==9:b='구'
    else: b='영'
    if c==1:c='일'
    elif c==2:c='이'
    elif c==3:c='삼'
    elif c==4:c='사'
    elif c==5:c='오'
    elif c==6:c='육'
    elif c==7:c='칠'
    elif c==8:c='팔'
    elif c==9:c='구'
    else: c='영'
def read_number():
    print(a,b,c)
num=int(input('세 자리 정수 입력: '))
a=num//100
b=(num-100*a)//10
c=num-100*a-10*b
read_single_digit()
read_number()
