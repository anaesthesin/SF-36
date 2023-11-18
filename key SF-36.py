##вопрос 1
while True:
    try:
        q1 = int(input('вопрос 1 '))
        while q1 < 1 or q1 > 5:
            print('ошибка, введите число от 1 до 5')
            q1 = int(input('вопрос 1 '))
        break
    except ValueError:
        print('введите целое число')

v1 = None
if q1 == 1:
    v1 = 5
if q1 == 2:
    v1 = 4.4
if q1 == 3:
    v1 = 3.4
if q1 == 4:
    v1 = 2
if q1 == 5:
    v1 = 1


##вопрос 2
while True:
    try:
        q2 = int(input('вопрос 2 '))
        while q2 < 1 or q2 > 5:
            print('ошибка, введите число от 1 до 5')
            q2 = int(input('вопрос 2 '))
        break
    except ValueError:
        print('введите целое число')

##вопрос 3
def vopros3(par):
    while True:
        try:
            q3a = int(input('введите ответ '))
            while q3a < 1 or q3a > 3:
                print('ошибка, введите число от 1 до 3')
                q3a = int(input('введите ответ '))
            break
        except ValueError:
            print('введите число от 1 до 3')
    return q3a
    
def PF():
    print('вопрос 3а')
    q3a = vopros3(PF3a)
    print('вопрос 3б')
    q3b = vopros3(PF3b)
    print('вопрос 3в')      
    q3c = vopros3(PF3c)
    print('вопрос 3г')      
    q3d = vopros3(PF3d)
    print('вопрос 3д')      
    q3e = vopros3(PF3e)
    print('вопрос 3е')     
    q3f = vopros3(PF3f)
    print('вопрос 3ж')      
    q3g = vopros3(PF3g)
    print('вопрос 3з')      
    q3h = vopros3(PF3h)
    print('вопрос 3и')      
    q3i = vopros3(PF3i)
    print('вопрос 3к')      
    q3j = vopros3(PF3j)
    PFsum = q3a + q3b + q3c + q3d + q3e + q3f + q3g + q3h + q3i + q3j
    PF = ((PFsum - 10)/20) * 100
##    print(PF)  #конечный результат 3 вопроса
    return PF
    
PF3a = None
PF3b = None
PF3c = None
PF3d = None
PF3e = None
PF3f = None
PF3g = None
PF3h = None
PF3i = None
PF3j = None
PF = PF()
##print('PF = ', PF)

##вопрос 4
def vopros4(par):
    while True:
        try:
            q4 = int(input('введите ответ '))
            while q4 != 1 and q4 != 2:
                print('ошибка, введите число 1 или 2')
                q4 = int(input('введите ответ '))
            break
        except ValueError:
            print('введите число 1 или 2')
    return q4

def RP():
    print('вопрос 4а')
    q4a = vopros4(RP4a)
##    print('q4a = ', q4a)
    print('вопрос 4б')
    q4b = vopros4(RP4b)
##    print('q4b = ', q4b)    
    print('вопрос 4в')
    q4c = vopros4(RP4c)
##    print('q4c = ', q4c)
    print('вопрос 4г')
    q4d = vopros4(RP4d)
##    print('q4d = ', q4d)
    RPsum = q4a + q4b + q4c + q4d
    RP = ((RPsum - 4)/4) * 100
##    print('RP = ', RP)
    return RP
    
RP4a = None 
RP4b = None  
RP4c = None  
RP4d = None
RP = RP()


#вопрос 5
def vopros5(par):
    while True:
        try:
            q = int(input('введите ответ '))
            while q != 1 and q != 2:
                print('ошибка, введите число - 1 или 2')
                q = int(input('введите ответ '))
            break
        except ValueError:
            print('ошибка, введите число')
    return q

def RE():
    print('вопрос 5а')
    q5a = vopros5(RE5a)
    print('вопрос 5б')
    q5b = vopros5(RE5b)
    print('вопрос 5в')
    q5c = vopros5(RE5c)
    REsum = q5a + q5b + q5c 
    RE = ((REsum - 3)/3)*100
##    print('RE = ', RE)
    return RE

RE5a = 0
RE5b = 0
RE5c = 0
RE = RE()

#вопрос 6
while True:
    try:
        q6n = int(input('вопрос 6 '))
        while q6n < 0 or q6n > 5:
            print('ошибка, введите число от 0 до 5')
            q6n = int(input('вопрос 6 '))
        break
    except ValueError:
        print('ошибка, введите число от 0 до 5')

q6 = None
if q6n == 1:
    q6 = 5
if q6n == 2:
    q6 = 4
if q6n == 3:
    q6 = 3
if q6n == 4:
    q6 = 2
if q6n == 5:
    q6 = 1
##print('q6 = ', q6)

