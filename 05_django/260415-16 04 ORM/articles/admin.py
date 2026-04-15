from django.contrib import admin
from .models import Article

# admin 페이지에 등록
# admin site에 등록(register)한다.
admin.site.register(Article)