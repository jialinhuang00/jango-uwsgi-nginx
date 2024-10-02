from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # 將 hello 應用的路由包含進來
    path('', include('ping.urls')),  # 將 hello 應用的路由包含進來
]
