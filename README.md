# Var mı Artıran? - Bilgi ve Açık Artırma Oyunu 

Bu proje, Python ile geliştirilmiş interaktif bir konsol oyunudur. Gruplar halinde oynanan bu oyunda, takımlar sorulan sorular üzerine açık artırmaya girer (örneğin: "Ben 3 tane sayarım!", "Ben 5 tane sayarım!") ve iddialarını süre bitmeden kanıtlamaya çalışırlar.

##  Özellikler

* **Dinamik Grup Yönetimi:** İstediğiniz sayıda grup oluşturabilme.
* **Açık Artırma ve Süre Sistemi:** İhaleyi kazanan grup için 30 saniyelik geri sayım sayacı.
* **Joker Sistemi:** Her grubun zorlandığı anlarda klavyeden `1` tuşuna basarak kullanabileceği +30 saniye ek süre jokeri.
* **Erken Bitirme:** Sayma işlemi erken biterse `Space` tuşu ile sayacı anında durdurabilme özelliği.
* **Skor Takibi:** Doğru cevaplarda skor artışı, yanlışlarda skor düşüşü. 10 puana ulaşan kazanır, 0 puana düşen elenir!
* **Dosyadan Soru Okuma:** Sorular harici bir `.txt` dosyasından çekilir, böylece kodlara dokunmadan soru havuzu güncellenebilir.

## Gereksinimler

Oyunun sayaç sırasında klavye tuşlarını (Space ve 1) algılayabilmesi için `keyboard` kütüphanesi kullanılmaktadır. Projeyi çalıştırmadan önce bu kütüphaneyi kurmanız gerekir:

```bash
pip install keyboard