-- ایجاد جدول Customers
CREATE TABLE Customers (
  id INTEGER PRIMARY KEY,
  name TEXT,
  city TEXT,
  country TEXT
);

-- ایجاد جدول Products
CREATE TABLE Products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  price REAL,
  count INTEGER
);

-- دستور INSERT برای وارد کردن اطلاعات دلخواه
INSERT INTO Customers (name, city, country) VALUES ('علی', 'تهران', 'ایران');
INSERT INTO Products (name, price, count) VALUES ('محصول ۱', 1000, 10);

-- دستور SELECT برای نمایش فقط کالاهای موجود
SELECT * FROM Products WHERE count > 0;

-- دستور DELETE برای حذف مشتریانی که ایرانی نیستند
DELETE FROM Customers WHERE country != 'ایران';

-- دستور UPDATE برای کاهش ۲۰ درصدی قیمت تمام کالاها
UPDATE Products SET price = price * 0.8;
