from django.urls import path
# from rest_framework import routers

from . import views


# router = routers.DefaultRouter()
#rを文字列の前に付与してエスケープシーケンスを無効化し、そのままの文字として扱う
# router.register(r'quoteitem', views.DataListView)

app_name = 'apiapp'
urlpatterns = [
    path('data-list/', views.DataListView.as_view({'get': 'list'}), name='data-list')
]