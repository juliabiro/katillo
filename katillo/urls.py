"""katillo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from book.admin import beszerzes_admin, recept_admin, tudas_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beszerzes_admin/', beszerzes_admin.urls),
    path('tudas_admin/', tudas_admin.urls),
    path('recept_admin/', recept_admin.urls),
    path('', include('book.urls')),
]
admin.site.site_header = "Kati illóolajas könyve"
admin.site.site_title = "Kati illóolajas könyve"
admin.site.index_title = "Katillo"
