-- Active: 1777334663300@@127.0.0.1@3306
-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

-- 실습 테이블 생성
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 1. Insert data into table
INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('hello', 'world', '2000-01-01');


INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('제목', '내용', DATE());


-- 2. Update data in table
UPDATE 
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

-- 전체 레코드를 수정하지 않는 단계적 방법
-- 1. 먼저 SELECT로 검증
-- (1) 영향 받을 행을 확인
-- SELECT * FROM articles WHERE id = 1;
-- (2) 확인 후 UPDATE/DELETE

UPDATE 
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

-- 3. Delete data from table
DELETE FROM
  articles
WHERE
  id = 1;


-- 심화
-- 작성일이 오래된 순으로 레코드 2개를 조회
SELECT
  id, createdAt
FROM
  articles
ORDER BY
  createdAt ASC
LIMIT 2;


DELETE FROM articles
WHERE id IN (
  SELECT id
  FROM articles
  ORDER BY createdAt ASC
  LIMIT 2
);

