from django import forms
from django.contrib.auth.models import User
from .models import Flashcard


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  
       

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard  
        fields = ['question', 'answer']  

        

