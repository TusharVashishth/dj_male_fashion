from django.urls import path
from .views import user_form ,update_address

urlpatterns = [
    path('', user_form, name='user_address'),
    path('update/',update_address , name='update_user_address'),
]
