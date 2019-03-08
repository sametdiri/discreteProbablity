##186112002 - Samet Diri
##
##Ayrık Sistemler İçin İleri Olasılık Dersi
##
##Hafta-2: Sayma
##
##Ödev: 1
##
##Ödev Konusu: Güvercin Yuvası
##
##Örnek Kaynağı: https://www.geeksforgeeks.org/discrete-mathematics-the-pigeonhole-principle/
##
##Örnek:
##Bir torbada 10 kırmızı misket, 10 beyaz misket ve 10 mavi misket vardır.
##Torbadan rastgele seçilen 4 tane misketin aynı renk olması en az kaç misket seçilmeli?
##
##Renk Sayısı (Yuva): n=3
##Misket Sayısı (Güvercin): K+1=4
##Böylece en az gerekli misket sayısı: Kn+1=10
##Sağlaması: (Kn+1)/n = 4 ise
##(Kn+1/3) = 4
##Kn+1 = 10'dur.
##Örneğin; 3 kırmızı + 3 beyaz + 3 mavi + 1(kırmızı|beyaz|mavi) = 10
##
##Example:
##A bag contains 10 red marbles, 10 white marbles, and 10 blue marbles.
##What is the minimum no. of marbles you have to choose randomly from the bag
##to ensure that we get 4 marbles of same color?
##
##Solution: 
##No. of colors (pigeonholes) n = 3
##No. of marbles (pigeons) K+1 = 4
##Therefore the minimum no. of marbles required = Kn+1
##By simplifying we get Kn+1 = 10.
##Verification: ceil[Average] is [Kn+1/n] = 4
##[Kn+1/3] = 4
##Kn+1 = 10
##i.e., 3 red + 3 white + 3 blue + 1(red or white or blue) = 10


print("Bir torbada 10 kırmızı misket, 10 beyaz misket ve 10 mavi misket vardır."+
      "Torbadan rastgele seçilen 4 tane misketin aynı renk olması en az kaç misket seçilmeli?")
print("Yuva sayısı: 3")
print("Güvercin sayısı: 4")

n = 3
K = 3
n = (10 - 1) / 3
print("En az 4 misketin aynı renk olması için " + str(n) + " tur misket seçilmelidir.")
