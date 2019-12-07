import requests
import time
import codecs

def dir_brute(hedef,wordlist):
	print("")
	print("İşlem Başlıyor....")
	print("")
	bulunanlar = []
	with open(wordlist,encoding="utf-8",errors="ignore") as list1:
		dir_list = list1.read().splitlines()
	for dirList in dir_list:
		istek=requests.get(hedef+"/"+dirList)
		if istek.status_code == 404:
			print(hedef+"/"+dirList) 
		else:
			print(hedef+"/"+dirList+" "+"----> Bulundu")
			bulunanlar.append(hedef+"/"+dirList)
	print("")
	if bulunanlar==None:
		print("Bulunamadı")
		quit()
	else:
		sayi=0
		liste_sayisi=len(bulunanlar)
		while(sayi<liste_sayisi):
			print("Bulunan---->"+bulunanlar[sayi])
			sayi=sayi+1
	print("")

hedef = input("Hedef: ")
wordlist=input("Wordlist: ")

dir_brute(hedef,wordlist)