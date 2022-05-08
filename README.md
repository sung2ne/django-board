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

### 게시글 목록 구현 순서

1. 템플릿(프로젝트/templates/board/list.html)
2. 모델(프로젝트/board/models.py)
3. 뷰(프로젝트/board/views.py)
4. URL(프로젝트/board/urls.py)

### 게시글 등록 구현 순서

1. 템플릿(프로젝트/templates/board/create.html)
2. 폼(프로젝트/board/forms.py)
3. 뷰(프로젝트/board/views.py)
4. URL(프로젝트/board/urls.py)

### 게시글 보기 구현 순서

1. 템플릿(프로젝트/templates/board/read.html)
2. 뷰(프로젝트/board/views.py)
3. URL(프로젝트/board/urls.py)

### 게시글 수정 구현 순서

1. 템플릿(프로젝트/templates/board/update.html)
2. 폼(프로젝트/board/forms.py)
3. 뷰(프로젝트/board/views.py)
4. URL(프로젝트/board/urls.py)

### 게시글 삭제 구현 순서

1. 뷰(프로젝트/board/views.py)
2. URL(프로젝트/board/urls.py)

### 댓글 보기 구현 순서

1. 모델(프로젝트/board/models.py)
2. 템플릿(프로젝트/templates/board/read.html)
3. 뷰(프로젝트/board/views.py)

### 댓글 등록 구현 순서

1. 폼(프로젝트/board/forms.py)
2. 템플릿(프로젝트/templates/board/read.html)
3. 뷰(프로젝트/board/views.py)
4. URL(프로젝트/board/urls.py)

### 댓글 수정 구현 순서

1. 폼(프로젝트/board/forms.py)
2. 템플릿(프로젝트/templates/board/read.html)
3. 뷰(프로젝트/board/views.py)
4. URL(프로젝트/board/urls.py)

### 댓글 삭제 구현 순서

1. 뷰(프로젝트/board/views.py)
2. URL(프로젝트/board/urls.py)

## 미션

1. 게시글 등록 후 게시글 목록이 아니라 게시글 보기로 넘어가기
2. 게시글 보기에서 본인글이 아니면 수정/삭제 버튼 숨김 처리
3. 댓글 보기에서 본인글이 아니면 수정/삭제 버튼 숨김 처리
4. 게시글 등록에서 목록 버튼 누르면 1페이지 목록이 아니라 이전에 보던 페이지 목록으로 넘어가기
