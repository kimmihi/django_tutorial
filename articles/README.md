# Django REST Framework로 게시판 API 생성하기

### rest_framework 설치

아래 명령어를 실행시켜 설치한 다음에 `settings.py`의 `INSTALLED_APPS`에 "rest_framework"를 추가한다.

```shell
pip install djangorestframework
```

### Model 만들기

게시글에 대한 모델을 `models.py`에 생성한다.

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
```

### Serializer 만들기

Serializer는 데이터를 JSON으로 변환해주어 데이터를 쉽게 다룰 수 있도록 생성한다. serializer를 통해 효율적으로 유효성검사와 쿼리셋으로부터 데이터를 불러오는 것을 간단히 구현할 수 있다.

```python
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
```

위의 코드에서 `fields`를 설정할 수 있는데 모델에서 `fields`에서 정의한 것만 읽고 쓸 수 있도록 하는 것이다. 만약 읽거나 쓰기만 가능하도록 하려면 `read_only_fields`와 `write_only_fields`를 사용한다.

### View 만들기
