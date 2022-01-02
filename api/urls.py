from django.urls import path, include
from rest_framework import viewsets
from api.views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='articles', viewset=ArticleViewSet, basename='articles')
router.register(prefix='users', viewset=UserViewSet, basename='users')
urlpatterns = [
    path('api/', include(router.urls))
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>', ArticleDetail.as_view())
    # path('articles', article_list),
    # path('articles/<int:pk>', article_details)
]
