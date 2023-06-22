from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', home),
    # path('add_student', post_student),
    # path('update_student/<int:id>/', update_student),
    # path('get_student/<int:id>/', get_student),
    # path('delete_student/<int:id>/', delete_student),

    path('get_books/', get_book),
    path('student/', StudentAPI.as_view()),
    path('register/', RegisterUser.as_view())
]
