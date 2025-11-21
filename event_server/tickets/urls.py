from django.urls import path
from .views import BookTicketView, MyTicketsView

urlpatterns = [
    path("book/", BookTicketView.as_view(), name="book-ticket"),
    path("booked/", MyTicketsView.as_view(), name="my-tickets"),
]
