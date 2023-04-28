from django.urls import path
from articles import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='Article_view'),  # 게시글 목록과 작성
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name="article_detail_view"),   # 게시글 상세페이지와 수정,삭제
]