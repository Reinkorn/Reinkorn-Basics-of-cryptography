# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:09:35 2020

@author: gorod
"""
import random

input_file = (open('text.txt','r',encoding='utf-8'))
ALF = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
KEY=ALF
otbivka=str(input_file.read())
v=str(input(f'Введите что вы хотите сделать?(Расшифровать или Зашифровать):'))
if (v=="Зашифровать"): 
    key = (open('key.txt','w+', encoding='utf-8'))
    random.shuffle(KEY)#перемешиваем алфавит
    for i in range(0,32):#записываем ключ 
        key.write(str(KEY[i]))     
    for i in range(1,len(otbivka)):    
        if (otbivka[i]=="а"):
            otbivka = otbivka[:i] + KEY[0]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="б"):
            otbivka = otbivka[:i] + KEY[1]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="в"):
            otbivka = otbivka[:i] + KEY[2]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="г"):
            otbivka = otbivka[:i] + KEY[3]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="д"):
            otbivka = otbivka[:i] + KEY[4]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="е"):
            otbivka = otbivka[:i] + KEY[5]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ж"):
            otbivka = otbivka[:i] + KEY[6]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="з"):
            otbivka = otbivka[:i] + KEY[7]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="и"):
            otbivka = otbivka[:i] + KEY[8]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="й"):
            otbivka = otbivka[:i] + KEY[9]+ otbivka[i+1:]
        elif (otbivka[i]=="к"):
            otbivka = otbivka[:i] + KEY[10]+ otbivka[i+1:]
        elif (otbivka[i]=="л"):
            otbivka = otbivka[:i] + KEY[11]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="м"):
            otbivka = otbivka[:i] + KEY[12]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="н"):
            otbivka = otbivka[:i] + KEY[13]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="о"):
            otbivka = otbivka[:i] + KEY[14]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="п"):
            otbivka = otbivka[:i] + KEY[15]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="р"):
            otbivka = otbivka[:i] + KEY[16]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="с"):
            otbivka = otbivka[:i] + KEY[17]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="т"):
            otbivka = otbivka[:i] + KEY[18]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="у"):
            otbivka = otbivka[:i] + KEY[19]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ф"):
            otbivka = otbivka[:i] + KEY[20]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="х"):
            otbivka = otbivka[:i] + KEY[21]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ц"):
            otbivka = otbivka[:i] + KEY[22]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ч"):
            otbivka = otbivka[:i] + KEY[23]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ш"):
            otbivka = otbivka[:i] + KEY[24]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="щ"):
            otbivka = otbivka[:i] + KEY[25]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ъ"):
            otbivka = otbivka[:i] + KEY[26]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ы"):
            otbivka = otbivka[:i] + KEY[27]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ь"):
            otbivka = otbivka[:i] + KEY[28]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="э"):
            otbivka = otbivka[:i] + KEY[29]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="ю"):
            otbivka = otbivka[:i] + KEY[30]+ otbivka[i+1:]#точно
        elif (otbivka[i]=="я"):
            otbivka = otbivka[:i] + KEY[31]+ otbivka[i+1:]#точно
        else:
            continue    
    ztext = (open('zashifrovantext.txt','w+', encoding='utf-8'))
    ztext.write(otbivka)
    ztext.close()
    key.close()
elif (v=="Расшифровать"): 
    sh=(open('zashifrovantext.txt','r',encoding='utf-8'))
    otbivka=str(sh.read())
    key = (open('key.txt','r', encoding='utf-8'))
    for i in range(0,32):#записываем ключ 
        KEY[i]=key.read(1)
    for i in range(1,len(otbivka)):    
        if (otbivka[i]==KEY[0]):
            otbivka = otbivka[:i] + "a"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[1]):
            otbivka = otbivka[:i] + "б"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[2]):
            otbivka = otbivka[:i] + "в"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[3]):
            otbivka = otbivka[:i] + "г"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[4]):
            otbivka = otbivka[:i] + "д"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[5]):
            otbivka = otbivka[:i] + "е"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[6]):
            otbivka = otbivka[:i] + "ж"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[7]):
            otbivka = otbivka[:i] + "з"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[8]):
            otbivka = otbivka[:i] + "и"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[9]):
            otbivka = otbivka[:i] + "й"+ otbivka[i+1:]
        elif (otbivka[i]==KEY[10]):
            otbivka = otbivka[:i] + "к"+ otbivka[i+1:]
        elif (otbivka[i]==KEY[11]):
            otbivka = otbivka[:i] + "л"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[12]):
            otbivka = otbivka[:i] + "м"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[13]):
            otbivka = otbivka[:i] + "н"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[14]):
            otbivka = otbivka[:i] + "о"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[15]):
            otbivka = otbivka[:i] + "п"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[16]):
            otbivka = otbivka[:i] + "р"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[17]):
            otbivka = otbivka[:i] + "с"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[18]):
            otbivka = otbivka[:i] + "т"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[19]):
            otbivka = otbivka[:i] + "у"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[20]):
            otbivka = otbivka[:i] + "ф"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[21]):
            otbivka = otbivka[:i] + "х"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[22]):
            otbivka = otbivka[:i] + "ц"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[23]):
            otbivka = otbivka[:i] + "ч"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[24]):
            otbivka = otbivka[:i] + "ш"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[25]):
            otbivka = otbivka[:i] + "щ"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[26]):
            otbivka = otbivka[:i] + "ъ"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[27]):
            otbivka = otbivka[:i] + "ы"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[28]):
            otbivka = otbivka[:i] + "ь"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[29]):
            otbivka = otbivka[:i] + "э"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[30]):
            otbivka = otbivka[:i] + "ю"+ otbivka[i+1:]#точно
        elif (otbivka[i]==KEY[31]):
            otbivka = otbivka[:i] + "я"+ otbivka[i+1:]#точно
        else:
            continue
    rtext = (open('rasshifrovantext.txt','w+', encoding='utf-8'))
    rtext.write(otbivka)
    rtext.close()
    key.close()
    sh.close()
else:
    print(f'Некорректный ввод!')
input_file.close()
