# 장고를 이용한 게시판

## 실행

### 최초 실행

```shell
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

### 서버 실행

```shell
python manage.py runserver
```

## 정적파일

### BASE_DIR/config/settings.py

- https://docs.djangoproject.com/ko/4.0/howto/static-files/

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

## 템플릿

### BASE_DIR/config/settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## 데이터베이스

### BASE_DIR/config/settings.py

- https://docs.djangoproject.com/en/4.0/ref/settings/#databases

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 기능 구현 순서

### 일반적인 형태

1. 템플릿(프로젝트/templates/app/기능.html)
2. 모델(프로젝트/앱/models.py)
3. 뷰(프로젝트/앱/views.py)
4. URL(프로젝트/앱/urls.py)

### 로그인 구현 순서

1. 템플릿(프로젝트/templates/common/login.html)
2. 모델 => 장고 사용자 모델을 활용
3. 뷰 => 장고 로그인 기능 활용
4. URL(프로젝트/common/urls.py)

### 사용자 정보 보기 구현 순서

1. 템플릿(프로젝트/templates/common/profile_view.html)
2. 모델 => 장고 사용자 모델을 활용
3. 뷰(프로젝트/common/views.py)
4. URL(프로젝트/common/urls.py)

### 사용자 정보 수정 구현 순서

1. 템플릿(프로젝트/templates/common/profile_edit.html)
2. 모델 => 장고 사용자 모델을 활용
3. 폼(프로젝트/common/forms.py)
4. 뷰(프로젝트/common/views.py)
5. URL(프로젝트/common/urls.py)

### 비밀번호 수정 구현 순서

1. 템플릿(프로젝트/templates/common/password_edit.html)
2. 모델 => 장고 사용자 모델을 활용
3. 폼(프로젝트/common/forms.py)
4. 뷰(프로젝트/common/views.py)
5. URL(프로젝트/common/urls.py)

### 로그아웃 구현 순서

1. URL(프로젝트/common/urls.py)

