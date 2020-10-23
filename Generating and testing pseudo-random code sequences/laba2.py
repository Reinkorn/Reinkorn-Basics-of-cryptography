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
    k = int(4)
    key_list=[]
    registor=[]
    input_file_key = (open('File/key.txt','w+',encoding='utf-8'))
    input_file_registor = (open('File/registor.txt','w+',encoding='utf-8'))
    condition=["0", "1"]
    registor= random.choices(condition, k=4)
    print(registor)
    for i in range(len_message_binary+k):
        key_list.append(registor[-1])
        x1_param = str(int(registor[-1])^int(registor[-2]))
        registor.insert(0, x1_param)
        del registor[-1]
    print(key_list)
    #key = str(input_file_key.write(key_list))
    
input_file = (open('File/text.txt','r',encoding='utf-8'))
message=str(input_file.read())
message_ascii=[ord(i) for i in message]
message_binary=[format(i,'b') for i in message_ascii]
q_space = space_message(message_binary)
len_message_binary = len(message_binary) * 7 - q_space
key_generation(len_message_binary)






