from django.urls import path
from . import views

app_name = 'basicApp'

urlpatterns = [
    path('appIndex/', views.BookListView.as_view(), name='books_list'),
    path('book/(?P<pk>\d+)', views.BookDetailView.as_view(), name='books_detail'),
    path('bookIssue/(?P<pk>\d+)', views.issueBookView, name='issue_book'),
    path('issueDetail/', views.issuedbookView, name='issueDetail')
]