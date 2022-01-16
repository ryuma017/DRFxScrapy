from django.contrib import admin
from django.urls import include, path

# from apiapp.urls import router as apiapp_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiapp.urls')),
    path('', include('browse.urls')),
]
