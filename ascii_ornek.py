# -*- coding: utf-8 -*-
#azatdicle
print("""

ASCII Latin alfabesi üzerine kurulu 7 bitlik bir karakter kümesidir.
İlk kez 1963 yılında ANSI tarafından standart olarak sunulmuştur.
ASCII'de 33 tane basılmayan kontrol karakteri ve 95 tane basılan karakter bulunur.       
@azatdicle                      
""")
#A-Z 65-90      
#a-z 97-122     

harf = input("Harf giriniz:")

if ord(harf) <=90 and ord(harf) >=65:
    print("{} Gridiginiz Karekter Buyuk : ascii kodu {}".format(harf,ord(harf)))
elif ord(harf) >=97 and ord(harf) <=122:
    print("{} Girdiginiz Karekter Kucuk : ascii kodu {}".format(harf,ord(harf)))
else:
    print("Girdiginz karakter latin alfabede yok")

print("")
print("")

secenek=input("Tum ascii Karekter kodlari gosterilsinmi: E/H: ")
alfabe_buyuk=["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alfabe_kucuk=["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if secenek=="E" or secenek=="e":
    for x in alfabe_buyuk:
        print("Buyuk olan:Karekter {} : ascii kodu {}".format(x,ord(x)))
    for j in alfabe_kucuk:
        print("Kucuk olan:Karekter {} : ascii kodu {}".format(j,ord(j)))
elif secenek=="H" or secenek=="h":
    print("by by ... :)")
else:
    print("Hatli tuslama")