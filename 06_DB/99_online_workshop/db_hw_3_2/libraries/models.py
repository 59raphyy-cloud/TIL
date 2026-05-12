from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    birth = models.DateField()
    nationality = models.CharField(max_length=50)

    # 관리자 페이지 저자 목록 정보에서 각 저자의 이름이 표기되도록 매직메서드를 활용하여 설정
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    adult = models.BooleanField(default=False)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
