# verilen yılın yüzyıl karşılığını veren program
def hesapla(yil):#int tipinde bir değişken alıyoruz
    str_yil=str(yil)
    if(len(str_yil)==2): # 10 20 40 45 99 gibi
        return 1
    elif(len(str_yil)==3):
        if(str_yil[1:2]=="00"):
            return int(str_yil[0])
        else:
            return int(str_yil[0])+1
    elif(len(str_yil)==4):
        if(str_yil[2:4]=="00"):
            return int(str_yil[:2])
        else:
            return int(str_yil[:2])+1
hesapla(2001)


