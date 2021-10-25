from django.urls import path, include
from .views import UserList, UserDetails,GroupList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
path('users/', UserList.as_view()),
path('users/<pk>/', UserDetails.as_view()),
path('groups/', GroupList.as_view()),
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
