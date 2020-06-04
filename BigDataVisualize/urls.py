"""BigDataVisualize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


'''
urls.path(urlPattern, viewFunc, **kwargs, name)
    urlPattern : 비교할 URL패턴
    viewFunc : HTTP 요청의 URL과 urlPattern이 같으면 실행할 view의 함수 (단, HTTP 요청의 URL이 더 남았을 경우, urls.include() 사용해서 다른 URLconf 참조)
    **kwargs : viewFunc 인자로 사용할 dict
    name : URL에 붙일 이름 (이름을 사용하여 어디서든 참조 가능)
'''
'''
urls.include() 함수는 다른 URLconf 참조할 수 있도록 해줌
'''


urlpatterns = [
    path('app01/', include('app01.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)