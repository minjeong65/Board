from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #이미지 경로에 사용
from . import settings # ''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/', include('acc.urls')),
    path('book/',include('book.urls')),
    path('home/',include('home.urls')),
    path('trans/',include('trans.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #이미지 경로
