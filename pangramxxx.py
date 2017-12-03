
"""Created by Zamanusta - Genetik Algoritma kullanarak bir metinden pangram yaratma - 03.11.2017"""

import random
from random import randint
import sys

sys.setrecursionlimit(100000)  # 10000 is an example, try with different values

llist = 0
sayac = 0
msay = 0
deneme = 50000
mutoran = 10


def read_words(words_file):
    with open(words_file, 'r') as infile:
        lst = []
        for line in infile:
            words = line.split()
            for word in words:
                if word not in lst:
                    lst.append(word)  # append only this word to the list, not all words on this line
        lst.sort()
        print("TOPLAM FARKLI KELİME SAYISI: %i" % len(lst))
        print(lst)
        global llist
        llist = len(lst)
        return lst
        # return [word for line in open(words_file, 'r') for word in line.split()]


def birle(phraselst):
    kubu = ''.join(phraselst)
    return kubu


def yarat(c):
    global llist, deneme, mutoran
    print("%s kelimelik denemeyle başlanıyor:" % c)
    print("Her turda nesil sayısı: %s, Mutasyon oranı: %f" % (deneme, (1 / mutoran)))
    ilkgenler = random.sample(range(0, llist), int(c * 2))
    anax = ilkgenler[0:int(c)]
    babax = ilkgenler[int(c):int(c * 2)]
    print("ilk anne:", yazdir(anax))
    print("ilk baba:", yazdir(babax))
    print("...")
    return anax, babax, c


def nesil(e1, e2, n):
    global llist, deneme
    k = n / 2
    bebs = []
    u = []
    bebek1 = e1[0:int(k)] + e2[0:int(k)]
    bebek2 = e1[0:int(k)] + e2[int(k):int(n)]
    bebek3 = e1[int(k):int(n)] + e2[0:int(k)]

    if randint(0, mutoran) != 1:
        bebek4 = e1[int(k):int(n)] + e2[int(k):int(n)]
    else:
        global msay
        msay += 1
        mutantgen = random.sample(range(0, llist), int(n / 2))
        bebek4 = e1[int(k):int(n)] + mutantgen

    u.append(len(is_pangram(yazdir(bebek1))))
    u.append(len(is_pangram(yazdir(bebek2))))
    u.append(len(is_pangram(yazdir(bebek3))))
    u.append(len(is_pangram(yazdir(bebek4))))
    bebs.append(bebek1)
    bebs.append(bebek2)
    bebs.append(bebek3)
    bebs.append(bebek4)

    sbebs = [x for _, x in sorted(zip(u, bebs))]
    u = sorted(u)
    yenianne = sbebs[0]
    yenibaba = sbebs[1]

    global sayac
    sayac += 1

    if sayac == deneme and n < 41 and u[0] != 0:
        n += 2
        print("%s nesilde bulunamadı. %s kez mutasyon gerçekleşti. en iyi aday:" % (sayac, msay))
        print(yazdir(bebek1))
        print("eksik harfler:%s" % is_pangram(yazdir(sbebs[0])))
        print("%s kelimelik yeni nesillere başlanıyor..." % n)
        print("...")
        msay = 0
        sayac = 0
        return yenianne, yenibaba, n
    elif u[0] == 0:
        print("BULDUK")
        silinecekler = []
        bulunan = list(set(sbebs[0]))
        bulunanx = yazdir(bulunan)
        bulunany = bulunan
        for w in range(0, len(set(sbebs[0]))):
            bulunan = list(set(sbebs[0]))
            del bulunan[w]
            if len(is_pangram(bulunanx)) == len(is_pangram(yazdir(bulunan))):
                silinecekler.append(bulunany[w])
        for w in silinecekler:
            bulunany.remove(w)
        print(yazdir(bulunany))
        vur = len(yazdir(bulunany))
        print("Toplam nesil sayısı: %i, Vuruş Sayısı: %i" % (int(((n - 3) * deneme / 2) + sayac), vur))
        return True, True, True
    else:
        return yenianne, yenibaba, n


def is_pangram(phrase):
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    return set(alphabet) - set(phrase)


def yazdir(lst):
    cumle = []
    for w in lst:
        cumle.append(liste[w])
        cumle.append(' ')
    yazi = ''.join(cumle)
    return yazi



#Fonksiyonlar sonu

yol = "digermetinler/safsata.txt" #dosya yolu buradan verilir.
liste = read_words(yol)
liste = [w.lower() for w in liste]
liste = [w.replace('â', 'a').replace('î', 'i').replace('û', 'u') for w in liste]
ozelkaldir = str.maketrans("", "", "?)(,.’\"“”…:;")
liste = [w.translate(ozelkaldir) for w in liste]
# TEST
testyazi = ''.join(liste)
if len(is_pangram(testyazi)) > 0:
    print("BU METİN TÜRKÇE'DEKİ TÜM HARFLERİ İÇERMİYOR. PANGRAM MÜMKÜN DEĞİL")
else:
    print("ÖZEL KARAKTERLERDEN TEMİZLENDİ:")
    print(liste)
    print("...")
    sayac = 0
    ana, baba, i = yarat(4)
    yana, ybaba, yi = nesil(ana, baba, i)
    while yana is not True:
        yana, ybaba, yi = nesil(yana, ybaba, yi)
