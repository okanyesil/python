import requests
from bs4 import BeautifulSoup
import sqlite3 as sql
from datetime import datetime
import time
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}
vt = sql.connect("dolarVeritabani.db")
while True:
    r = requests.get('https://www.doviz.com/', headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    veriler = soup.find("div", {"class": "market-data"})
    veriler = veriler.find_all("div", {"class": "item"})
    dolarKur = veriler[1].find("span", {"class": "value"}).text
    tarih = datetime.now()
    im = vt.cursor()
    im.execute("INSERT INTO dolarTablo VALUES (?, ?)", (dolarKur, tarih))
    vt.commit()
    time.sleep(50)
vt.close()
