from django.urls import path
from .views import HomePage, BlogListPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('blog/', BlogListPage.as_view(), name='blog'),
]