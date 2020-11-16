from django.urls import path
from osakkeet import views

urlpatterns = [
    path('', views.OsakeLista.as_view(), name='osakkeet'),
    path('new/', views.new, name='new'),
]