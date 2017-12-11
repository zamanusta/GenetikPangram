# GenetikPangram

Pangram bir dilin alfabesindeki tüm harfleri içeren anlamlı cümleye denir. Kelimenin kaynağı Yunancada'dır. Bütün, hepsi anlamına gelen "pan" ve harf anlamına gelen "gramma" sözcüklerinin bir araya gelmesinden oluşur.

Program genetik algoritma yoluyla verdiğiniz metin dosyasından pangram elde etmenizi sağlıyor. Tek sorun: Anlamlı bir cümle oluşturmaması :) Yani yapmaya çalıştığı şey aslında "tüm harfleri barındıran en kısa cümleyi" bulmak.

Bazı örnek metinleri klasörde sundum. Kendi TXT dosyalarınızla da deneyebilirsiniz.

## Değişkenler

Bir bireyin genleri kelimelerden oluşur. Başlangıçta bireyler 4 gene sahiptir. Her bir gen, bir kelimedir.

DENEME SAYISI (Default=50.000)

Program denemeye 4 kelimeli bireylerle başlar. Burada belirlediğiniz deneme sayısı kadar nesil oluşturur. Bir pangrama ulaşırsa keser; ulaşamazsa 6 kelimelik bireylere evrilir. Yani deneme sayısı, evrilmeden önce kaç nesil deneme yapılacağının sayısıdır.

MUTASYON ORANI (Default=10)

Varsayılan değer 10'dur. Yani %10 olasılıkla her nesilde bir bireyin tüm genleri mutasyona uğrayacaktır. Başka bir deyişle gen havuzuna dört yeni kelime katılmış olacaktır (ya da 6, 8...).

YOL:

Metnin alınacağı TXT dosyasının yolduru. Varsayılan değeri: "digermetinler/cogulluk.txt"
