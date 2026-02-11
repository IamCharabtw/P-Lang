import sys
import os

class PMotoru:
    def __init__(self):
        self.hafiza = {}

    def deger_coz(self, ifade):
        if (ifade.startswith('"') and ifade.endswith('"')) or (ifade.startswith("'") and ifade.endswith("'")):
            return ifade[1:-1]
        if ifade in self.hafiza:
            return self.hafiza[ifade]
        try:
            # Sayısal işlemleri çöz
            return eval(ifade, {}, self.hafiza)
        except:
            return ifade

    def calistir(self, dosya_yolu):
        if not os.path.exists(dosya_yolu):
            print(f"Hata: '{dosya_yolu}' dosyası bulunamadı.")
            return

        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            satirlar = f.readlines()

        for satir in satirlar:
            satir = satir.strip()
            if not satir or satir.startswith('#'):
                continue

            if satir.startswith('yaz(') and satir.endswith(')'):
                icerik = satir[4:-1].strip()
                print(self.deger_coz(icerik))
            elif '=' in satir:
                deg_adi, deger = satir.split('=', 1)
                self.hafiza[deg_adi.strip()] = self.deger_coz(deger.strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python p_motor.py dosya_adi.p")
    else:
        p = PMotoru()
        p.calistir(sys.argv[1])