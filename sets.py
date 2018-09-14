# w3school'dan takip ettiğim python derslerinin sets konusu örnekleri.

new_sets={"Java","c#","c++","c","ruby"}#sets küme parantezi içerisinde tanımlanır.
print(new_sets)
#sets sayılamayan ve indexlenemez
for y in new_sets:
  print(y)
#sets'i bir döngü içerisinde yazdırabiliriz.
print("c#" in new_sets)#setin içindeki veriyi in komutuyla arayabiliriz
#eğer değer içinde varsa true değerini döndürecektir.
#eğer setsi güncellemek istiyorsak update veya add komutunu kullanabiliriz.
#tek veri için add, birden fazla veri için update komutunu kullanabiliriz.
new_sets.add("css")
print(new_sets) #değerleri index olarak atamaz.
new_sets.update(["html","ruby","python"])
print(new_sets)
#update komutunu köşeli parantezler yardımıyla kullanılır.
print(len(new_sets))#setimizin eleman sayısını verir.
# setsimizden değer silmek için remove ya da discard() methodları kullanılır.
# not listlerede olduğu gibi index numarası vererek diziden değer silemeyiz.
new_sets.remove("css")
print(new_sets)
# Discard ile remove arasındaki en büyük fark ise 
# remove silmek istedğimz değer yoksa hata verirken
# Discard silmek istedğimiz değer yoksa hata vermez
new_sets.discard("html")
print(new_sets)