import pandas as pd
import os
from datetime import datetime

# Verilen metin
text = """
dispute - tartışma, münakaşa
growl - hırlamak, hırıltın
distilling - damıtma
gun - silah
divided - ayrılmış, bölünmüş
habit - huy, alışkanlık
doom - kıyamet
hammer - çekiç
doubtful - şüpheli, kuşkulu
harness - koşum takımı
drifted - yığılmak
harrow - tırmık
drop - damla
harvest - hasat
duty - görev, yükümlülük
hay - saman
effort - çaba
hedge - çit
enemy - düşman
hesitate - tereddüt etmek
engage in trade - ticaret yapmak
hind - arka
enthusiastic - hevesli, coşkulu
hoisting - çekmek, kaldırmak
equal - eşit
hoof (hooves) - toynak
escape - kaçma, kurtulma
hope - umut
evil - kötülük
horn - boynuz
except - hariç
inevitable - kaçınılmaz
excitement - heyecan, coşku
influence - etki, tesir
existence - varoluş
inn - meyhane
expelled - kovulmuş
instant - anında
explanation - açıklama
inventive - yaratıcı
exploit - istismar, sömürmek
irrepressible - durdurulamaz
expressed - ifade
faithful - sadık, bağlı, vefalı
jealous - kıskanç
fang - azı dişi
kind - tür, çeşit
fate - kader; son
laborious - zahmetli, yorucu
feather - kuş tüyü
lantern - fener
fertile - bereketli
lash - kamçı darbesi; kamçılamak
field - tarla, kır
launch - başlatmak
flutter - heyecan, telaş
lawsuit - dava
foal - tay
leisure - boş zaman, rahat
forelock - perçem, kakül
liberty - özgürlük
frank - dürüst, açık sözlü, samimi
loyalty - sadakat, bağlılık
gathering - toplama
lump - parça
grain - tahıl, tane
majority - çoğunluk
rubbish heap - çöplük
stroke - okşamak
ruin - harabe
struggle - savaş, mücadele
rumour - söylenti, dedikodu
suffer - acı çekmek; katlanmak
sacrifice - fedakarlık
sweated - terli
sake - hatır
tame - evcil
sand - kum
task - görev, iş
scattered - dağıtmak
tears - gözyaşı
scent - koku, esans
threshing - harman
schedule - programlamak
tool - alet
tormentor - işkenceci
scheme - şema, plan
trace - iz, işaret
seldom - nadiren
treachery - ihanet
sentimental - duygusal
trembled - titremek
settled - oturmuş
tremendous - muazzam
shed - kulübe
triumph - zafer
sill - eşik, pervaz
trotter - tirıs giden at; paça
situated - kurulu, bulunan
tyranny - zulüm, zorbalık
slave - esir, köle
udder - meme
sniff - koklamak
vain - nafile, boşuna
soil - toprak
voluntary - gönüllü
soul - ruh
vote - oy
sow - ekmek, tohum ekmek
wagged - sallamak
spread - yayılmış
weed - yabani ot
stable - ahır
well - kuyu
stalk - sap
wheat - buğday
stall - ahır
whip - kırbaç
staring - dik dik bakmak
whirling - fıldır fıldır dönmek
starve - açlıktan ölmek
windmill - yel değirmeni
steadily - sürekli
wing - kanat
stir - ayağa kaldırmak
wisdom - bilgelik
store - ambar
wise - bilge, akıllı
straw - saman
wisp - tutam, ufacık şey
stray - başıboş
worth - değerli
strip - şerit
yard - avlu
porker - domuz eti
mane - yele
precautions - önlemler
mantelpiece - şömine rafi
predict - önceden haber vermek
mare - kısrak
preparation - hazırlık
marvel - hayret etmek
prevail - galip gelmek, yenmek
mash - lapa, püre
previous - önceki, evvelki
mattress - şilte, yatak
primitive - ilkel
miserable - sefil, perişan, zavallı
principle - prensip, ilke
misery - acı, sefalet
produce - üretmek, yetiştirmek
mistaken - yanlış, hatalı
motto - slogan, parola
prophecy - kehanet
muted - sağır etmek
prosperity - refah, zenginlik
mysterious - gizemli, esrarengiz
prosperous - refah, zengin
neglected - bakımsız
proud - gururlu
nestled - sokulmak
purpose - amaç
nodded - başı ile onaylamak
purred - hırıldamak, mırıldamak
oat - yulaf
pursuing - peşinde
occupied - meşgul
rafter - çatı kirişi
opponents - rakipler
raise - kaldırmak, yükseltmek
orchard - meyve bahçesi
ration - yiyecek payı
raven - karga
pail - kova
rebellion - isyan, ayaklanma
pasture - otlak, çayır
rebuild - yeniden inşa etmek
paw - pati, pençe
reduced - indirgenmiş
pecking - gagalamak
regarded - saygın
perch - tünemek, konmak
persuade - ikna etmek
reign - egemenlik, hükümdarlık
rein - dizgin
phrase - ifade
pile of timber - kereste yığını
remark - açıklama
pipe - pipo
remove - uzaklaştırmak
plough - pulluk
resemble - benzemek
ploughland - sürülebilir toprak
resolution - kararlılık
poem - şiir
retreat - geri çekilmek
poison - zehir
ribbon - kurdele
pond - gölet
ridiculous - saçma, anlamsız
ripe - olgun
"""

# Satırlara ayır
lines = text.strip().split('\n')

# Listeleri oluştur
words_before_dash = []
words_after_dash = []

# Satırları işleyin
for line in lines:
    if "-" in line:
        parts = line.split(" - ")
        words_before_dash.append(parts[0].strip())
        words_after_dash.append(parts[1].strip())
    else:
        # "-" işareti olmayan satırları da uygun bir şekilde ekleyin
        words_before_dash.append(line.strip())
        words_after_dash.append('')  # Boş değer

# DataFrame oluştur
df_new = pd.DataFrame({
    'İngilizce': words_before_dash,
    'Türkçe': words_after_dash
})

# Güncel tarihi ve saati al
# current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Klasörü oluştur (varsa üzerine yazmaz)
os.makedirs('words', exist_ok=True)

# Dosya adı
file_name = 'words/en-words.xlsx'

# Dosya mevcutsa veriyi yükle, yoksa yeni dosya oluştur
if os.path.exists(file_name):
    # Mevcut dosyayı oku
    df_existing = pd.read_excel(file_name)
    # Yeni veriyi mevcut veriye ekle
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
else:
    # Dosya yoksa, sadece yeni veriyi kullan
    df_combined = df_new

# Excel dosyasına yaz
df_combined.to_excel(file_name, index=False)

print(f"Excel dosyası {file_name} olarak güncellendi.")
