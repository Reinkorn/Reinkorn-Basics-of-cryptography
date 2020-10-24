# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:45:58 2020

@author: gorod
"""

import random
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
        key_list_str="".join(key_list)
    print(f"Длинна ключа:{len(key_list_str)}")
    print(f"Ключ:{key_list_str}")
    str(input_file_key.write(key_list_str))
    input_file_registor.close()
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
    
    print(f"Серии по 2 бит ключа:{key_list_serial}")
    print(f"Вероятности появления:{N_E}")
    
    
input_file_txt = (open('File/text.txt','r',encoding='utf-8'))
message=str(input_file_txt.read())
message_ascii=[ord(i) for i in message]
message_binary=[format(i,'b') for i in message_ascii]
q_space = space_message(message_binary)
len_message_binary = len(message_binary) * 7 - q_space
key = key_generation(len_message_binary)
serial_test_2(key)







