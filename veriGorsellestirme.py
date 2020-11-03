import matplotlib.pyplot as plt
import sqlite3 as sql
from datetime import datetime
connection = sql.connect("dolarVeritabani.db")

result = connection.execute("SELECT * FROM dolarTablo")
dolarData = []
tarihData = []
for data in result:
    dolarData.append(data[0])
    tarihData.append(str(data[1]).split(' ')[1].split('.')[0])



plt.figure(figsize=(13, 8))

plt.plot(tarihData, dolarData)
plt.xticks(tarihData, rotation="vertical")
plt.tick_params(axis='x', which ='major', labelsize=8)
plt.title("50snlik Zamana Göre Dolar kuru Grafiği")
plt.xlabel("Zaman")
plt.ylabel("dolar kuru")
plt.show()
