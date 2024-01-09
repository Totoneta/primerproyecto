from django.contrib import admin
from django.urls import path, include #agregar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('apppaginacoder.urls')) #urls incluidos de app
]