#вопрос 7 и вопрос 8
def vopros7_var_ab(x): #рассчет вопроса 7 (вариант А и В)
    vopros7 = None
    if x == 1:
        vopros7 = 6
    if x == 2:
        vopros7 = 5.4
    if x == 3:
        vopros7 = 4.2
    if x == 4:
        vopros7 = 3.1
    if x == 5:
        vopros7 = 2.2
    if x == 6:
        vopros7 = 1
##    print('вопрос 7 =', vopros7)
    return vopros7
        
def vopros8_var_a(x, y): # рассчет вопроса 8 (вариант А)
    vopros8 = None
    if x == 1 and y == 1:
        vopros8 = 6
        
    if x == 2 and y == 1:
        vopros8 = 5
        
    if x == 3 and y == 1:
        vopros8 = 5
        
    if x == 4 and y == 1:
        vopros8 = 5
        
    if x == 5 and y == 1:
        vopros8 = 5
        
    if x == 6 and y == 1:
        vopros8 = 5
        
    if y == 2:
        vopros8 = 4
        
    if y == 3:
        vopros8 = 3
        
    if y == 4:
        vopros8 = 2
        
    if x == 5:
        vopros8 = 1
##    print('вопрос 8 =', vopros8)
    return vopros8

def vopros8_var_c(x): #рассчет вопроса 8 (вариант С)
    vopros8 = None
    if x == 1:
        vopros8 = 6
    if x == 2:
        vopros8 = 4.75
    if x == 3:
        vopros8 = 3.5
    if x == 4:
        vopros8 = 2.25
    if x == 5:
        vopros8 = 1
    return vopros8

def BP(x, y):
    BP = (((x + y) - 2)/10) * 100 #универсальный рассчет BP для всех вариантов
##    print('BP =', BP)
    return BP
    


#в зависимости от введенных вариантов, возможны несколько
#сценариев перерасчета сырых баллов

while True:  #ввод вопроса №7
    try:
        v7 = int(input('введите ответ на вопрос 7 '))
        while v7 < 0 or v7 > 6:
            print('ошибка, введите число от 0 до 6')
            v7 = int(input('введите ответ на вопрос 7 еще раз '))
        break
    except ValueError:
        print('ошибка, введите число от 0 до 6')


while True: #ввод вопроса #8
    try:
        v8 = int(input('введите ответ на вопрос 8 '))
        while v8 < 0 or v8 > 5:
            print('ошибка, введите число от 0 до 5')
            v8 = int(input('введите ответ на вопрос 8 еще раз '))
        break
    except ValueError:
        print('ошибка, введите число от 0 до 5')
    


if v7 > 0 and v8 > 0: #вариант А (имеются ответы на оба вопроса)
    vopros7 = vopros7_var_ab(v7)
    vopros8 = vopros8_var_a(v7, v8)
    BP = BP(vopros7, vopros8)
    
if v7 > 0 and v8 == 0: # вариант В (есть ответ на вопрос 7, нет на 8)
    vopros7 = vopros7_var_ab(v7)
    vopros8 = vopros7
    BP = BP(vopros7, vopros8)

if v7 == 0 and v8 > 0: # вариант С (на 7 нет ответа, на 8 есть)
    vopros8 = vopros8_var_c(v8)
    vopros7 = vopros8
    BP = BP(vopros7, vopros8)
if v7 == 0 and v8 == 0: # вариант Д. программа дальше работать не будет.
    print('ошибка, необходимо дать ответ на вопросы 7 и/или 8 \nперезапустите программу')
    input()
    

#вопрос 9

def vopros9():
    while True:
        try:
            q9 = int(input('введите ответ '))
            while q9 < 1 or q9 > 6:
                print('ошибка, введите число от 1 до 6')
                q9 = int(input('введите ответ '))
            break
        except ValueError:
            print('введите число от 1 до 6')
    return q9

print('вопрос 9а')
v9a = vopros9()

q9a = None
if v9a == 1:
    q9a = 6
if v9a == 2:
    q9a = 5
if v9a == 3:
    q9a = 4
if v9a == 4:
    q9a = 3
if v9a == 5:
    q9a = 2
if v9a == 6:
    q9a = 1


print('вопрос 9б')
v9b = vopros9()

print('вопрос 9в')
v9c = vopros9()

print('вопрос 9г')
v9d = vopros9()
q9d = None
if v9d == 1:
    q9d = 6
if v9d == 2:
    q9d = 5
if v9d == 3:
    q9d = 4
if v9d == 4:
    q9d = 3
if v9d == 5:
    q9d = 2
if v9d == 6:
    q9d = 1

print('вопрос 9д')
v9e = vopros9()
q9e = None
if v9e == 1:
    q9e = 6
if v9e == 2:
    q9e = 5
if v9e == 3:
    q9e = 4
if v9e == 4:
    q9e = 3
if v9e == 5:
    q9e = 2
if v9e == 6:
    q9e = 1

print('вопрос 9е')
v9f = vopros9()

print('вопрос 9ж')
v9g = vopros9()

print('вопрос 9з')
v9h = vopros9()
q9h = None
if v9h == 1:
    q9h = 6
