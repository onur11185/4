# bot_logic in original

import random


def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 2) 
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
def number():
    number = random.randint(1,10)
    return number

def fact():
    facts = [
        "İkinci el kıyafetler almak, tekstil endüstrisinin karbon ayak izini azaltır.",
        "Atlantiğin üstünden uçarak giden ilk kadın Amelia Earhart'dır",
        "Tekrar kullanılabilir çantalar, her yıl milyonlarca plastik poşeti engeller",
        "Beethoven duyma özelliğini kaybetmesine rağmen besteciliğe devam etti, 9. Semfonisini yazdıktan sonra komple saar oldu",
        "8 saatlik bir uykuda sadece 2 saat rüya görürsün, o 2 saatte en fazla 7 tane rüya görebilirsin",
        "Her 100 yılda bir, 1 gün 1.8 saniye artıyor",
        "Plastik, doğada 500 yıldan fazla kalabilen bir malzemedir",
        "İnsanlardan Küçük hayvanlar için zaman daha yavaş geçer",
        "Kompostlama, mutfak atıklarının yüzde 30'unu geri kazandırır",
        "1940 yılında Mike isimli bir tavuk kafasız çekilde 18 ay yaşadı",
        "Metal pipetler, her yıl denizlere karışan plastik atıkları azaltır",
        "Uzun Kelimelerden korkmaya verilen isim 'Hippopotomonstrosesquippedaliophobia'dır",
        "Dünya genelinde her yıl 1,3 milyar ton gıda israfı oluyor",
        "Gıda atıkları, tüm dünya metan gazı salınımının yüzde 8’ini oluşturur",
        "Dünyanın en çok yaşayan köpeği 29.5 yıl yaşadı",
        "Dünyanın en çok yaşayan kedisi 38 yıl 3 gün yaşadı",
        "Doğru geri dönüşüm, atıkların yüzde 75’inin yeniden kullanılmasını sağlar",
        "Testereler doğum için icat edilmişti",
        "Her yıl yaklaşık 92 milyon ton tekstil atığı oluşuyor",
        "Tek kullanımlık bez peçeteler, her yıl milyarlarca ton atık üretir"
    ]
    return random.choice(facts)


def ball8():
    answers = [
        "evet",
        "hayır",
        "belki"
    ]
    return random.choice(answers)

def commands():
    return ("?hello: Geri Selam Verir,?smile: Emoji yollar,?coin: Yazı Tura atar,?number: 1-10 arası rastgele sayı seçer,?pass: rastgele bir şifre oluşturur,?bye: 'Görüşürüz' Yazar,?facts: Bazı gerçekleri rastgele bir şekilde söyler,?8ball: komudu yazdıktan sonra sorduğun soruya karşılık rastgele cevap verir")
