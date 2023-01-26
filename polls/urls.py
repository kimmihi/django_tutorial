from django.urls import path
from . import views

# 다른 앱에 동일한 뷰 이름을 갖는 것이 있을 수 있기 때문에 app_name 지정
# 이는 템플릿에서 {% url %}  템플릿 태그 사용할 때 유용
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]