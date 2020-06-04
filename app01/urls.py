from django.urls import path
from . import views


# urls : HTTP 요청에 알맞은 뷰를 호출 (모든 앱의 urls는 최상단 프로젝트의 urls.include()로부터 참조됨)


urlpatterns = [
    path('fileRequest/', views.fileRequest, name='fileRequest'),
    path('imageResponse/', views.imageResponse, name='imageResponse'),
]


