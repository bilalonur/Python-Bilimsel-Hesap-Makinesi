# Python ile Bilimsel Hesap Makinesi (math, eval)
# Bilal Onur Eskili  // 10.05.2020

import math as ma
pi = ma.pi
cos = ma.cos
d2r = ma.radians
lg = ma.log10
ln = ma.log
e = ma.e
krk = ma.sqrt

x = 1
print("-> Çıkış için 'cik' \n-> Komutlar için 'komut' ")
print()
while x != 'cik':
    x = eval(input(">> "))
    if x == 'komut':
        print("pi : pi sayısı \ncos : kosinüs \nd2r : dereceden radyana \nlg : logaritma (10 tabanında) \nln : logaritma (e tabanında) \ne : e sayısı \nkrk : karekök \n")
    else:
        print(x)