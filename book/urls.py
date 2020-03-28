from django.urls import path
from book import views

urlpatterns = [
    path('', views.index, name='index'),
    path('olajok/', views.olaj_list, name='olaj_list'),
    path('receptek/', views.recept_list, name='recept_list'),
    path('arak/', views.arak_list, name='arak_list'),
    path('olajok/<int:pk>', views.olaj, name='olaj'),
    path('receptek/<int:pk>', views.recept, name='recept'),
    path('forgalmazok/<int:pk>', views.forgalmazo, name='forgalmazo'),
]
