import requests
from bs4 import BeautifulSoup
from notifypy import Notify

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}

request = requests.get("https://www.doviz.com/", headers=header)

tumVeriler = BeautifulSoup(request.content, "html.parser")

tumVeriler = tumVeriler.find("div", {"class": "market-data"}).findAll("div", {"class": "item"})

bitcoin = tumVeriler[5].find("span", {"class": "value"}).text

bitcoin = list(bitcoin)
bitcoin.pop(0)
yeniDeger = "".join(bitcoin)


def notify_user():
    notification = Notify()
    notification.title = "Bitcoin Degeri"
    notification.message = yeniDeger + "$"
    notification.icon = "bitcoin.jpg"
    notification.send()


notify_user()
