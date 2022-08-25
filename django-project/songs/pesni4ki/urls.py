from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('pesen/<int:pk>', views.SongDetailView.as_view(), name='song-detail'),
]