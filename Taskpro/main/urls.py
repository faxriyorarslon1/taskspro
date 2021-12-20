from django.urls import path
from .views import main_page, gallery_page


urlpatterns = [
    path('gallery/', gallery_page, name='gallery' ),
    path('',main_page, name='main_page')
]