from django.urls import path
from . import views

app_name="catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name ='books'),
    path('book/<int:pk>', views.book_detail_view, name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]