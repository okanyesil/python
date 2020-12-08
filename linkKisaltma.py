import pyshorteners
import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
url = tk.StringVar()
shorted_link = tk.Entry(root, width=40)
def shortner():
        link = url.get()
    short = pyshorteners.Shortener()
    short_link = short.tinyurl.short(link)
    shorted_link.insert(0, short_link)
url.set("")
url_label = tk.Label(root, text="Kısaltılacak Urlyi Giriniz:")
url_entry = tk.Entry(root, textvariable=url, width=80)
sub_btn = tk.Button(root, text="Url Kısalt", command=shortner)

url_label.grid(row=0, column=0)
url_entry.grid(row=0, column=1)
sub_btn.grid(row=1, column=0)
shorted_link.grid(row=2, column=1)
root.mainloop()



#url = input("Enter Url: ")
#final = shortner(url)
#print(f"Shortened Link is {final}")
