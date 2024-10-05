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


# Araba başlangıç pozisyonu
araba_x = GENISLIK//2 - 25
araba_y = YUKSEKLIK - 110
araba_hizi = 5

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
    if tuslar[pygame.K_LEFT] and araba_x > 0:
        araba_x -= araba_hizi
    if tuslar[pygame.K_RIGHT] and araba_x < GENISLIK - 50:
        araba_x += araba_hizi
    if tuslar[pygame.K_UP] and araba_y > 0:
        araba_y -= araba_hizi
    if tuslar[pygame.K_DOWN] and araba_y < YUKSEKLIK - 100:
        araba_y += araba_hizi

    # Ekranı beyaz renkle temizle
    ekran.fill(BEYAZ)

    # Arabayı ekranda çiz
    ekran.blit(arka_plan, (0,0))
    ekran.blit(araba_resmi, (araba_x, araba_y))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    saat.tick(60)
    



