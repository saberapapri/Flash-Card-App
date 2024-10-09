

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import flashcard_list, add_flashcard, edit_flashcard, delete_flashcard, register

urlpatterns = [
    path('', flashcard_list, name='flashcard_list'),
    path('add/', add_flashcard, name='add_flashcard'),
    path('edit/<int:flashcard_id>/', edit_flashcard, name='edit_flashcard'),
    path('delete/<int:flashcard_id>/', delete_flashcard, name='delete_flashcard'),
    path('register/', register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='flashcards/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
