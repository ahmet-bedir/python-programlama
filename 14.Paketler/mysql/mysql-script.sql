-- Yeni kullanıcı oluştur
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'u1';

-- Mevcut kullanıcıları listele
SELECT user, host FROM mysql.user;

-- Veritabanı oluştur
CREATE DATABASE storedb;

-- Kullanıcıya tam yetki ver
GRANT ALL PRIVILEGES ON storedb.* TO 'user1'@'localhost';

-- Oluşturulan veritabanına geç
USE storedb;

-- Tablo oluştur
CREATE TABLE products (
    product_id INT UNSIGNED AUTO_INCREMENT,
    product_name VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    product_image VARCHAR(30),
    description TEXT,
    registration_date DATE DEFAULT (CURRENT_DATE),  -- Bugünün tarihi
    categoryid INT UNSIGNED,
    CONSTRAINT products_pk PRIMARY KEY (product_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;

-- 
CREATE TABLE categories (
	category_id INT UNSIGNED AUTO_INCREMENT,
	category_name VARCHAR(30),
	CONSTRAINT categories_pk PRIMARY KEY (category_id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;

-- Froign key tanımı
ALTER TABLE products
ADD CONSTRAINT products_categories_fk
FOREIGN KEY (categoryid)
REFERENCES categories(category_id);

-- Veri ekle
INSERT INTO products
(product_name, price, product_image, description, registration_date, categoryid)
VALUES
('Laptop', 34999.99, 'laptop.jpg',
 '16 GB RAM, 512 GB SSD dizüstü bilgisayar',
 '2026-01-15', 1),

('Mekanik Klavye', 2499.90, 'klavye.jpg',
 'RGB aydınlatmalı mekanik klavye',
 '2026-01-18', 2),

('Kablosuz Mouse', 899.50, 'mouse.jpg',
 'Ergonomik kablosuz mouse',
 '2026-01-20', 2),

('27 Inch Monitör', 7999.00, 'monitor.jpg',
 '2K çözünürlüklü IPS monitör',
 '2026-01-22', 1),

('USB Bellek 64GB', 349.90, 'usb64.jpg',
 'USB 3.2 hızlı bellek',
 '2026-01-25', 3),

('Harici SSD 1TB', 4299.00, 'ssd1tb.jpg',
 'Taşınabilir SSD depolama',
 '2026-02-01', 3),

('Akıllı Telefon', 28999.00, 'telefon.jpg',
 '128 GB depolamalı akıllı telefon',
 '2026-02-05', 4),

('Tablet', 15999.00, 'tablet.jpg',
 '10.5 inç ekranlı tablet',
 '2026-02-08', 4),

('Bluetooth Kulaklık', 1799.90, 'kulaklik.jpg',
 'Kablosuz stereo kulaklık',
 '2026-02-10', 5),

('Akıllı Saat', 5499.90, 'saat.jpg',
 'Nabız ve uyku takibi özellikli',
 '2026-02-12', 5),

('Web Kamera', 1299.00, 'kamera.jpg',
 '1080p görüntü kalitesi',
 '2026-02-15', 6),

('Mikrofon', 1899.00, 'mikrofon.jpg',
 'Yayıncı tipi USB mikrofon',
 '2026-02-18', 6),

('Oyuncu Koltuğu', 8999.90, 'koltuk.jpg',
 'Ayarlanabilir ergonomik koltuk',
 '2026-02-20', 7),

('Yazıcı', 4499.00, 'yazici.jpg',
 'Renkli çok fonksiyonlu yazıcı',
 '2026-02-22', 8),

('Tarayıcı', 3199.90, 'tarayici.jpg',
 'Yüksek çözünürlüklü belge tarayıcı',
 '2026-02-25', 8),

('Ethernet Kablo', 149.90, 'ethernet.jpg',
 'Cat6 ağ kablosu',
 '2026-03-01', 9),

('WiFi Adaptörü', 699.90, 'wifi.jpg',
 'USB kablosuz ağ adaptörü',
 '2026-03-03', 9),

('Projeksiyon Cihazı', 12499.00, 'projeksiyon.jpg',
 'Full HD projeksiyon cihazı',
 '2026-03-05', 10),

('Powerbank 20000mAh', 1199.90, 'powerbank.jpg',
 'Hızlı şarj destekli',
 '2026-03-08', 11),

('Şarj Adaptörü', 499.90, 'adaptor.jpg',
 '65W Type-C adaptör',
 '2026-03-10', 11),

('HDMI Kablo', 199.90, 'hdmi.jpg',
 '2 metre HDMI kablo',
 '2026-03-12', 12),

('Hoparlör', 2499.00, 'hoparlor.jpg',
 'Bluetooth masaüstü hoparlör',
 '2026-03-15', 5),

('Ekran Kartı', 24999.00, 'gpu.jpg',
 '12 GB GDDR6 ekran kartı',
 '2026-03-18', 1),

('İşlemci', 14999.00, 'cpu.jpg',
 '8 çekirdekli performans işlemcisi',
 '2026-03-20', 1),

('Anakart', 7999.00, 'anakart.jpg',
 'ATX form faktörlü anakart',
 '2026-03-22', 1);
 
-- 
INSERT INTO categories (category_name) VALUES
('Bilgisayarlar'),
('Çevre Birimleri'),
('Depolama'),
('Mobil Cihazlar'),
('Ses Sistemleri'),
('Kamera ve Yayın'),
('Oyuncu Ekipmanları'),
('Ofis Ürünleri'),
('Ağ Ürünleri'),
('Görüntü Sistemleri');
-- 
SELECT * FROM products;
--
SELECT * FROM categories;

