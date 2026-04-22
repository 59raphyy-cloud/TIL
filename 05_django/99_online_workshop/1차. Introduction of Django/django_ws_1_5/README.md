### 3223. 프로젝트 이름 수정하기(Lv5)

1. manage.py
    > os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_seccond_pjt.settings')

2. my_second_pjt/wsgi.py
    > os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_seccond_pjt.settings')

3. my_second_pjt/asgi.py
    > os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_seccond_pjt.settings')

4. my_second_pjt/settings.py
    > ROOT_URLCONF = 'my_seccond_pjt.urls'
    > WSGI_APPLICATION = 'my_seccond_pjt.wsgi.application'