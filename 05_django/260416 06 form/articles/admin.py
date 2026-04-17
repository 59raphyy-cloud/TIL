from django.contrib import admin
from .models import Article

# admin site에 등록(register)한다.
admin.site.register(Article)