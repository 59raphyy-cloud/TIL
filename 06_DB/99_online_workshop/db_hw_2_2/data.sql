-- 1-1. orders 테이블 생성
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL
);

-- 1-2. 데이터 삽입
INSERT INTO orders (order_date, total_amount) 
VALUES ('2023-07-15', 50.99);
INSERT INTO orders (order_date, total_amount) 
VALUES ('2023-07-16', 75.5);
INSERT INTO orders (order_date, total_amount) 
VALUES ('2023-07-17', 30.25);

-- 2-1. customers 테이블 생성
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT
);

-- 2-2. 데이터 삽입
INSERT INTO customers (name, email, phone) 
VALUES ('허균', 'hong.gildong@example.com', '010-1234-5678');
INSERT INTO customers (name, email, phone) 
VALUES ('김영희', 'kim.younghee@example.com', '010-9876-5432');
INSERT INTO customers (name, email, phone) 
VALUES ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');

-- 3-1. orders의 3번째 레코드 삭제
DELETE FROM orders 
WHERE order_id = 3;

-- 3-2. customers의 1번째 레코드의 name을 '홍길동'으로 수정
UPDATE customers 
SET name = '홍길동' 
WHERE customer_id = 1;

-- 4-1. orders의 모든 데이터 조회
SELECT * FROM orders;

-- 4-2. customers의 모든 데이터 조회
SELECT * FROM customers;