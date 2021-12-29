from django.urls import path
from api.views import Index, article_details, article_list

urlpatterns = [
    path('', Index),
    path('articles', article_list),
    path('articles/<int:pk>', article_details)
]
