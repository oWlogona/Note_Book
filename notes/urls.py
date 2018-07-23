from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('add_note/', views.add_note, name='add_note'),
]
