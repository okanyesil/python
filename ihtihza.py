# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:20:07 2019

@author: OKAN
"""


#%%
dosya=open("deneme.txt","w")
print("hello txt dosyasi",file=dosya)
dosya.close()
import os
os.getcwd()#dosyanın dizinini verir
#%%
f=open("yazi.text","w")
print("bu txt dosyasına yazılacak",file=f)
print("ayrıyaten bu da txtye yazılacak",file=f)
f.close()

#%%
print(*"TBMM",sep=".")
#%%
import sys
sys.stdout
a=open("deneme.txt","w")
sys.stdout=a
print("bunu direk yazdiracak",flush=True)
print(sys.stdout,flush=True)