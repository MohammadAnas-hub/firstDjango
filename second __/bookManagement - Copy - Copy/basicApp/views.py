from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Books, IssuedBooks
from django.contrib.auth.decorators import login_required
from .forms import IssuedBooksForm
from accounts.models import User


# Create your views here.
class AppIndex(TemplateView):
    template_name = 'appIndex.html'

class BookListView(ListView):
    model = Books

    def get_queryset(self):
        return Books.objects.filter(in_stock__isnull=False)

class BookDetailView(DetailView):
    model = Books

@login_required
def issueBookView(request, pk):
    book = get_object_or_404(Books, pk=pk)
    user = request.user
    if request.method == 'POST':
        form = IssuedBooksForm(request.POST)
        
        if form.is_valid() and user.is_authenticated:
            x = form.save(commit=False)
            book.issue()
            book.save()
            x.book = book
            x.user = user
            x.save()
            return redirect('basicApp:books_list')
    else:
        form = IssuedBooksForm()
    
    return render(request, 'basicApp/issueBook.html', {'form':form})

@login_required
def issuedbookView(request):
    user = request.user.id


    books = IssuedBooks.objects.filter(user_id=user)
    username = request.user
    return render(request, 'basicApp/issuedbooks_detail.html', {'books':books, 'user':username})