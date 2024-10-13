import pygame
import sys

# Pygame'i başlat
pygame.init()

# Renkler
BEYAZ = (255, 255, 255)

# Pencere boyutu
GENISLIK, YUKSEKLIK = 600, 400
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Araba Oyunu")

# Saat ayarı (FPS için)
saat = pygame.time.Clock()

# Araba görselini yükle
araba_resmi = pygame.image.load('car.png')
araba_resmi = pygame.transform.scale(araba_resmi, (50, 100))  # Boyutu ayarla

arka_plan = pygame.image.load("carpark.png")
arka_plan = pygame.transform.scale(arka_plan, (GENISLIK, YUKSEKLIK))

# Araba başlangıç pozisyonu (araba sabit kalacak)
araba_x = GENISLIK // 2 - 25  # Araba her zaman ortada
araba_y = YUKSEKLIK - 110
araba_hizi = 5

# Arka plan kayma değişkeni
arka_plan_x = 0
arka_plan_hizi = 5  # Arka planın hareket hızı

# Oyun döngüsü
calisiyor = True
while calisiyor:
    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tuşlarla hareket
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        arka_plan_x += arka_plan_hizi  # Arka planı sağa kaydır
    if tuslar[pygame.K_RIGHT]:
        arka_plan_x -= arka_plan_hizi  # Arka planı sola kaydır

    # Arka planın sonsuz bir döngüde kayması için
    if arka_plan_x <= -GENISLIK:
        arka_plan_x = 0
    elif arka_plan_x >= GENISLIK:
        arka_plan_x = 0

    # Ekranı beyaz renkle temizle
    ekran.fill(BEYAZ)

    # Arka planı iki kez çizerek sürekli kaydırma efekti ver
    ekran.blit(arka_plan, (arka_plan_x, 0))
    ekran.blit(arka_plan, (arka_plan_x + GENISLIK, 0))

    # Arabayı ekranda çiz (araba sabit kalacak)
    ekran.blit(araba_resmi, (araba_x, araba_y))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    saat.tick(60)
