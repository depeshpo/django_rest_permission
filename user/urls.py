from rest_framework.routers import DefaultRouter
from django.urls import path, include

from user import views

router = DefaultRouter()
router.register('users', views.UserViewSet, base_name='user-list')
router.register('login', views.LoginView, base_name='login')

urlpatterns = [
    # path('users/', views.UserView.as_view(), name='users'),
    # path('users/add/', views.UserCreate.as_view(), name='user-add'),
    # path('users/update<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
    # path('users/delete<int:pk>', views.UserDeleteView.as_view(), name='user-delete'),
    path('', include(router.urls)),
    path('account/logout/', views.LogoutView.as_view(), name='logout'),
    # path('users/', views.UserViewSet.as_view(), name='user_list')
]
