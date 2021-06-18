from django.urls import path
from .views import FlightListView, FlightDetailView

urlpatterns = [
    path('', FlightListView.as_view()),
    path('<int:pk>/', FlightDetailView.as_view())
]