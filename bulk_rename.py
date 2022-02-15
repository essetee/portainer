#! /usr/bin/python3
from genericpath import isfile
import os


extensions = ['.png', '.jpg', '.jpeg', '.webp', '.bmp']
tel = 1

for x in os.listdir():
    if isfile(x):
        name = str(x)
        namex = "'" + name + "'"
        name_low = name.lower()
        if name_low != name:
            cmd = 'mv ' + namex + ' ' + name_low
            os.system(cmd)

for x in os.listdir():
    if isfile(x):
        name = str(x)
        namex = "'" + name + "'"
        if name.__contains__(' '):
            name2 = name.replace(' ', '_')
            cmd = 'mv ' + namex + ' ' + name2
            os.system(cmd)
            # print(f"moving {name} to {name2}")

for x in os.listdir():
    if isfile(x):
        name = str(x)
        name2 = name.split('.')
        extens = name2[-1]
        extens = "." + extens
        if extens in extensions:
            r = range(0, 10)
            r2 = range(10, 100)
            r3 = range(100, 1000)
            r4 = range(1000, 10000)
            r5 = range(10000, 100000)
            if tel in r:
                pre = "img0000" + str(tel)
            if tel in r2:
                pre = "img000" + str(tel)
            if tel in r3:
                pre = "img00" + str(tel)
            if tel in r4:
                pre = "img0" + str(tel)
            if tel in r5:
                pre = "img" + str(tel)
            tel = tel + 1
            wname = pre + extens
            os.system('mv ' + name + ' ' + wname)





        


  
