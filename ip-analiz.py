import requests

print("")
print("-"*30)
print("        Ip Analizi")
print("-"*30)
print("")
def istek(ip):
	istek=requests.get("http://ipapi.co/"+ip+"/json")
	print(istek.text)
	print("")
	
ip=input("Ip Adresini Giriniz: ")
print("")

istek(ip)