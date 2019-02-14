# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:03:57 2019

@author: OKAN
"""

#print komutu ile txt dosyasına veri yazma

dosya=open("isim.txt","w")
print("Okan Yesiloglu",file=dosya)
dosya.close()