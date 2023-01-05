from django import forms
from .models import Books, IssuedBooks

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('author', 'title', 'desc')

class IssuedBooksForm(forms.ModelForm):
    class Meta:
        model = IssuedBooks
        fields = ('noOfDays',)