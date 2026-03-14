import time #zaman sayacı ekleyeceğiz
import random # soru seçmek için kullanıcaz
import os #dosya kontrolü için gerekli
import keyboard  # kullanıcıdan tuşu algılamak için kullanıcaz sayaç sırasında
oyundevametsin=True # oyunu devam edip bitirmekte kullacnağımız parametre


def sayac(süre=30):
    
    while süre > 0:
        print(f"Kalan süre: {süre} saniye.(cıkmak için space e bas)(ek süre jokeri için 1 e bas)", end="\r")
        #burada end = "r" ile yaparsak her seferinde kendi üzerine yazar ve sayaç akıyormuş gibi olur
        #bunun yerine end = "\n" olsaydı (default hali budur) alt alta yazardı her seferinde .deneyerek görebilrisin
        time.sleep(1)
        süre -= 1
        #eğer kullanıcı sayaç akarken space tuşuna basarsa süre dolmadan çıkabileecek
        if keyboard.is_pressed("space"):  # space tuşu dinleniyor
            print("\nSayaç kullanıcı tarafından durduruldu.")
            return
        elif keyboard.is_pressed("1"):
            süre+=30
            
    print("\nSüre doldu!")


    
# kullanıcıdan sayısal veri almak için fonksiyon
def input_int(mesaj, varsayılan=None) -> int:
    while True:
        metin = input(mesaj).strip()
        if not metin and varsayılan is not None:
            return varsayılan
        try:    
            return int(metin)
        except ValueError:
            print("lütfen sayısal bir değer girin")


# dosyamızı açıp kapatırken bu dosya yolunu kullanıcaz.
dosya_yolu = "C:\\Users\\Hasan Tuna\\Desktop\\var_mı_artıran\\sorular.txt"


     
class Jokerler():
    def __init__(self,eksüre,tamamlama)-> None:
         self.eksüre = eksüre
         self.tamamlama = tamamlama 
         
class Gruplar(Jokerler):
    gruplar=[]
    def __init__(self,isim,skor=3)->None:
        self.isim = isim 
        self.skor = skor  
        super().__init__(eksüre=30,tamamlama=30)#Jokerler classından miras alıyoruz
    @staticmethod
    def grupOlustur()->str:
        choose = input_int("Kaç grup olacak: ")
        for i in range(choose):
            isim = input(f"{i+1}. grubun ismini girin: ")
            grup = Gruplar(isim)
            Gruplar.gruplar.append(grup)

        print("\nGruplar oluşturuldu:")
        for g in Gruplar.gruplar:
            print(f"{g.isim} - Başlangıç skoru: {g.skor}")

#kullanılcak fonksiyonlar.   

def dosya_kontrol(dosya_yolu)->bool:
    """Dosyanın varlığını kontrol eder"""
    if not os.path.exists(dosya_yolu):
        print(f"⚠️ Hata: '{dosya_yolu}' dosyası bulunamadı!")
        return False
    return True

def sorulariOku(dosya_yolu)->None:
    """Sorular dosyasını okur"""
    try:
        if not dosya_kontrol(dosya_yolu):
            # Örnek sorular oluştur
            ornek_sorular = [
                "Türkiye'nin başkenti neresidir? - Ankara",
                "Dünyanın en büyük okyanusu hangisidir? - Pasifik",
                "1 dakikada kaç saniye vardır? - 60",
                "Güneş sistemindeki gezegen sayısı kaçtır? - 8",
                "Türkiye hangi kıtada yer alır? - Asya ve Avrupa"
            ]
            return ornek_sorular
            
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            sorular = [satir.strip() for satir in f.readlines() if satir.strip()]
        
        if not sorular:
            print("⚠️ Dosya boş! Örnek sorular kullanılacak.")
            return [
                "Örnek soru 1: 2+2 = ? - 4",
                "Örnek soru 2: Türkiye'nin başkenti? - Ankara"
            ]
        
        return sorular
        
    except Exception as e:
        print(f"⚠️ Dosya okuma hatası: {e}")
        return ["Örnek soru: Test sorusu - Test cevabı"]  
    
def rastgeleSoruSec(sorular)->str:
    print( random.choice(sorular))
    
def grupSec()->None:
        global oyundevametsin
    # Grupları listele
        for i, g in enumerate(Gruplar.gruplar, 1):
            print(f"{i}. {g.isim} (Skor: {g.skor})")

        # Kullanıcı hangi grubun cevap verdiğini seçsin
        choose = input_int("Hangi grup ihaleye girdi? (Numara):(cıkıs:-1) ")

        if 1 <= choose <= len(Gruplar.gruplar):
            secilen_grup = Gruplar.gruplar[choose-1]  # index = numara-1
            return secilen_grup           
        elif choose == -1 :
             oyundevametsin = False
             return None
        else:
            print("⚠️ Geçersiz seçim!")    
            
def skorArttir(grup, miktar=1)->str:
    #Seçilen grubun skorunu artırır
    global oyundevametsin
    grup.skor += miktar
    print(f"{grup.isim} grubunun skoru {miktar} puan artırıldı. Yeni skor: {grup.skor}")
    if grup.skor == 10:   
       print(f"{grup.isim} Oyunu Kazandı !!!")
       oyundevametsin = False
       
def skorAzalt(grup, miktar=1)->str:
    #Seçilen grubun skorunu azaltır
    global oyundevametsin 
    grup.skor -= miktar
    print(f"{grup.isim} grubunun skoru {miktar} puan azaltıldı. Yeni skor: {grup.skor}")
    if grup.skor == 0 :
        print(f"{grup.isim} Oyunu kaybetti !!!")
        oyundevametsin = False
    
             
def oyunBaslat()->None:
    Gruplar.grupOlustur()
    sorular = sorulariOku(dosya_yolu)
    global oyundevametsin
    oyundevametsin= True
    while oyundevametsin:
            soru = random.choice(sorular)
            print(f"soru: {soru}")
            secilen_grup= grupSec() 
            if secilen_grup is None:
               print("Oyun kullanıcı tarafından durduruldu.")
               break  # while döngüsünden çık
            input("zamanı başlatmak için enter a basın") 
                          
            sayac()
            
            print("1-Evet \n2-Hayır")    
            choose = input_int("grup doğru cevapladı mı: ")
            if choose == 1 :
                skorArttir(secilen_grup)
            elif choose == 2:
                skorAzalt(secilen_grup)
            else : 
                print("Hatalı Tuşlama")        

def oyunKurallari()->None:
    try:
        with open("oyunkurallari.txt","r",encoding="utf-8") as dosya:
            print("\n--- Oyun Kuralları ---")
            print(dosya.read())

    except FileNotFoundError:
        print("⚠️ 'oyunkurallari.txt' dosyası bulunamadı. Lütfen dosyayı oluşturun!")
    input("🔙 Menüye dönmek için Enter'a basın...")
            


def giris()->None:
    global oyundevametsin
    while oyundevametsin:
        print("Var mı Artıran Oyununa Hoş Geldiniz..")
        print("1-Oyun kuralları\n2-Oyuna Başla\n3-Cıkıs")
        choose= input_int("Lütfen seçim yapın: ")
        
        if choose == 1:
            oyunKurallari()
        elif choose==2: 
            oyunBaslat()
            
            
        elif choose ==3:
            print("Program kapanıyor !! ")
            oyundevametsin=False
            
        else: 
            print("Hatalı Tuşlama !!! ")
            
    
if __name__ == "__main__":
    giris()        
                                  

