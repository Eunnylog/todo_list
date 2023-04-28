from django.urls import path,include
from users.views import UserDetailView
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),  # 회원가입
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 로그인
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:id>/', UserDetailView.as_view(), name='user_detail_view'),
]