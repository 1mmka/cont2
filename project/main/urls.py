from django.urls import path
from main.views import AllUsersView,UserInformation

urlpatterns = [
    path('',AllUsersView.as_view(),name='all_usernames'),
    path('user/<int:user_id>',UserInformation.as_view(),name='user_info')
]