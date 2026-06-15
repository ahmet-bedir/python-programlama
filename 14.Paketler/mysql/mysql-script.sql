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


-- 
SELECT * FROM products;
--
SELECT * FROM categories;

