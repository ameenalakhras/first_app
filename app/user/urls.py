from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    # the name is good for using the url in the Reverse() function
    path('create/', views.CreateUserView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token")
]
