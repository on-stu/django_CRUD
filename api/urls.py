from django.urls import path, include
from api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='articles', viewset=ArticleViewSet, basename='articles')
urlpatterns = [
    path('', include(router.urls))
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>', ArticleDetail.as_view())
    # path('articles', article_list),
    # path('articles/<int:pk>', article_details)
]
