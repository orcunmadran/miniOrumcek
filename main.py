import time

from dataURL import DataURL
useDataURL = DataURL()

print("-: Mini Örümceğe hoş geldiniz! :-")
print("|------------------------------|")
print("")
time.sleep(2)

while True:
    print("Menü: (0)Çıkış (1)URL Listele || (2)URL Ekle")
    menuSecim = int(input("Tercihiniz: "))
    if menuSecim == 0:
        print("Mini Örümcek kapatılıyor...")
        time.sleep(1)
        break
    elif menuSecim == 1:
        useDataURL.dataRead()
    elif menuSecim == 2:
        useDataURL.dataWrite()