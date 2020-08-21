
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 앱 내부에서 순환할때는 views.home처럼 사용하면 된다.
]
