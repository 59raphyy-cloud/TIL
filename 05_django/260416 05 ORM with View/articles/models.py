from django.db import models


# 테이블 설계도 초안
class Article(models.Model):
    # 필드(컬럼)의 이름 == 클래스 변수명
    # 각 필드의 타입을 결정 하는 것 == model Field 클래스들
    # 제약조건 == model Field 클래스의 키워드 인자
    # id(primary key) 필드는 장고가 자동으로 설정
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# article = Article()

# 인스턴스 변수에 값을 할당
# 게시글의 제목과 내용을 작성하는 행위
# article.title = '제목'
# article.content = '내용'

# 게시글을 생성
# article 인스턴스가 save 인스턴스 메서드를 호출
# save 메서드는 작성된 데이터를 orm에게 db에 저장해달라 요청하는 것
# article.save()

# 클래스의 메서드
# 1. 인스턴스 메서드
# 2. 클래스 메서드
# 3. 스태틱 메서드