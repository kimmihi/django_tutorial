# django_tutorial

## Part 1

### 프로젝트 생성하기

아래 명령어를 통해 프로젝트를 생성한다.

```shell
django-admin startproject server
```

### 프로젝트 생성 후 초기파일

- `manage.py` : Django 서비스를 실행시키기위한 커맨드라인의 유틸리티다.
- `server/` : 해당 디렉토리 내부에 프로젝트를 위한 실제 Python 패키지들이 저장된다.
- `server/__init__.py` : Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 단순한 빈 파일이다.
- `server/settings.py` : 현재 Django 프로젝트의 환경 및 구성을 저장한다.
- `server/urls.py` : 현재 Django Project의 URL을 선언한다.
- `server/asgi.py` : 현재 프로젝트를 서비스하기 위한 ASGI호환 웹 서버의 진입접이다.
- `server/wsgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI호환 웹 서버의 진입접이다.

### 개발서버 실행하기

Django Project 위치로 이동하여 아래 명령어를 실행시킨다.

```shell
python3 manage.py runserver
```

### 설문조사 앱 만들기

프로젝트 안에 앱을 만든다. 블로그를 개발한다고 했을 때 프로젝트 내에 게시글을 보여주는 앱인 `articles`를 만들 수 있고, 게시글을 관리하는 `admin` 앱을 만들 수 있다.

아래 명령어를 통해 설문조사 앱을 만든다.

```shell
python3 manage.py startapp polls
```

위의 명령어를 실행하면 프로젝트 하위에 `polls/` 폴더가 생기고 하위에 아래와같은 파일이 생성된다.

- `admin.py` : 해당 앱에 대한 관리자 인터페이스를 등록한다.
- `apps.py` : 해당 앱의 경로를 설정한다.
- `modeles.py` : 데이터베이스의 필드 및 데이터를 관리한다.
- `tests.py` : 테스트코드 작성한다.
- `views.py` : 모델의 정보를 받아 로직을 처리한다.
- `migrations/` : 모델에 대한 마이그레이션 내역을 저장한다.

그리고 아래 순서를 통해 특정 경로에 요청이 들어왔을 때 실행할 로직을 작성한다.

- `views.py`에 요청이 왔을 때 실행할 로직을 작성한다.
- `polls/urls.py`를 생성한다.
- `polls.urls.py`에 경로를 작성하고 `views.py`의 함수와 매칭시킨다.
- `server/urls.py`에 `polls` 앱의 경로를 추가한다.

---

## Part 2

### 데이터베이스 설치

Django는 기본적으로 SQLite를 사용하도록 구성되어있다. 하지만 다른 데이터베이스와 연동하여 개발할 수도 있다. ex) PostgreSQL

### 모델 만들기

`polls/modles.py`에 클래스를 사용하여 모델을 생성할 것이다. 모델은 데이터의 스키마 역할을 한다.

생성한 클래스별로 테이블이라고 생각하면된다. 해당 테이블 안에 어떤 형식을 갖는 데이터를 정의할 것인지 작성하였다. 또한 외래키를 사용하여 테이블간의 관계를 맺을 수도 있다.

### 모델의 활성화

`models.py`에서 생성한 모델은 데이터베이스 스키마를 생성하고 ORM을 통해 `Question`과 `Choice` 객체에 접근할 수 있다.

아래 명령을 실행시켜 변경시킨 모델을 migration으로 저장시킬 준비를 한다.(settings.py의 INSTALLED_APPS에 polls가 있어야한다.)

```shell
python manage.py makemigrations polls
```

그 다음 아래 명령을 통해 실제 마이그레이션을 적용한다. (데이터베이스에 모델과 관련된 테이블을 생성한다.)

```shell
python manage.py migrate polls
```

---

## Part 3

### view 추가하기

view에 요청이 왔을 때 처리할 로직을 작성하고, `urls.py`에 URL과 view를 매칭시켜준다.

`urls.py`에 URL을 작성할 때 `<int:question_id>`라고 작성했는데, 이는 URL에서 동적인 값을 받아 `question_id`라는 변수명으로 view 함수에서 받을 수 있다.

### 모델 불러오기

앱에 정의한 모델을 불러와서 특정 로직을 통해 데이터베이스에 저장된 데이터를 반환할 수 있다.

### 404에러 일으키기

404는 요청한 결과가 없을 경우 반환하는 응답 코드이다. `get_object_or_404()` 또는 `get_list_or_404()`를 통해 객체나 리스트가 있으면 이를 반환하고 없으면 404를 반환할 수 있다.

### 템플릿 적용하기

앱내에 템플릿을 만들어 view의 결과로 반환할 수 있다.

---