if v9h == 2:
    q9h = 5
if v9h == 3:
    q9h = 4
if v9h == 4:
    q9h = 3
if v9h == 5:
    q9h = 2
if v9h == 6:
    q9h = 1

print('вопрос 9и')
v9j = vopros9()

VTsum = q9a + q9e + v9g + v9j
VT = ((VTsum - 4) / 20) * 100
##print('VT =', VT)

MHsum = v9b + v9c + q9d + v9f + q9h
MH = ((MHsum - 5) / 25) * 100
##print('MH = ', MH)

#вопрос 10
while True:
    try:
        SF10 = int(input('вопрос 10 '))
        while SF10 < 0 or SF10 > 5:
            print('ошибка, введите число от 0 до 5')
            SF10 = int(input('вопрос 10 '))
        break
    except ValueError:
        print('ошибка, введите число от 0 до 5')

SFsum = q6 + SF10
SF = ((SFsum - 2)/8) * 100
##print('SF = ', SF)


def vopros11():
    while True:
        try:
            q11 = int(input('введите ответ '))
            while q11 < 1 or q11 > 5:
                print('ошибка, введите число от 1 до 5')
                q11 = int(input('введите ответ '))
            break
        except ValueError:
            print('введите число от 1 до 5')
    return q11

    
print('вопрос 11а')
v11a = vopros11()

print('вопрос 11б')
v11b = vopros11()
q11b = None
if v11b == 1:
    q11b = 5
if v11b == 2:
    q11b = 4
if v11b == 3:
    q11b = 3
if v11b == 4:
    q11b = 2
if v11b == 5:
    q11b = 1

print('вопрос 11в')
v11c = vopros11()

print('вопрос 11г')
v11d = vopros11()
q11d = None

if v11d == 1:
    q11d = 5
if v11d == 2:
    q11d = 4
if v11d == 3:
    q11d = 3
if v11d == 4:
    q11d = 2
if v11d == 5:
    q11d = 1

GHsum = v1 + v11a + q11b + v11c + q11d
GH = ((GHsum - 5) / 20) * 100
##print('GH = ', GH)


# рассчет шкал (8 штук)

print('Физическое функционирование (PF) =', round(PF, 1))
print('Ролевое функционирование, обусловленное физическим состоянием (RP) =', round(RP, 1))
print('Интенсивность боли (BP) =', round(BP, 1))
print('Общее состояние здоровья (GH) =', round(GH, 1))
print('Жизненная акивность (VT) =', round(VT, 1))
print('Социальное функционирование (SF) =', round(SF, 1))
print('Ролевое функционирование, обусловленное эмоциональным состоянием(RE) =', round(RE, 1))
print('Психическое здоровье (MH) =', round(MH, 1))
print()






PF_Z = (PF - 84.52404) / 22.89490
RP_Z = (RP - 81.19907) / 33.797290

BP_Z = (BP - 75.49196) / 23.558790
GH_Z = (GH - 72.21316) / 20.16964
VT_Z = (VT - 61.05453) / 20.86942
SF_Z = (SF - 83.59753) / 22.37642
RE_Z = (RE - 81.29467) / 33.02717
MH_Z = (MH - 74.84212) / 18.01189
##print('PF_Z = ', PF_Z, 'RP_Z = ', RP_Z, 'BP_Z = ', BP_Z, 'GH_Z = ', GH_Z, 
##    'VT_Z = ', VT_Z, 'SF_Z = ', SF_Z, 'RE_Z = ', RE_Z, 'MH_Z = ', MH_Z)      

##n1 = PF_Z * 0.42402
##n2 = RP_Z * 0.35119
##n3 = BP_Z * 0.31754
##n4 = SF_Z * -0.00753
##n5 = MH_Z * -0.22069
##n6 = RE_Z * -0.19206
##n7 = VT_Z * 0.02877
##n8 = GH_Z * 0.24954



PHsum = (PF_Z * 0.42402) + (RP_Z * 0.35119) + (BP_Z * 0.31754) +\
        (SF_Z * -0.00753) + (MH_Z * -0.22069) + (RE_Z * -0.19206) +\
        (VT_Z * 0.02877) + (GH_Z * 0.24954)
PH1 = (PHsum * 10) + 50
print('"Физический компонент здоровья" =', round(PH1, 2))
##print('"Физический компонент здоровья без округ" = ', PH1)


MHsum2 = (PF_Z * -0.22999) + (RP_Z * -0.12329) + (BP_Z * -0.09731) +\
         (SF_Z * 0.26876) + (MH_Z * 0.48581) + (RE_Z * 0.43407) +\
         (VT_Z * 0.23534) + (GH_Z * -0.01571)
##print('MH сумма = ', MHsum2)
PH2 = (MHsum2 * 10) + 50
print('"Психологический компонент здоровья" =', round(PH2, 2))
##print('"Психологический компонент здоровья без округл" = ', PH2)


input()

