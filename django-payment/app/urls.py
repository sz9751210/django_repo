from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('update/<int:pk>', views.update, name='Update'), # name要與template的href同名
    path('delete/<int:pk>', views.delete, name='Delete'),
]