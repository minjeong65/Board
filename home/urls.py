from django.urls import path
from . import views

app_name = 'home' #앱 마다 별칭이 겹칠 수 있으므로 앱 이름으로 구분
urlpatterns = [
    path('', views.home, name = 'home'),
    path('create', views.create, name = "create"),
    path('detail/<bpk>', views.detail, name="detail"),
    path('modify/<bpk>', views.modify, name="modify"),
    path('delete/<bpk>', views.delete, name="delete"),
    path('addup/<bpk>', views.addup, name="addup"),
    path('removeup/<bpk>', views.removeup, name="removeup")
]