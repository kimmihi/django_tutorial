# django_tutorial

## part1

---

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
