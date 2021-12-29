from django.urls import path
from api.views import ArticleDetail, ArticleList
urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>', ArticleDetail.as_view())
    # path('articles', article_list),
    # path('articles/<int:pk>', article_details)
]
