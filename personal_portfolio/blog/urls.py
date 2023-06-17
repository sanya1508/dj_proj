from django.urls import path, include  # type: ignore
from . import views  # type: ignore

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]