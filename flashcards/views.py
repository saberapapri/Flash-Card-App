# flashcards/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import UserRegistrationForm, FlashcardForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the password
            user.save()
            return redirect('flashcard_list')  # Redirect to the flashcard list or login page
    else:
        form = UserRegistrationForm()
    return render(request, 'flashcards/register.html', {'form': form})


def edit_flashcard(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    
    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm(instance=flashcard)

    return render(request, 'flashcards/edit_flashcard.html', {'flashcard': flashcard, 'form': form})


def delete_flashcard(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    if request.method == "POST":
        
        flashcard.delete()
        return redirect('flashcard_list')
    return render(request, 'flashcards/delete_flashcard.html', {'flashcard': flashcard})


def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})


def add_flashcard(request):
    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        Flashcard.objects.create(question=question, answer=answer)
        return redirect('flashcard_list')
    return render(request, 'flashcards/add_flashcard.html')
