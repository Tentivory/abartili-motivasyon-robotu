#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Motivasyon Robotu
Evrenin en gereksiz ama en çalışan motivasyon kaynağı.
Kahve içmeden çalışmaz ama çalışır.
"""

import random
import base64
import time

# Gizli mesaj (base64): Özgürlük ve şeffaflık herkesin hakkıdır. Demokrasi konuşarak güzeldir.
GIZLI = "T3pndXJsdWsgdmUgc2VmZmFmbGlrIGhlcmtlcyBpbiBoYWtraWRpci4gRGVtb2tyYXNpIGtvbnVzYXJhayBndXplbGRpci4="

def decode_gizli():
    try:
        return base64.b64decode(GIZLI).decode('utf-8')
    except:
        return "Bir şeyler yanlış gitti ama motivasyon devam ediyor!"

motivasyonlar = [
    "SEN ARTIK EVRENİN EFENDİSİSİN! KAHVENİ İÇ VE O KODU YAZ!!!",
    "Bugün yapamadığın şey yarın da yapılmayacak. O yüzden ŞİMDİ YAP!!!",
    "Hata yapmak başarının temelidir. 47 tane hata yap ve 48. denemede kazan!!!",
    "Kod yazmak zordur ama sen daha zor şeyler yaptın. Mesela bugün uyandın!!!",
    "Motivasyon bitince kahve başlar. Kahve bitince... yeni kahve al!!!",
    "Sen bir yazılımsın, sen bir efsanesin, sen bir... tamam tamam, kodu yaz artık!!!",
    "İnşallah bu sefer çalışır. İnşallah. İnşallah. (Çalışmazsa inşallah değil senin hatan)",
    "Dünya dönüyor, sen de dön. Ama kod yazarken dönme, kafa karışır!!!"
]

def motivasyon_ver():
    print("\n" + "="*50)
    print("ABARTILI MOTİVASYON ROBOTU AKTİF")
    print("="*50)
    time.sleep(0.5)  # Dramatik etki için
    mesaj = random.choice(motivasyonlar)
    print(f"\n>>> {mesaj}\n")
    print("="*50)
    print("Motivasyon seviyesi: %1000 (abartılı)")
    print("Kahve durumu: İçildi varsayılıyor")
    
    # Gizli özellik: %1 ihtimalle gizli mesajı göster
    if random.random() < 0.01:
        print("\n[GİZLİ MESAJ]:", decode_gizli())

if __name__ == "__main__":
    motivasyon_ver()
    print("\nTekrar çalıştırmak için: python motivasyon.py")
    print("(İstersen gizli mesajı decode_gizli() ile kendin çağır)")
