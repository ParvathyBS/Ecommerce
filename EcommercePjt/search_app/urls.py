from . import views
from django.urls import path

app_name = 'search_app'

urlpatterns = [
    path('search', views.search, name='search'),

]
