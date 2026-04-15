from django.db import models


# 테이블 설계도 초안
class Article(models.Model):
    # 필드(컬럼)의 이름 == 클래스 변수명
    # 각 필드의 타입을 결정하는 것 == model Feild 클래스
    # 제약조건 == model Field 클래스의 키워드 인자
    # id = models.AutoField(_("")) -> 원래 이거 설정해야 함
    # but id(primary key)는 django가 알아서 추가해주므로 직접 작성하지 않음
    title = models.CharField(max_length=10) # 제약 조건
    content = models.TextField()  # 길이 제한 없음(Large Mount). 무한은 아니지만 최대치의 문자열 저장
    content_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
