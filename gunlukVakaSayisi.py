from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}

request = requests.get('https://news.google.com/covid19/map?hl=tr&mid=%2Fm%2F02j71&gl=TR&ceid=TR%3Atr', headers=header)
ulkeAdi = input("lütfen arama yapmak istediğiniz ülkeyi giriniz")
soup = BeautifulSoup(request.content, "html.parser")

veriler = soup.find("tbody", {"class": "ppcUXd"})
liste = []
deger = veriler.find_all("tr")
print("-"*20, ulkeAdi+" Corona Tablosu", "-"*20)
for deg in deger:
    if deg.find("th").find("div").text == ulkeAdi:
        for veri in deg.find_all("td"):
            liste.append(veri.text)
print("Toplam vaka sayısı:" + liste[0])
print("Yeni Vaka sayisi:" + liste[1])
print("Bir milyon kişi başına vaka:" + liste[3])
print("Ölüm:" + liste[4])


