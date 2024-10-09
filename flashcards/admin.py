from django.contrib import admin
from .models import Flashcard

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'created_at')  # Customize columns
    list_filter = ('created_at',)  # Filter by creation date
    search_fields = ('question', 'answer')  # Search by question or answer
    ordering = ('-created_at',)  # Order by most recent
    list_per_page = 20  # Pagination

# Registering the Flashcard model with the admin
admin.site.register(Flashcard, FlashcardAdmin)
