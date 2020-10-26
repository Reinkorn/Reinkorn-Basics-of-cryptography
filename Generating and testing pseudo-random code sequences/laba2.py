# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:45:58 2020

@author: gorod
"""

import random

def bin_to_dec(digit):           
    dlina=len(digit)           
    print (dlina)           
    chislo_dec=0           
    for i in range(0, dlina):               
        chislo_dec=chislo_dec+int(digit[i])*(2**(dlina-i-1))           
        return chislo_dec   

def space_message(sms):
    q = 0
    for i in range(len(sms)):
        if(len(sms[i]) != 7):
            q+= 1
    return q

def key_generation(len_message_binary):
    k = int(33)
    key_list=[]
    registor=[]
    input_file_key = (open('File/key.txt','w+',encoding='utf-8'))
    #input_file_key_1 = (open('File/key_1.txt','w+',encoding='utf-8'))
    condition=["0", "1"]
    
    v  =str(input(f'Загрузить начальные значения регистра из файла?(y/n):'))
    if (v == "y"):        
        input_file_registor = (open('File/registor.txt','r',encoding='utf-8'))
        registor_str = input_file_registor.read()
        registor = list(registor_str)
        #print(f'Начальное состояние регистра:{registor}')
        input_file_registor.close()
    else:
        input_file_registor = (open('File/registor.txt','w+',encoding='utf-8'))
        registor = random.choices(condition, k=33)
        registor_str ="".join(registor)
        input_file_registor.write(registor_str)
        #print(f'Начальное состояние регистра:{registor}')
    for i in range(len_message_binary+k):#формирование ключевой последовательности
        key_list.append(registor[-1])
        x1_param = str(int(registor[-1])^int(registor[12]))#P(x)=X^33+x^13+1=0
        registor.insert(0, x1_param)
        del registor[-1]
    #del key_list[-66:-1]#Чтобы убрать значения начальные
    key_list_str="".join(key_list)
    #print(f"Длинна ключа:{len(key_list_str)}")
    #print(f"Ключ:{key_list_str}")
    str(input_file_key.write(key_list_str))
    #str(input_file_key_1.write(key_list_str))
    input_file_registor.close()
    input_file_key.close()
    return key_list_str

def serial_test_2(key):
    x1=x2=x3=x4=0
    N_T=[]
    N_E=[]
    key_list_serial=[]
    key_list=list(key)
    if (len(key) % 2 == 1):
        for i in range(0,len(key)-1,2):
            key_list_serial.append(key_list[i]+key_list[i+1])
    else:
        for i in range(0,len(key),2):
            key_list_serial.append(key_list[i]+key_list[i+1])
    for i in key_list_serial:
        if i == "00":
            x1+=1
        elif i == "01":
            x2+=1
        elif i == "10":
            x3+=1
        elif i == "11":
            x4+=1
            
    N_E.append(x1/(len(key_list_serial)))
    N_E.append(x2/(len(key_list_serial)))
    N_E.append(x3/(len(key_list_serial)))
    N_E.append(x4/(len(key_list_serial)))
    
    n=4 #объявление переменной 2^k
    for i in range(n):
        N_T.append(0.25)
    X_2=0
    for i in range(n):
        X_2+=((N_E[i]-N_T[i])**2)/N_T[i]
    #print(X_2)
    #print(f"Серии по 2 бит ключа:{key_list_serial}")
   # print(f"Вероятности появления из сформированной выборки:{N_E}")
   # print(f"Вероятности появления теоретическая:{N_T}")
   # print(f'Хи-квадрат равен:{X_2}')

def cor_test():
    sum_key = 0
    sum_key_1 = 0
    input_file_key = (open('File/key.txt','r',encoding='utf-8'))
    key = str(input_file_key.read())
    key_1= key[-10:-1]+key[9:]
    input_file_key.close()
    
    for i in range(len(key)):
        sum_key+=int(key[i])
    for i in range(len(key_1)):
        sum_key_1+=int(key_1[i])
    
    top_sum_1=0
    low_sum_1=0
    low_sum_2=0
    
    for i in range(len(key)):
        top_sum_1+=int(key[i])*int(key_1[i])
    for i in range(len(key)):
        low_sum_1+=int(key[i])**2
    for i in range(len(key)):
        low_sum_2+=int(key_1[i])**2  
        
    R= (len(key)*top_sum_1 - (sum_key*sum_key_1))/pow(((len(key)*low_sum_1 - sum_key**2)*(len(key)*low_sum_2 - sum_key_1**2)) ,0.5)
    R_mod =(1/(len(key)-1))+(2/(len(key)-2))*pow(((len(key))*((len(key))-3))/(len(key)+1) , 0.5)
    #print(f'Коэффициент автокорреляции при k=1:{R}')
    #print(f'Модульное значение (8):{R_mod}')

shifrotext_list_list=[]
message_binary_list_key=[]
message_binary_list=[]
message_binary_list_str_key=[]
input_file_txt = (open('File/text.txt','r',encoding='utf-8'))
input_file_txt_shifrotext =(open('File/shifrotext.txt','w+',encoding='utf-8'))
message=str(input_file_txt.read())
message_ascii=[ord(i) for i in message]
message_binary=[format(i,'b') for i in message_ascii]
q_space = space_message(message_binary)
len_message_binary = len(message_binary) * 7 - q_space
key = key_generation(len_message_binary)
serial_test_2(key)
cor_test()

z = 0
for i in range(len(message_binary)):
    message_binary_list_key.append(list(message_binary[i]))
    message_binary_list.append(list(message_binary[i]))
for i in range(len(message_binary)):
    for j in range(len(message_binary[i])):
        message_binary_list_key[i][j]=key[z]
        z+=1
z = 0
for i in range(len(message_binary)):
    message_binary_list_str_key.append("".join(message_binary_list_key[i]))

for i in range(len(message_binary)):
    for j in range(len(message_binary[i])):
        shifrotext_list_list.append(int(message_binary_list_key[i][j])^int(message_binary_list[i][j]))

print(message_binary_list_str_key[1])
print(message_binary[1])
print(shifrotext_list_list)
#a=input("Введите двоичное целое число =")   
#print("Двоичное целое число",a,"соответствует десятичному числу ", bin_to_dec(a))
#for i in range (len(message_binary))
#
#str(input_file_txt_shifrotext.write())
input_file_txt.close()








