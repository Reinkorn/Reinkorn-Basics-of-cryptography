# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:21:11 2020

@author: gorod
"""
def count(my_string):
    print(f"Количество букв а:{my_string.count('а')}")
    print(f"Количество букв б:{my_string.count('б')}")
    print(f"Количество букв в:{my_string.count('в')}")
    print(f"Количество букв г:{my_string.count('г')}")
    print(f"Количество букв д:{my_string.count('д')}")
    print(f"Количество букв е:{my_string.count('е')}")
    print(f"Количество букв ё:{my_string.count('ё')}")
    print(f"Количество букв ж:{my_string.count('ж')}")
    print(f"Количество букв з:{my_string.count('з')}")
    print(f"Количество букв и:{my_string.count('и')}")
    print(f"Количество букв й:{my_string.count('й')}")
    print(f"Количество букв к:{my_string.count('к')}")
    print(f"Количество букв л:{my_string.count('л')}")
    print(f"Количество букв м:{my_string.count('м')}")
    print(f"Количество букв н:{my_string.count('н')}")
    print(f"Количество букв о:{my_string.count('о')}")
    print(f"Количество букв п:{my_string.count('п')}")
    print(f"Количество букв р:{my_string.count('р')}")
    print(f"Количество букв с:{my_string.count('с')}")
    print(f"Количество букв т:{my_string.count('т')}")
    print(f"Количество букв у:{my_string.count('у')}")
    print(f"Количество букв ф:{my_string.count('ф')}")
    print(f"Количество букв х:{my_string.count('х')}")
    print(f"Количество букв ц:{my_string.count('ц')}")
    print(f"Количество букв ч:{my_string.count('ч')}")
    print(f"Количество букв ш:{my_string.count('ш')}")
    print(f"Количество букв щ:{my_string.count('щ')}")
    print(f"Количество букв ъ:{my_string.count('ъ')}")
    print(f"Количество букв ы:{my_string.count('ы')}")
    print(f"Количество букв ь:{my_string.count('ь')}")
    print(f"Количество букв э:{my_string.count('э')}")
    print(f"Количество букв ю:{my_string.count('ю')}")
    print(f"Количество букв я:{my_string.count('я')}")
input_file = (open('10_crypt.txt','r',encoding='utf-8'))
output_file = open('10_cryptGOOD.txt','w',encoding='utf-8')
my_string = str(input_file.read())
input_file.close()
count(my_string)
otbivka=my_string
for i in range(1,len(otbivka)):
    if (otbivka[i]=="в"):
        otbivka = otbivka[:i] + "о"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="д"):
        otbivka = otbivka[:i] + "г"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ю"):
        otbivka = otbivka[:i] + "д"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ъ"):
        otbivka = otbivka[:i] + "е"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="и"):
        otbivka = otbivka[:i] + "а"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="м"):
        otbivka = otbivka[:i] + "н"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="у"):
        otbivka = otbivka[:i] + "и"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ч"):
        otbivka = otbivka[:i] + "с"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="а"):
        otbivka = otbivka[:i] + "в"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="э"):
        otbivka = otbivka[:i] + "р"+ otbivka[i+1:]
    elif (otbivka[i]=="т"):
        otbivka = otbivka[:i] + "л"+ otbivka[i+1:]
    elif (otbivka[i]=="ш"):
        otbivka = otbivka[:i] + "к"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ц"):
        otbivka = otbivka[:i] + "м"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ж"):
        otbivka = otbivka[:i] + "п"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="н"):
        otbivka = otbivka[:i] + "т"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="р"):
        otbivka = otbivka[:i] + "ж"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="л"):
        otbivka = otbivka[:i] + "щ"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="п"):
        otbivka = otbivka[:i] + "ц"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="х"):
        otbivka = otbivka[:i] + "й"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="с"):
        otbivka = otbivka[:i] + "у"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ф"):
        otbivka = otbivka[:i] + "б"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="щ"):
        otbivka = otbivka[:i] + "я"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="я"):
        otbivka = otbivka[:i] + "ш"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="б"):
        otbivka = otbivka[:i] + "ч"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="о"):
        otbivka = otbivka[:i] + "х"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="г"):
        otbivka = otbivka[:i] + "ю"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="ь"):
        otbivka = otbivka[:i] + "ф"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="й"):
        otbivka = otbivka[:i] + "ъ"+ otbivka[i+1:]#точно
    elif (otbivka[i]=="е"):
        otbivka = otbivka[:i] + "ь"+ otbivka[i+1:]#точно
    else:
        continue
output_file.write(otbivka)
output_file.close()